"""app file"""
import os
import random
import flask
from flask import url_for
from tmdb_wiki import get_movie_data, wiki_page
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import psycopg2
from wtforms.validators import InputRequired, Length, ValidationError

app = flask.Flask(__name__)

# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zevcghcsspxyhs:b9c4248c91bada3bd2a38b6ce4c95b5a3b5e793f7d6732c269450ec7738cfaf8@ec2-35-175-68-90.compute-1.amazonaws.com:5432/db65homnul3lba"
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'this is a secret key!!!'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

@login_manager.user_loader
def load_user(user_id):
    """load_user"""
    return User.query.get(int(user_id)) # might have to change the cast

class AllData(db.Model):
    """class person"""
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(120), unique=False, nullable=False)
    movie_id = db.Column(db.String(80), unique=False, nullable=False)
    user = db.Column(db.String(80), unique=False, nullable=False)
    rating = db.Column(db.String(80), unique=False, nullable=False)

class User(db.Model, UserMixin):
    """user class"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique = True)

class RegisterForm(FlaskForm):
    """register form"""
    username=StringField(validators=[InputRequired(), Length(
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
    submit=SubmitField("Login")

db.create_all()

# routes interpret different pages of a page
@app.route("/")
def index():
    """landing page"""
    return flask.render_template("index.html")

@app.route("/homepage/<name>", methods=['GET', 'POST'])
def home_page(name):
    """home page"""
    external_ids = ["27205", "557", "419430", "496243"]
    new_id = random.choice(external_ids)
    movie_data = get_movie_data(new_id)
    wiki_link = wiki_page(movie_data[0], movie_data[4])
    if flask.request.method == "POST":
        data = flask.request.form
        this_id = flask.request.form['movie_id']
        add_comment = data.get("comment")
        add_rating = data.get("rating")
        if not add_comment:
            add_comment = name + " did not leave a comment!"
        if not add_rating:
            add_rating = name + " did not leave a rating!"
        if add_comment and add_rating:
            new_review = AllData(comment=add_comment, rating=add_rating, movie_id=this_id, user=name)
            db.session.add(new_review)
            db.session.commit()
    review_data = AllData.query.filter_by(movie_id=new_id).all()
    num_review_data = len(review_data)
    return flask.render_template(
        "home.html",
        review_data=review_data,
        num_review_data=num_review_data,
        movie_id=new_id,
        name=name,
        movie_data=movie_data,
        link=wiki_link
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    """login page"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        name = form.username.data
        if user:
            login_user(user)
            return flask.redirect(flask.url_for('home_page', name=name))
    return flask.render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """register page"""
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        db.session.add(new_user)
        db.session.commit()
        return flask.redirect(flask.url_for('login'))
    return flask.render_template('register.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    """logout"""
    logout_user()
    return flask.redirect(flask.url_for('login'))

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8000)),
    debug=True
)
