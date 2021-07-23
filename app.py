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
            form(action="movies", class_="form-landing")(
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

    cards_str = ""
    for id in movie_list:
        movie_img = movie_list[id]['img']
        movie_name = movie_list[id]['title']
        movie_year = movie_list[id]['year']
        movie_type = movie_list[id]['type']

        list_of_cards = div(class_="card", style="width: 11rem;margin: 10px;text-align: center;")(
                a(href="http://google.com")(
                    img(src=f"{movie_img}", class_="card-img-top", alt=f"{movie_name} ({movie_year})"),
                    div(class_="card-body")(
                        h5(class_="card-title")(
                            f"{movie_name}"
                        ),
                        p(f"{movie_type} - 9.5/10")
                    )
                )
        )
        cards_str = cards_str + str(list_of_cards)

    #Concatenate flex wrap div to start and end of list of cards
    cards_str = "<div class=\"movie-list-wrap\">" + cards_str + "<div>"

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
            div(class_="header-flex")(
                a(href="/")(
                    img(src=config.LOGO, alt="MCAD Logo", class_ ="logo-header selector"),
                ),
                form(action="movies", class_="form-header")(
                    input_(type="text", name="movie_title", placeholder="Search", class_="searchbox"),
                    button(type="Submit", value="Search", class_="btn btn-primary")(
                        i(class_="fas fa-search")
                    ),
                )
            ),
            br(),
        )
    )
    return str(content) + cards_str

if __name__ == "__main__":
    app.run(debug=True)