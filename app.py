"""app file"""
import os
import random
import flask
from tmdb_wiki import get_movie_data, wiki_page
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pnjonadutwpcns:68c0e33ca6cea3a2c70487bf5694f03e185232d4636ce2c57844651ca3b180ce@ec2-44-192-245-97.compute-1.amazonaws.com:5432/ddggelsgi946kc"
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app = flask.Flask(__name__)
"""routes interpret different pages of a page"""
three = set()
@app.route("/")
def index():
    """home page"""
    external_ids = ["27205", "557", "419430", "496243"]
    external_id = random.choice(external_ids)
    movie_data = get_movie_data(external_id)
    wiki_link = wiki_page(movie_data[0], movie_data[4])
    return flask.render_template(
        "index.html",
        data=movie_data,
        link=wiki_link
        )

app.run(debug=True)
