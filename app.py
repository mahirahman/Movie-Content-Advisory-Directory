from flask import Flask, request
from pyhtml import *
import src.config as config
from src.getMovie import *
from src.content import *
from src.constructMovieCard import *

app = Flask(__name__, static_url_path = '/public', static_folder = 'public')

@app.route('/')
def main():
    content = html(
        HTML_HEAD_TAG,
        LANDING_PAGE_BODY
    )
    return str(content)

@app.route('/movies', methods=["POST"])
def movies():

    movie = request.form['movie_title']
    movie_list = getMovieList(movie, config.API_KEY)

    # No movies found or not a valid search
    if (movie_list == False):
        content = html(
        HTML_HEAD_TAG,
        SEARCH_HEADER,
        SEARCH_NOT_FOUND
    )
        return str(content)
    else:
        # Constuct movie cards
        cards = "<div class=\"movie-list-wrap\">" + constructMovieCard(movie_list) + "<div>"
        content = html(
            HTML_HEAD_TAG,
            SEARCH_HEADER
        )
        return str(content) + cards

if __name__ == "__main__":
    app.run(debug=True)