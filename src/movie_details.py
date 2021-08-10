from src.imdb_requests import *
from src.movie_cards import *
from src.content import *

# Returns information about the movie in HTML format and the raw data in a tuple
def get_movie_info(movie_ID, api_key):
    get_movie_details = get_movie_details_request(movie_ID, api_key)
    # Check for 400/500 Internal Server and Bad Connection Error
    if (get_movie_details == None or get_movie_details.status_code == 500 or get_movie_details.status_code == 400):
        return False
    else:
        info = get_movie_details.json()

        # Default values
        movie_image_path = "/public/img/null_image.png"
        movie_time_string = "No Time Available"
        certificate = "No Rating Certificate"
        movie_rating = "Not Yet Rated"
        movie_plot = "No Plot Available"

        for data in info:

            if (data == "title"):
                # Movie title, year and type
                # Data returned is guranteed as it has already returned in the search page
                movie_title = info[data]["title"]
                movie_year = info[data]["year"]
                movie_type = info[data]["titleType"]

                # Poster/Image of the movie
                if (info[data].get("image") != None):
                    movie_image_path = info[data]["image"]["url"]

                if (info[data].get("runningTimeInMinutes") != None):
                    movie_time_string = convert_to_hour_mins(info[data]["runningTimeInMinutes"])

            # Movie Rating Certification
            if (data == "certificates"):
                if (info[data]["US"][0].get("certificate") != None):
                    certificate = info[data]["US"][0]["certificate"]
                    if (certificate != "Unrated" and certificate != "Not Rated"):
                        certificate = format_movie_rating_string(certificate)
                    
                if (info[data]["US"][0].get("ratingReason") != None):
                    certificate = info[data]["US"][0]["ratingReason"]

            # Movie score rating out of ten
            if (data == "ratings"):
                if (info[data]["canRate"] == True and info[data].get("rating") != None):
                    movie_rating = f'{str(info[data]["rating"])} / 10'
            
            if (data == "plotOutline"):
                if (info[data].get("text") != None):
                    movie_plot = f'{info[data]["text"]}'

    return (construct_movie_details_card(movie_title, movie_year, movie_image_path, movie_rating, format_movie_type_string(movie_type), movie_time_string, certificate, movie_plot),
    movie_title,
    movie_year,
    movie_image_path
)

# Formats the movie rating string with certificate and reason
def format_movie_rating_string(certificate):
    if (certificate == "G" or certificate == "TV-G" or certificate == "TV-Y"):
        rating_reason = "all audiences"
    if (certificate == "GP"):
        rating_reason = "parental guidance suggested"
    elif (certificate == "TV-Y7" or certificate == "TV-Y7-FV"):
        rating_reason = "children 7 and above"
    elif (certificate == "PG" or certificate == "TV-PG" or certificate == "E10+"):
        rating_reason = "children 10 and above"
    elif (certificate == "PG-13" or certificate == "TV-14" or certificate == "TV-13" or certificate == "T"):
        rating_reason = "children 13 and above"
    elif (certificate == "TV-14"):
        rating_reason = "children 14 and above"
    elif (certificate == "TV-MA"):
        rating_reason = "mature audiences"
    elif (certificate == "R"):
        rating_reason = "ages under 17 not admitted without parent or guardian"
    elif (certificate == "NC-17" or certificate == "X"):
        rating_reason = "ages under 17 not admitted"
    elif (certificate == "M"):
        rating_reason = "ages 17 and older"
    elif (certificate == "E"):
        rating_reason = "everyone"
    elif (certificate == "AO"):
        rating_reason = "ages 18 and over"
    elif (certificate == "Approved"):
        rating_reason = "exhibition"
    else:
        return f'Rated {certificate}'
    return f'Rated {certificate} for {rating_reason}'

#
def convert_to_hour_mins(movie_total_mins):
    # Get hours with floor division
    hours = movie_total_mins // 60
    # Get additional minutes with modulus
    minutes = movie_total_mins % 60

    # Create time as a string
    if (hours == 1 and minutes == 0):
        movie_time_string = f'{hours} hour'
    elif (hours == 1 and minutes == 1):
        movie_time_string = f'{hours} hour {minutes} min'
    elif (hours > 1 and minutes == 1):
        movie_time_string = f'{hours} hours {minutes} min'
    elif (hours > 1 and minutes == 0):
        movie_time_string = f'{hours} hours'
    elif (hours == 0 and minutes == 1):
        movie_time_string = f'{minutes} min'
    elif (hours == 0 and minutes > 1):
        movie_time_string = f'{minutes} mins'
    else:
        movie_time_string = f'{hours} hours {minutes} mins'
    return movie_time_string