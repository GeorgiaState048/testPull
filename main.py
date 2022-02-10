import flask
from tmdb import get_movie_data
import random

app = flask.Flask(__name__)
"""routes interpret different pages of a page"""

@app.route("/")
def index():
    """home page"""
    external_ids = ["558", "557", "419430", "634649"]
    external_id = random.choice(external_ids)
    movie_data = get_movie_data(external_id)
    return flask.render_template(
        "index.html",
        data=movie_data,
        )
    #return "Hello World"

@app.route("/movie_one.html")
def movie_one():
    """movie_one page"""
    external_ids = ["558", "557", "419430", "634649"]
    external_id = random.choice(external_ids)
    movie_data = get_movie_data(external_id)
    return flask.render_template(
        "movie_one.html",
        data=movie_data,
        )

app.run()
