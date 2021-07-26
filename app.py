from flask import Flask, request
from pyhtml import *
import src.config as config
from src.getMovie import *
from src.content import *
from src.constructMovieCards import *
#from src.contentAdvisory import *

app = Flask(__name__, static_url_path = '/public', static_folder = 'public')
app.config['SECRET_KEY'] = config.SESSION_KEY

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
        CARD_LIST = SEARCH_NOT_FOUND
    else:
        CARD_LIST = div(class_="movie-list-wrap")(
                        constructMovieCards(movie_list)
                    )

    # Constuct search page
    content = html(
        HTML_HEAD_TAG,
        SEARCH_HEADER,
        CARD_LIST
    )
    return str(content)

@app.route('/advisory/<movie_ID>')
def advisory(movie_ID):
    content = html(
        HTML_HEAD_TAG,
        SEARCH_HEADER,
        p(f'{movie_ID}')
    )
    return str(content)

if __name__ == "__main__":
    app.run(debug=True)