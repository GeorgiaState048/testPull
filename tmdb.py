"""program to find new movies"""
import os
from re import search
import requests
from dotenv import load_dotenv, find_dotenv

# will probably be using this to find movie information:
# https://developers.themoviedb.org/3/find/find-by-id

load_dotenv(find_dotenv())
# BASE_URL = "https://api.themoviedb.org/3/trending/movie/week?api_key=" + os.getenv("TMDB_KEY")
# image_base = https://image.tmdb.org/t/p/w500/

def get_movie_data(external_id):
    """returns info about a movie"""
    base_url = "https://api.themoviedb.org/3/movie/" + external_id + \
        "?api_key="+os.getenv("TMDB_KEY")+"&language=en-US"
    response = requests.get(base_url)
    response_json = response.json()
    genre_ids = response_json['genres']
    genres = []
    for i, value in enumerate(genre_ids):
        genres.append(genre_ids[i]['name'])
    title = response_json['original_title']
    overview = response_json['overview']
    genre_names = ', '.join(genres)
    picture = "https://image.tmdb.org/t/p/w500" + response_json['poster_path']
    date = response_json['release_date'][0:4]
    return  [title, overview, genre_names, picture, date]

def wiki_page(title, year):
    """wikipedia api"""
    movie = title + year
    base_url = "https://en.wikipedia.org/w/api.php"
    query_params = {
        "action": "opensearch",
        "search": movie,
        "format": "json",
    }

    the_response = requests.get(base_url, params=query_params)
    json_response = the_response.json()
    return json_response[3][0]
