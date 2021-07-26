import requests

# Returns JSON data from parental guide of the movie_ID
#def getParentalGuideJSON(movie_ID, api_key):
def getParentalGuideJSON(movie_ID, api_key):  

    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

    url = "https://imdb8.p.rapidapi.com/title/get-parental-guide"
    querystring = {"tconst":movie_ID}

    get_advisory = requests.request("GET", url, headers=headers, params=querystring)
    info = get_advisory.json()

    return info

# Returns advisory data for nudity otherwise returns None
def nudity_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "nudity"):
            nudity = {}
            for key2 in key["items"]:
                nudity[key2["text"]] = {}
                nudity[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
                nudity[key2["text"]]['status'] = key["severityVotes"]["status"]
            return nudity
    return None

# Returns advisory data for violence otherwise returns None
def violence_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "violence"):
            violence = {}
            for key2 in key["items"]:
                violence[key2["text"]] = {}
                violence[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
                violence[key2["text"]]['status'] = key["severityVotes"]["status"]
            return violence
    return None

# Returns advisory data for profanity otherwise returns None
def profanity_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "profanity"):
            profanity = {}
            for key2 in key["items"]:
                profanity[key2["text"]] = {}
                profanity[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
                profanity[key2["text"]]['status'] = key["severityVotes"]["status"]
            return profanity
    return None

# Returns advisory data for drugs otherwise returns None
def drugs_advisory(data):
    drugs = {}
    return drugs

# Returns advisory data for intense scenes otherwise returns None
def frightening_advisory(data):
    intense = {}
    return intense


###############################################################################################
# Returns all content advisory data in a dictionary
def contentAdvisoryDict(movie_ID):

    advisory_data = getParentalGuideJSON(movie_ID, "ENTER API KEY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if (advisory_data == None):
        return None
    else:
        # Sex & Nudity
        print(nudity_advisory(advisory_data))
        # Violence & Gore
        print(violence_advisory(advisory_data))
        # Profanity
        print(profanity_advisory(advisory_data))
        # Alcohol, Drugs & Smoking
        #drugs_advisory(advisory_data)
        # Frightening & Intense Scenes
        #frightening_advisory(advisory_data)

contentAdvisoryDict("tt0099387")