from src.imdb_requests import get_movies_dict_request
from src.constant import TITLE_TYPE

# Produces a dictionary of movies from API
# If the API produces an error it will return None
def get_movie_dict(movie_ID, api_key):
    get_all_movies = get_movies_dict_request(movie_ID, api_key)
    
    if get_all_movies is None or get_all_movies.status_code in (400, 500):
        return False
    
    info = get_all_movies.json()
    
    if 'results' not in info:
        return False
    
    movies_dict = {}
    for data in info['results']:
        title_type = data.get("titleType")
        release_year = data.get("year")

        # Exclude unwanted types and entries
        if title_type and release_year and title_type not in {"tvEpisode", "podcastEpisode"}:
            id = data['id'][7:-1]
            movie_image_path = data.get('image', {"url": "/public/img/null_image.webp"})["url"]

            movies_dict[id] = {
                'title': data.get("title"),
                'year': release_year,
                'type': title_type,
                'img': movie_image_path
            }

    return movies_dict

# Cleans the movie type string into a readable format
def format_movie_type_string(movie_type):
    return TITLE_TYPE.get(movie_type, movie_type)
