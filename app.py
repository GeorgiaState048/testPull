"""app file"""
import os
import random
import flask
from tmdb_wiki import get_movie_data, wiki_page


app = flask.Flask(__name__)
"""routes interpret different pages of a page"""
three = set()
@app.route("/")
def index():
    """home page"""
    external_ids = ["27205", "557", "419430", "496243"]
    if len(three) == 3:
        threes = list(three)
        external_id = random.choice(threes)
    else:
        external_id = random.choice(external_ids)
        three.add(external_id)
    print(three)
    movie_data = get_movie_data(external_id)
    wiki_link = wiki_page(movie_data[0], movie_data[4])
    return flask.render_template(
        "test.html",
        data=movie_data,
        link=wiki_link
        )

app.run()
