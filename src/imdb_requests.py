import requests

def request_headers(api_key):
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    return headers

# Find title by whatever you are familiar with, such as : name of title, album, song, etc…
def get_movie_list_request(movie_ID, api_key):

    # Find list of movies based on search
    url = "https://imdb8.p.rapidapi.com/title/find"
    querystring = {"q":movie_ID}
    get_all_movies = requests.request("GET", url, headers=request_headers(api_key), params=querystring)

    return get_all_movies

# Get overview information of the title
def get_movie_details_request(movie_ID, api_key):

    url = "https://imdb8.p.rapidapi.com/title/get-overview-details"
    querystring = {"tconst":movie_ID,"currentCountry":"US"}
    get_movie_details = requests.request("GET", url, headers=request_headers(api_key), params=querystring)

    return get_movie_details

# Get parent guide information for specific movie
def get_movie_advisory_request(movie_ID, api_key):

    url = "https://imdb8.p.rapidapi.com/title/get-parental-guide"
    querystring = {"tconst":movie_ID}
    get_advisory = requests.request("GET", url, headers=request_headers(api_key), params=querystring)

    return get_advisory