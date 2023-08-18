import requests

def request_headers(api_key):
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    return headers

def make_request(url, querystring, api_key):
    try:
        response = requests.get(url, headers=request_headers(api_key), params=querystring)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
# Find title by whatever you are familiar with, such as: name of title, album, song, etc…
def get_movies_dict_request(movie_ID, api_key):
    url = "https://imdb8.p.rapidapi.com/title/find"
    querystring = {"q": movie_ID}
    return make_request(url, querystring, api_key)

# Get overview information of the title
def get_movie_details_request(movie_ID, api_key):
    url = "https://imdb8.p.rapidapi.com/title/get-overview-details"
    querystring = {"tconst": movie_ID, "currentCountry": "US"}
    return make_request(url, querystring, api_key)

# Get parent guide information for specific movie
def get_movie_advisory_request(movie_ID, api_key):
    url = "https://imdb8.p.rapidapi.com/title/get-parental-guide"
    querystring = {"tconst": movie_ID}
    return make_request(url, querystring, api_key)
