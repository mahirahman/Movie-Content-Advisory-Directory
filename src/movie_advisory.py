from src.imdb_requests import *
from pyhtml import *

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
    return advisory_data

def construct_advisory_text(html_list):
    if (html_list == None):
        return None
    html_advisory_list = []
    for text in html_list:
        html_advisory_list.append(p(class_="card-text")(text))
    return html_advisory_list


def construct_advisory(html_nudity_list, html_violence_list, html_profanity_list, html_alcohol_list, html_frightening_list, 
                        nudity_status, violence_status, profanity_status, alcohol_status, frightening_status):
    return  div (class_="card text-center advisory-box")(
            div(class_="container")(
                h5(class_="card-title round-edges-top-only")(
                    "Sex & Nudity"
                ),
                h5(class_=f'status-box {nudity_status}')(
                    nudity_status
                )
            ),
            div(class_="card-body card-advisory round-edges")(
                    html_nudity_list
            ),
            div(class_="container")(
                h5(class_="card-title round-edges-top-only")(
                    "Violence & Gore"
                ),
                h5(class_=f'status-box {violence_status}')(
                    violence_status
                )
            ),
            div(class_="card-body card-advisory round-edges")(
                    html_violence_list
            ),
            div(class_="container")(
                h5(class_="card-title round-edges-top-only")(
                    "Profanity"
                ),
                h5(class_=f'status-box {profanity_status}')(
                    profanity_status
                )
            ),
            div(class_="card-body card-advisory round-edges")(
                    html_profanity_list
            )
            ,
            div(class_="container")(
                h5(class_="card-title round-edges-top-only")(
                    "Alcohol, Drugs & Smoking"
                ),
                h5(class_=f'status-box {alcohol_status}')(
                    alcohol_status
                )
            ),
            div(class_="card-body card-advisory round-edges")(
                    html_alcohol_list
            )
            ,
            div(class_="container")(
                h5(class_="card-title round-edges-top-only")(
                    "Frightening & Intense Scenes"
                ),
                h5(class_=f'status-box {frightening_status}')(
                    frightening_status
                )
            ),
            div(class_="card-body card-advisory round-edges")(
                    html_frightening_list
            )
        )