from pyhtml import *

# Construct HTML cards for the amount of movies in movie list
def constructMovieCard(movie_list):
    cards_str = ""
    for id in movie_list:
        movie_img = movie_list[id]['img']
        movie_name = movie_list[id]['title']
        movie_year = movie_list[id]['year']
        movie_type = movie_list[id]['type']
        
        movie_ratings = movie_list[id]['rating']
        if (movie_ratings == None):
            movie_ratings = "Not Yet Rated"
        else:
            movie_ratings = f"{movie_ratings}/10"

        list_of_div_cards = div(class_="card")(
                a(href="http://google.com")(
                    img(src=f"{movie_img}", class_="card-img-top selector", alt=f"{movie_name} ({movie_year})"),
                    div(class_="card-body")(
                        h5(class_="card-title")(
                            f"{movie_name} ({movie_year})"
                        ),
                        p(f"{formatMovieTypeString(movie_type)} - {movie_ratings}")
                    )
                )
        )
        cards_str = cards_str + str(list_of_div_cards)
    return cards_str

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