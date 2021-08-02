from flask import Flask, request
from pyhtml import *
from requests import api
import src.config as config
from src.imdb_requests import *
from src.content import *
from src.movie_cards import *
from src.movie_details import *
from src.movie_advisory import *

app = Flask(__name__, static_url_path = '/public', static_folder = 'public')
app.config['SECRET_KEY'] = config.SESSION_KEY

# Landing Page
@app.route('/')
def main():
    content = html(
        HTML_HEAD_TAG,
        LANDING_PAGE_BODY
    )
    return str(content)

# Movies Page
@app.route('/movies', methods=["POST"])
def movies():

    movie = request.form['movie_title']
    movie_list = get_movie_list(movie, config.API_KEY)

    # No movies found or not a valid search
    if (movie_list == False):
        PAGE_BODY = SEARCH_NOT_FOUND
    else:
        # Generate the movie cards
        PAGE_BODY = div(class_="movie-list-wrap")(
                        construct_movie_cards(movie_list)
                    )

    # Constuct search page
    content = html(
        HTML_HEAD_TAG,
        SEARCH_HEADER,
        PAGE_BODY
    )
    return str(content)

# Movie Advisory Page
@app.route('/advisory/<movie_ID>')
def advisory(movie_ID):

    advisory_data = get_content_advisory_dict(movie_ID, API_KEY)
    if (advisory_data == False):
        PAGE_ADVISORY = div(class_="alert")(
                    p("Uh Oh - No Content Advisories Found 🤷"),
                    a(href=f'https://www.imdb.com/registration/signin?u=https%3A%2F%2Fwww.imdb.com%2Ftitle%2F{movie_ID}%2Fparentalguide', target="_blank")(
                        "Be the first to evaluate this"
                    )
                )
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

    content = html(
        HTML_HEAD_TAG,
        SEARCH_HEADER,
        get_movie_info(movie_ID, config.API_KEY),
        PAGE_ADVISORY
    )
    return str(content)

if __name__ == "__main__":
    app.run(debug=True)