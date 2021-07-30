from pyhtml import *
from flask import url_for
from src.imdb_requests import *

def get_movie_list(movie_ID, api_key):
    get_all_movies = get_movie_list_request(movie_ID, api_key)
    # Check for 400/500 Internal Server Error
    if (get_all_movies.status_code == 500 or get_all_movies.status_code == 400):
        return False
    else:
        info = get_all_movies.json()
        # Check if there are any movies available from search
        if (get_all_movies.status_code == 200 and len(info) == 4):
            return False

    movie_list = {}
    for data in info['results']:

        # Exclude anything such as actors, filming locations, directors, tv episodes, unreleased etc..
        if (data.get("titleType") != None and data.get("year") != None and data["titleType"]!= "tvEpisode"):
            
            # ID
            id = data['id'][7:-1]
            movie_list[id] = {}

            # Title of movie
            title = data.get("title")
            movie_list[id]['title'] = title

            # Year movie was released
            release_date = data.get("year")
            movie_list[id]['year'] = release_date

            # Type of movie (Movie, TV, Mini, Short)
            movie_type = data.get("titleType")
            movie_list[id]['type'] = movie_type

            # Poster/Image of the movie
            if (data.get('image') == None):
                movie_image_path = "/public/img/null_image.png"
            else:
                movie_image_path = data['image']["url"]
            movie_list[id]['img'] = movie_image_path

    return movie_list

# Construct HTML cards for the amount of movies in movie list
def construct_movie_cards(movie_list):
    movie_cards = []
    for movie_id in movie_list:
        movie_cards.append(
            div(class_="card")(
                a(href=url_for('advisory', movie_ID=movie_id))(
                    img(src=f"{movie_list[movie_id]['img']}", class_="card-img-top selector", alt=f"{movie_list[movie_id]['title']} ({movie_list[movie_id]['year']})"),
                    div(class_="card-body")(
                        h5(class_="card-title")(
                            f"{movie_list[movie_id]['title']}"
                        ),
                        h5(f"({movie_list[movie_id]['year']})"),
                        p(f"{format_movie_type_string(movie_list[movie_id]['type']) }")
                    )
                )
            ))
    return movie_cards

# Cleans the movie type string
def format_movie_type_string(movie_type):
    if (movie_type == "movie"):
        movie_type = "Movie"
    elif (movie_type == "tvMovie"):
        movie_type = "TV Movie"
    elif (movie_type == "videoGame"):
        movie_type = "Video Game"
    elif (movie_type == "tvSeries"):
        movie_type = "TV Series"
    elif (movie_type == "short"):
        movie_type = "Short"
    elif (movie_type == "tvEpisode"):
        movie_type = "TV Episode"
    elif (movie_type == "video"):
        movie_type = "Video"
    return movie_type