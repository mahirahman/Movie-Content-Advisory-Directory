from imdb_requests import *

# Returns advisory data for nudity otherwise returns None
def nudity_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "nudity"):
            nudity = {}
            if (key.get("items") != None):
                for key2 in key["items"]:
                    nudity[key2["text"]] = {}
                    nudity[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
            return nudity
    return None
    
# Gets the status level of nudity advisory
def nudity_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "nudity"):
            return key["severityVotes"]["status"]
    return None

# Returns advisory data for violence otherwise returns None
def violence_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "violence"):
            violence = {}
            if (key.get("items") != None):
                for key2 in key["items"]:
                    violence[key2["text"]] = {}
                    violence[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
            return violence
    return None

def violence_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "violence"):
            return key["severityVotes"]["status"]
    return None

# Returns advisory data for profanity otherwise returns None
def profanity_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "profanity"):
            profanity = {}
            if (key.get("items") != None):
                for key2 in key["items"]:
                    profanity[key2["text"]] = {}
                    profanity[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
            return profanity
    return None

def profanity_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "profanity"):
            return key["severityVotes"]["status"]
    return None

# Returns advisory data for drugs otherwise returns None
def alcohol_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "alcohol"):
            drugs = {}
            if (key.get("items") != None):
                for key2 in key["items"]:
                    drugs[key2["text"]] = {}
                    drugs[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
            return drugs
    return None

def alcohol_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "alcohol"):
            return key["severityVotes"]["status"]
    return None

# Returns advisory data for intense scenes otherwise returns None
def frightening_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "frightening"):
            frightening = {}
            if (key.get("items") != None):
                for key2 in key["items"]:
                    frightening[key2["text"]] = {}
                    frightening[key2["text"]]['isSpoiler'] = key2["isSpoiler"]
            return frightening
    return None

def frightening_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "frightening"):
            return key["severityVotes"]["status"]
    return None

###############################################################################################
# Returns all content advisory data in a dictionary
def get_content_advisory_dict(movie_ID, api_key):

    advisory_data = get_movie_advisory_request(movie_ID, api_key)
    # Check for 500 Internal Server Error
    if (advisory_data.status_code == 500):
        return False
    else:
        # Check if there is any information to display
        advisory_data = advisory_data.json()
        if (advisory_data["parentalguide"] == None):
            return False

        print(f'\n{nudity_advisory(advisory_data)}')
        print(f'{nudity_advisory_status(advisory_data)}\n')

        print(f'{violence_advisory(advisory_data)}')
        print(f'{violence_advisory_status(advisory_data)}\n')

        print(f'{profanity_advisory(advisory_data)}')
        print(f'{profanity_advisory_status(advisory_data)}\n')

        print(f'{alcohol_advisory(advisory_data)}')
        print(f'{alcohol_advisory_status(advisory_data)}\n')

        print(f'{frightening_advisory(advisory_data)}')
        print(f'{frightening_advisory_status(advisory_data)}\n')

        return True

assert(get_content_advisory_dict("tt0352416", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt12227440", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == False)
assert(get_content_advisory_dict("tt0816692", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt0286716", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt0099387", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt0206488", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == False) 
assert(get_content_advisory_dict("tt0800080", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt10857160", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == False) 
assert(get_content_advisory_dict("tt10872600", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == False) 
assert(get_content_advisory_dict("tt6320628", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt5807780", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt0145487", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt0948470", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt4633694", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt2930604", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 
assert(get_content_advisory_dict("tt3748528", "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db") == True) 