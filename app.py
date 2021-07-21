from flask import Flask, request
from pyhtml import *
import src.config as config
from src.getMovie import *

app = Flask(__name__, static_url_path = '/public', static_folder = 'public')
app_title = config.TITLE

@app.route('/')
def main():
    main_page = html(
        head(
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
            title(app_title),
            link(rel="stylesheet", href="https://use.fontawesome.com/releases/v5.15.2/css/all.css"),
            link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap"),
            link(rel="stylesheet", href="public/css/mdb.min.css"),
            link(rel="stylesheet", href="public/css/style.css"),
            link(rel="icon", href= config.FAVICON),
            script(src="public/js/mdb.min.js")
        ),
        body(
            img(src=config.LOGO, alt="MCAD Logo", class_ ="logo center selector"),
            br(),
            form(action="movies")(
                input_(type="text", name="movie_title", placeholder="Search", class_="searchbox"),
                button(type="Submit", value="Search", class_="btn btn-primary")(
                    i(class_="fas fa-search")
                ),
            )

        )
    )
    return str(main_page)

@app.route('/movies', methods=["POST"])
def movies():

    movie = request.form['movie_title']
    movie_list = getMovieList(movie, config.API_KEY)
    
    content = html(
        head(
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
            title(app_title),
            link(rel="stylesheet", href="https://use.fontawesome.com/releases/v5.15.2/css/all.css"),
            link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap"),
            link(rel="stylesheet", href="public/css/mdb.min.css"),
            link(rel="stylesheet", href="public/css/style.css"),
            link(rel="icon", href= config.FAVICON),
            script(src="public/js/mdb.min.js")
        ),
        body(
            p(f"You searched for {movie_list}"),
        )
    )
    return str(content)

if __name__ == "__main__":
    app.run(debug=True)