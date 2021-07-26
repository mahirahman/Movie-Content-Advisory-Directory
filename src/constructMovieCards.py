from pyhtml import *
from flask import url_for

# Construct HTML cards for the amount of movies in movie list
def constructMovieCards(movie_list):
    movie_cards = []
    for movie_id in movie_list:
        movie_cards.append(
            div(class_="card")(
                a(href=url_for('advisory', movie_ID=movie_id))(
                    img(src=f"{movie_list[movie_id]['img']}", class_="card-img-top selector", alt=f"{movie_list[movie_id]['title']} ({movie_list[movie_id]['year']})"),
                    div(class_="card-body")(
                        h5(class_="card-title")(
                            f"{movie_list[movie_id]['title']} ({movie_list[movie_id]['year']})"
                        ),
                        p(f"{formatMovieTypeString(movie_list[movie_id]['type']) }")
                    )
                )
            ))
    return movie_cards

# Cleans the movie type string
def formatMovieTypeString(movie_type):
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