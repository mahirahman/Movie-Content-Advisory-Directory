from pyhtml import *
from flask import Flask, request, session
import src.config as config
from src.movie_cards import get_movie_dict
from src.movie_details import get_movie_info
from src.movie_advisory import (
    nudity_advisory, violence_advisory, profanity_advisory,
    alcohol_advisory, frightening_advisory,
    nudity_advisory_status, violence_advisory_status,
    profanity_advisory_status, alcohol_advisory_status,
    frightening_advisory_status, get_content_advisory_dict
)
from src.content import (
    construct_head, construct_landing_page_body,
    construct_search_header, construct_dark_mode_switch,
    construct_previous_searched_movies, construct_movie_cards,
    construct_advisory_text, construct_advisory,
    construct_search_not_found, construct_no_advisories
)

app = Flask(__name__, static_url_path='/public', static_folder='public')
app.config['SECRET_KEY'] = config.SESSION_KEY

# Landing Page
@app.route('/')
def main():
    content = html(lang="en")(
        construct_head(),
        body(
            construct_dark_mode_switch(),
            construct_landing_page_body(session),
            construct_previous_searched_movies(session)
        )
    )
    return str(content)

# Movies Page
@app.route('/movies', methods=["POST"])
def movies():
    movie = request.form['movie_title']
    movies_dict = get_movie_dict(movie, config.API_KEY)

    if not movies_dict or movies_dict == {}:
        PAGE_BODY = construct_search_not_found()
    else:
        PAGE_BODY = div(class_="movie-list-wrap")(
            construct_movie_cards(movies_dict)
        )

    content = html(lang="en")(
        construct_head(),
        body(
            construct_search_header(),
            construct_dark_mode_switch(),
            div(class_="scroll-container-header")(
                construct_previous_searched_movies(session)
            ),
            PAGE_BODY
        )
    )
    return str(content)

# Movie Advisory Page
@app.route('/advisory/<movie_ID>')
def advisory(movie_ID):
    (MOVIE_DETAILS, movie_title, movie_year, movie_img_path) = get_movie_info(movie_ID, config.API_KEY)

    if movie_ID not in session:
        session[movie_ID] = movie_img_path, movie_title, movie_year

    advisory_data = get_content_advisory_dict(movie_ID, config.API_KEY)
    
    if not advisory_data:
        PAGE_ADVISORY = construct_no_advisories(movie_ID)
    else:
        # Generate advisory card
        PAGE_ADVISORY = construct_advisory(
            construct_advisory_text(nudity_advisory(advisory_data)),
            construct_advisory_text(violence_advisory(advisory_data)),
            construct_advisory_text(profanity_advisory(advisory_data)),
            construct_advisory_text(alcohol_advisory(advisory_data)),
            construct_advisory_text(frightening_advisory(advisory_data)),
            nudity_advisory_status(advisory_data),
            violence_advisory_status(advisory_data),
            profanity_advisory_status(advisory_data),
            alcohol_advisory_status(advisory_data),
            frightening_advisory_status(advisory_data)
        )

    content = html(lang="en")(
        construct_head(),
        construct_dark_mode_switch(),
        construct_search_header(),
        div(class_="scroll-container-header")(
            construct_previous_searched_movies(session)
        ),
        MOVIE_DETAILS,
        PAGE_ADVISORY
    )
    return str(content)

if not config.PRODUCTION and __name__ == "__main__":
    app.run(debug=True)
