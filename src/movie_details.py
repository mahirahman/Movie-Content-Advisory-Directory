from src.imdb_requests import get_movie_details_request
from src.movie_cards import format_movie_type_string
from src.content import construct_movie_details_card
from src.constant import RATING_REASONS

# Returns information about the movie in HTML format and the raw data in a tuple
def get_movie_info(movie_ID, api_key):
    get_movie_details = get_movie_details_request(movie_ID, api_key)

    if get_movie_details is None or get_movie_details.status_code in (400, 500):
        return False

    info = get_movie_details.json()

    # Default values
    movie_image_path = "/public/img/null_image.webp"
    movie_time_string = "No Time Available"
    certificate = "No Rating Certificate"
    movie_rating = "Not Yet Rated"
    movie_plot = "No Plot Available"
    movie_title = ""
    movie_year = ""
    movie_type = ""

    if "title" in info:
        movie_data = info["title"]
        movie_title = movie_data["title"]
        movie_year = movie_data["year"]
        movie_type = movie_data["titleType"]

        if "image" in movie_data:
            movie_image_path = movie_data["image"]["url"]

        if "runningTimeInMinutes" in movie_data:
            movie_time_string = convert_to_hour_mins(movie_data["runningTimeInMinutes"])

    if "certificates" in info:
        us_certificates = info["certificates"].get("US", [])

        if us_certificates:
            certificate_data = us_certificates[0]
            certificate = certificate_data.get("certificate", certificate)
            if certificate != "Unrated" and certificate != "Not Rated":
                certificate = format_movie_rating_string(certificate)
            certificate_rating_reason = certificate_data.get("ratingReason", certificate)
            if certificate_rating_reason is not None:
                certificate = certificate_rating_reason

    if "ratings" in info:
        ratings_data = info["ratings"]
        if ratings_data.get("canRate", False) and "rating" in ratings_data:
            movie_rating = f'{ratings_data["rating"]} / 10'

    if "plotOutline" in info:
        plot_data = info["plotOutline"]
        movie_plot = plot_data.get("text", movie_plot)

    return (
        construct_movie_details_card(
            movie_title,
            movie_year,
            movie_image_path,
            movie_rating,
            format_movie_type_string(movie_type),
            movie_time_string,
            certificate,
            movie_plot,
        ),
        movie_title,
        movie_year,
        movie_image_path,
    )

def format_movie_rating_string(certificate):
    rating_reason = RATING_REASONS.get(certificate, None)
    if rating_reason is None:
        return f"Rated {certificate}"
    return f"Rated {certificate} for {rating_reason}"

# Converts the total minutes into hour(s) and minute(s) format
def convert_to_hour_mins(movie_total_mins):
    hours = movie_total_mins // 60
    minutes = movie_total_mins % 60

    if hours == 0 and minutes == 0:
        return "0 mins"

    time_parts = []
    if hours > 0:
        time_parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes > 0:
        time_parts.append(f"{minutes} {'min' if minutes == 1 else 'mins'}")
    return " ".join(time_parts)
