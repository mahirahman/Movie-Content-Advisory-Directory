import requests

# Returns a dictionary of movies based on what user has searched
def getMovieList(movie, api_key):

    movie_list = {}

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    url = "https://imdb8.p.rapidapi.com/title/find"
    querystring = {"q":movie}
    get_allMovies = requests.request("GET", url, headers=headers, params=querystring)
    
    # Check for 500 Internal Server Error
    if (get_allMovies.status_code == 500):
        return False
    else:
        info = get_allMovies.json()
        # Check if there are any movies available from search
        if (get_allMovies.status_code == 200 and len(info) == 4):
            return False

    count = 0
    for data in info['results']:

        # Exclude anything such as actors, filming locations, directors, unreleased etc..
        if (info['results'][count].get("titleType") != None and info['results'][count].get("year") != None):

            # ID
            id = info['results'][count]['id'][7:-1]
            movie_list[id] = {}

            # Title of movie
            title = info['results'][count].get("title")
            movie_list[id]['title'] = title

            # Year movie was released
            release_date = info['results'][count].get("year")
            movie_list[id]['year'] = release_date

            # Type of movie (Movie, TV, Mini, Short)
            movie_type = info['results'][count].get("titleType")
            movie_list[id]['type'] = movie_type

            # Poster/Image of the movie
            if (info['results'][count].get('image') == None):
                movie_image_path = "/public/img/null_image.png"
            else:
                movie_image_path = info['results'][count]['image']["url"]
            movie_list[id]['img'] = movie_image_path

            #print(f"ID: {id}\nTitle: {title} ({release_date})\nType: {movie_type}\n{movie_image_path}\n")
        count += 1
    return movie_list