import requests
import src.config as config

headers = {
    'x-rapidapi-key': config.API_KEY,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

####################################################################################################################################
# Get list of movies based on what user searches

movie = input("What is the movie you are looking for? ")

url = "https://imdb8.p.rapidapi.com/title/find"
querystring = {"q":movie}
get_allMovies = requests.request("GET", url, headers=headers, params=querystring)
info = get_allMovies.json()

count = 0
for data in info['results']:

    # Exclude anything such as actors, filming locations, directors etc..
    if (info['results'][count].get("titleType") != None):

        # ID
        id = info['results'][count]['id'][7:-1]

        # Title of movie
        title = info['results'][count].get("title")

        # Year movie was released
        if (info['results'][count].get("year") == None):
            release_date = "Unreleased"
        else: 
            release_date = info['results'][count].get("year")

        # Type of movie (Movie, TV, Mini, Short)
        movie_type = info['results'][count].get("titleType")

        # Poster/Image of the movie
        if (info['results'][count].get('image') == None):
            movie_image_path = config.NULL_POSTER
        else:
            movie_image_path = info['results'][count]['image']["url"]            

        print(f"ID: {id}\nTitle: {title} ({release_date})\nType: {movie_type}\n{movie_image_path}\n")
    count += 1
####################################################################################################################################
def nudity_advisory_status(info):
    return info['parentalguide'][0]['severityVotes']['status']
####################################################################################################################################
def violence_advisory_status(info):
    return info['parentalguide'][1]['severityVotes']['status']
####################################################################################################################################
# Get advisory information of the movie user has picked
def nudity_advisory(info):
    severity = nudity_advisory_status(info)
    print(severity)

    # Get all content advisory for nudity and insert it into a list
    nudity_list = []
    count = 0
    for item in info['parentalguide'][0]['items']:
        if (info['parentalguide'][0]['items'][count]['isSpoiler'] == False):
            nudity_list.append(info['parentalguide'][0]['items'][count]['text'])
        count += 1

    return nudity_list

####################################################################################################################################
# Get advisory information of the movie user has picked
def violence_advisory(info):
    severity = violence_advisory_status(info)
    print(severity)

    # Get all content advisory for violence and insert it into a list
    violence_list = []
    count = 0
    for item in info['parentalguide'][1]['items']:
        if (info['parentalguide'][1]['items'][count]['isSpoiler'] == False):
            violence_list.append(info['parentalguide'][1]['items'][count]['text'])
        count += 1

    return violence_list

####################################################################################################################################
url = "https://imdb8.p.rapidapi.com/title/get-parental-guide"

# !!!!!!!!!!!!! Hard Coded with Interstellar (2014) !!!!!!!!!!!!!!!!!!
querystring = {"tconst":"tt0816692"}
# !!!!!!!!!!!!! Hard Coded with Interstellar (2014) !!!!!!!!!!!!!!!!!!
# Final product will have user able to select movie which will return
# movie id and send it as parameter for querystring

get_advisory = requests.request("GET", url, headers=headers, params=querystring)
info = get_advisory.json()

if (info['parentalguide'] == None):
    print("Return false, no parental guide")
else:
    print("Sex & Nudity: ")
    print(nudity_advisory(info))
    
    print("Violence & Gore: ")
    print(violence_advisory(info))

    print("Profanity: ")
    #profanity_advisory(info)

    print("Alcohol, Drugs & Smoking: ")
    #drugs_advisory(info)

    print("Frightening & Intense Scenes: ")
    #frightening_advisory(info)

####################################################################################################################################