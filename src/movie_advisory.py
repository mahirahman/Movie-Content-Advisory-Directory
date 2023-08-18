from src.imdb_requests import get_movie_advisory_request

def get_advisory_data(data, label):
    for key in data['parentalguide']:
        if key["label"] == label:
            advisory_list = []
            if key.get("items"):
                advisory_list = [item["text"] for item in key["items"]]
            return advisory_list if advisory_list else None
    return None

def get_advisory_status(data, label):
    for key in data['parentalguide']:
        if key["label"] == label:
            return key["severityVotes"]["status"]
    return None

def get_content_advisory_dict(movie_ID, api_key):
    advisory_data = get_movie_advisory_request(movie_ID, api_key)
    
    if advisory_data is None or advisory_data.status_code in [400, 500]:
        return False
    
    advisory_data = advisory_data.json()
    if advisory_data.get("parentalguide") is None:
        return False
    
    return advisory_data

def nudity_advisory(data):
    return get_advisory_data(data, "nudity")

def nudity_advisory_status(data):
    return get_advisory_status(data, "nudity")

def violence_advisory(data):
    return get_advisory_data(data, "violence")

def violence_advisory_status(data):
    return get_advisory_status(data, "violence")

def profanity_advisory(data):
    return get_advisory_data(data, "profanity")

def profanity_advisory_status(data):
    return get_advisory_status(data, "profanity")

def alcohol_advisory(data):
    return get_advisory_data(data, "alcohol")

def alcohol_advisory_status(data):
    return get_advisory_status(data, "alcohol")

def frightening_advisory(data):
    return get_advisory_data(data, "frightening")

def frightening_advisory_status(data):
    return get_advisory_status(data, "frightening")
