"""app file"""
import os
import random
import flask
from flask import url_for
from tmdb_wiki import get_movie_data, wiki_page
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = flask.Flask(__name__)

# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zevcghcsspxyhs:b9c4248c91bada3bd2a38b6ce4c95b5a3b5e793f7d6732c269450ec7738cfaf8@ec2-35-175-68-90.compute-1.amazonaws.com:5432/db65homnul3lba"
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'this is a secret key!!!'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

@login_manager.user_loader
def load_user(user_id):
    """load_user"""
    return User.query.get(int(user_id)) # might have to change the cast

class User(db.Model, UserMixin):
    """user class"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique = True)
    password = db.Column(db.String(80), nullable=False, unique = False)

class RegisterForm(FlaskForm):
    """register form"""
    username=StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password=StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    submit=SubmitField("Register")

    def validate_username(self, username):
        """checks username"""
        existing_user_username = User.query.filter_by(
            username = username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose a different one"
            )

class LoginForm(FlaskForm):
    """login form"""
    username=StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password=StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit=SubmitField("Login")

db.create_all()

"""routes interpret different pages of a page"""
@app.route("/")
def index():
    """landing page"""
    return flask.render_template("index.html")

@app.route("/homepage")
def home_page():
    """home page"""
    external_ids = ["27205", "557", "419430", "496243"]
    external_id = random.choice(external_ids)
    movie_data = get_movie_data(external_id)
    wiki_link = wiki_page(movie_data[0], movie_data[4])
    return flask.render_template(
        "home.html",
        data=movie_data,
        link=wiki_link
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    """login page"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return flask.redirect(flask.url_for('dashboard'))
    return flask.render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """register page"""
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = str(bcrypt.generate_password_hash(form.password.data))
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return flask.redirect(flask.url_for('login'))
    return flask.render_template('register.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """dashboard"""
    return flask.render_template('dashboard.html')



app.run(debug=True)
