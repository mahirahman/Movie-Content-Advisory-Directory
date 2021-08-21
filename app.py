from flask import Flask, request, session
from pyhtml import *
import src.config as config
from src.content import *
from src.movie_cards import *
from src.movie_details import *
from src.movie_advisory import *

app = Flask(__name__, static_url_path = '/public', static_folder = 'public')
app.config['SECRET_KEY'] = config.SESSION_KEY

# Landing Page
@app.route('/')
def main():
    content = html(lang="en")(
        HTML_HEAD_TAG,
        body(
            DARK_MODE_SWITCH,
            LANDING_PAGE_BODY,
            previous_searched_movies(session)
        )
    )

    return str(content)

# Movies Page
@app.route('/movies', methods=["POST"])
def movies():
    # String passed from landing page input
    movie = request.form['movie_title']

    # Dictionary of movies based on input
    movies_dict = get_movie_dict(movie, config.API_KEY)

    # No movies found or not a valid search
    if (movies_dict == False or movies_dict == {}):
        PAGE_BODY = SEARCH_NOT_FOUND
    else:
        # Generate the movie cards
        PAGE_BODY = div(class_="movie-list-wrap")(
                        construct_movie_cards(movies_dict)
                    )

    # Constuct search page
    content = html(lang="en")(
        HTML_HEAD_TAG,
        body(
            SEARCH_HEADER,
            DARK_MODE_SWITCH,
            div(class_="scroll-container-header")(
                previous_searched_movies(session)
            ),
            PAGE_BODY
        )
    )
    return str(content)

# Movie Advisory Page
@app.route('/advisory/<movie_ID>')
def advisory(movie_ID):
    (MOVIE_DETAILS, movie_title, movie_year, movie_img_path) = get_movie_info(movie_ID, config.API_KEY)
    # Add movie_ID and movie poster to session dictionary
    if movie_ID not in session:
        session[movie_ID] = movie_img_path, movie_title, movie_year

    advisory_data = get_content_advisory_dict(movie_ID, API_KEY)
    if (advisory_data == False):
        PAGE_ADVISORY = no_advisories(movie_ID)
    else:
        # Get the advisory string texts in an array
        nudity_list = nudity_advisory(advisory_data)
        violence_list = violence_advisory(advisory_data)
        profanity_list = profanity_advisory(advisory_data)
        alcohol_list = alcohol_advisory(advisory_data)
        frightening_list = frightening_advisory(advisory_data)

        # Get the advisory status of each
        nudity_status = nudity_advisory_status(advisory_data)
        violence_status = violence_advisory_status(advisory_data)
        profanity_status = profanity_advisory_status(advisory_data)
        alcohol_status = alcohol_advisory_status(advisory_data)
        frightening_status = frightening_advisory_status(advisory_data)

        # Get the HTML texts in an array
        html_nudity_list = construct_advisory_text(nudity_list)
        html_violence_list = construct_advisory_text(violence_list) 
        html_profanity_list = construct_advisory_text(profanity_list)
        html_alcohol_list = construct_advisory_text(alcohol_list)
        html_frightening_list = construct_advisory_text(frightening_list)

        # Generate advisory card
        PAGE_ADVISORY = construct_advisory(html_nudity_list, html_violence_list, html_profanity_list, html_alcohol_list, html_frightening_list, 
                                            nudity_status, violence_status, profanity_status, alcohol_status, frightening_status)

    content = html(lang="en")(
        HTML_HEAD_TAG,
        DARK_MODE_SWITCH,
        SEARCH_HEADER,
        div(class_="scroll-container-header")(
            previous_searched_movies(session)
        ),
        MOVIE_DETAILS,
        PAGE_ADVISORY
    )
    return str(content)

if __name__ == "__main__":
    if (DEBUG):
        app.run(debug=True)
    else:
        app.run(debug=False)