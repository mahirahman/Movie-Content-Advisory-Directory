from src.imdb_requests import *

# Produces a dictionary of movies from API
# If the API produces an error it will return None
def get_movie_dict(movie_ID, api_key):
    get_all_movies = get_movies_dict_request(movie_ID, api_key)
    # Check for 400/500 Internal Server and Bad Connection Error
    if (get_all_movies == None or get_all_movies.status_code == 500 or get_all_movies.status_code == 400):
        return False
    else:
        info = get_all_movies.json()
        # Check if there are any movies available from search
        if ('results' not in info):
            return False

    movies_dict = {}
    for data in info['results']:

        # Exclude anything such as actors, filming locations, directors, tv episodes, unreleased etc..
        if (data.get("titleType") != None and data.get("year") != None and data["titleType"]!= "tvEpisode" and data["titleType"]!= "podcastEpisode"):
            
            # ID
            id = data['id'][7:-1]
            movies_dict[id] = {}

            # Title of movie
            title = data.get("title")
            movies_dict[id]['title'] = title

            # Year movie was released
            release_date = data.get("year")
            movies_dict[id]['year'] = release_date

            # Type of movie (Movie, TV, Mini, Short)
            movie_type = data.get("titleType")
            movies_dict[id]['type'] = movie_type

            # Poster/Image of the movie
            if (data.get('image') == None):
                movie_image_path = "/public/img/null_image.webp"
            else:
                movie_image_path = data['image']["url"]
            movies_dict[id]['img'] = movie_image_path

    return movies_dict

# Cleans the movie type string into a readable format
def format_movie_type_string(movie_type):
    if (movie_type == "movie"):
        movie_type = "Movie"
    elif (movie_type == "tvMovie"):
        movie_type = "TV Movie"
    elif (movie_type == "videoGame"):
        movie_type = "Video Game"
    elif (movie_type == "tvSeries"):
        movie_type = "TV Series"
    elif (movie_type == "tvMiniSeries"):
        movie_type = "TV Mini Series"
    elif (movie_type == "short"):
        movie_type = "Short"
    elif (movie_type == "video"):
        movie_type = "Video"
    elif (movie_type == "tvSpecial"):
        movie_type = "TV Special"
    elif (movie_type == "musicVideo"):
        movie_type = "Music Video"
    return movie_type
