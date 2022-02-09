import flask
from tmdb import get_movie_data

app = flask.Flask(__name__)
"""routes interpret different pages of a page"""

@app.route("/")
def index():
    """home page"""
    return flask.render_template("index.html")
    #return "Hello World"

@app.route("/movie_one.html")
def movie_one():
    """movie_one page"""
    external_id = "157336"
    movie_data = get_movie_data(external_id)
    return flask.render_template(
        "movie_one.html",
        data=movie_data,
        )

@app.route("/movie_two.html")
def movie_two():
    """movie_two page"""
    return flask.render_template("movie_two.html")

@app.route("/movie_three.html")
def movie_three():
    """movie_three page"""
    return flask.render_template("movie_three.html")

@app.route("/movie_four.html")
def movie_four():
    """movie_four page"""
    return flask.render_template("movie_four.html")

@app.route("/movie_five.html")
def movie_five():
    """movie_five page"""
    return flask.render_template("movie_five.html")

app.run()
