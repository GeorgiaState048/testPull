"""program to find new movies"""
import os
import requests
from dotenv import load_dotenv, find_dotenv


# will probably be using this to find movie information:
# https://developers.themoviedb.org/3/find/find-by-id

load_dotenv(find_dotenv())
# BASE_URL = "https://api.themoviedb.org/3/trending/movie/week?api_key=" + os.getenv("TMDB_KEY")
# image_base = https://image.tmdb.org/t/p/w500/

def get_movie_data():
    """returns info about a movie"""
    base_url = "https://api.themoviedb.org/3/search/movie?api_key="+os.getenv("TMDB_KEY")+ \
    "&language=en-US&query=Interstellar&page=1&include_adult=false"

    query_params = {

    }

    response = requests.get(base_url, params=query_params)
    response_json = response.json()
    results = response_json['results']

    return [results[0]['original_title'], results[0]['genre_ids'], "https://image.tmdb.org/t/p/w500" + results[0]['backdrop_path'], results[0]['overview']]

def get_genre_info():
    """getting genre info"""
    genres = set(get_movie_data()[1])
    final = []
    base_url = "https://api.themoviedb.org/3/genre/movie/list?api_key="+os.getenv("TMDB_KEY")+"&language=en-US"
    response = requests.get(base_url)
    response_json = response.json()
    results = response_json['genres']
    for i, value in enumerate(results):
        curr = results[i]
        if curr['id'] in genres:
            final.append(results[i]['name'])
    return ', '.join(final)
