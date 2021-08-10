from src.imdb_requests import *

# Returns advisory data for nudity otherwise returns None
def nudity_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "nudity"):
            nudity = []
            if (key.get("items") != None):
                for key2 in key["items"]:
                    nudity.append(key2["text"])
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
            violence = []
            if (key.get("items") != None):
                for key2 in key["items"]:
                    violence.append(key2["text"])
            return violence
    return None

# Gets the status level of violence advisory
def violence_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "violence"):
            return key["severityVotes"]["status"]
    return None

# Returns advisory data for profanity otherwise returns None
def profanity_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "profanity"):
            profanity = []
            if (key.get("items") != None):
                for key2 in key["items"]:
                    profanity.append(key2["text"])
            return profanity
    return None

# Gets the status level of profanity advisory
def profanity_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "profanity"):
            return key["severityVotes"]["status"]
    return None

# Returns advisory data for drugs otherwise returns None
def alcohol_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "alcohol"):
            drugs = []
            if (key.get("items") != None):
                for key2 in key["items"]:
                    drugs.append(key2["text"])
            return drugs
    return None

# Gets the status level of alcohol advisory
def alcohol_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "alcohol"):
            return key["severityVotes"]["status"]
    return None

# Returns advisory data for intense scenes otherwise returns None
def frightening_advisory(data):
    for key in data['parentalguide']:
        if (key["label"] == "frightening"):
            frightening = []
            if (key.get("items") != None):
                for key2 in key["items"]:
                    frightening.append(key2["text"])
            return frightening
    return None

# Gets the status level of frightening advisory
def frightening_advisory_status(data):
    for key in data['parentalguide']:
        if (key["label"] == "frightening"):
            return key["severityVotes"]["status"]
    return None

# Returns all content advisory JSON data in a dictionary
def get_content_advisory_dict(movie_ID, api_key):
    advisory_data = get_movie_advisory_request(movie_ID, api_key)
    # Check for 400/500 Internal Server and Bad Connection Error
    if (advisory_data == None or advisory_data.status_code == 500 or advisory_data.status_code == 400):
        return False
    else:
        # Check if there is any information to display
        advisory_data = advisory_data.json()
        if (advisory_data["parentalguide"] == None):
            return False
    return advisory_data