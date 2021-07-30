from flask import Flask, request
from pyhtml import *
from requests import api
import src.config as config
from src.imdb_requests import *
from src.content import *
from src.movie_cards import *
from src.movie_details import *

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
    

    content = html(
        HTML_HEAD_TAG,
        SEARCH_HEADER,
        get_movie_info(movie_ID, config.API_KEY)
    )
    return str(content)

if __name__ == "__main__":
    app.run(debug=True)