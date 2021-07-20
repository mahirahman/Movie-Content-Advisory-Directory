from flask import Flask, request
from pyhtml import *
import requests
import src.config as config

app = Flask(__name__, static_url_path = '/public', static_folder = 'public')
app_title = "Movie Content Advisory Directory"
@app.route('/')
def main():
    content = html(
        head(
            title(app_title),
            link(rel="stylesheet", href="public/css/style.css"),
            link(rel="icon", href="public/fav/favicon.ico")
        ),
        body(
            p("Movie Content Advisory Directory"),
            form(action="movies")(
                label("Search"),
                input_(type="text", name="movie_title"),
                input_(type="Submit", value="Search")
            )
        )
    )
    return str(content)

@app.route('/movies', methods=["POST"])
def movies():

    print(request.form)

    name = request.form['movie_title']

    content = html(
        head(
            title(app_title)
        ),
        body(
            p(f"You searched for {name}"),
        )
    )
    return str(content)

if __name__ == "__main__":
    app.run(debug=True)