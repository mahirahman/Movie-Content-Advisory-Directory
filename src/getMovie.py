import requests

# Returns a dictionary of movies and information based on what user has searched
def getMovieList(movie_ID, api_key):

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    # Find list of movies based on search
    url = "https://imdb8.p.rapidapi.com/title/find"
    querystring = {"q":movie_ID}
    get_allMovies = requests.request("GET", url, headers=headers, params=querystring)
    
    # Check for 500 Internal Server Error
    if (get_allMovies.status_code == 500):
        return False
    else:
        info = get_allMovies.json()
        # Check if there are any movies available from search
        if (get_allMovies.status_code == 200 and len(info) == 4):
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

            rating = None
            movie_list[id]['rating'] = rating

            #print(f"ID: {id}\nTitle: {title} ({release_date})\nType: {movie_type}\n{movie_image_path}\n")
    return movie_list