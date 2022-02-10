import flask
from tmdb import get_movie_data, wiki_page
import random

app = flask.Flask(__name__)
"""routes interpret different pages of a page"""

@app.route("/")
def index():
    """home page"""
    external_ids = ["558", "557", "419430", "634649"]
    external_id = random.choice(external_ids)
    movie_data = get_movie_data(external_id)
    wiki_link = wiki_page(movie_data[0], movie_data[4])
    return flask.render_template(
        "index.html",
        data=movie_data,
        link=wiki_link
        )

app.run()
