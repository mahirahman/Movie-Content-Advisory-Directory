from pyhtml import *
from flask import url_for
from src.config import *
from src.movie_cards import *

# Header Tag
HTML_HEAD_TAG = head(
            meta(charset="utf-8"),
            meta(name="twitter:card", content="summary"),
            title(TITLE),
            meta(property="og:title", content=TITLE),
            meta(property="og:site_name", content=TITLE),
            meta(property="og:url", content=URL),
            meta(property="og:image", content="/public/img/screenshot.png"),
            meta(name="viewport", content="width=device-width, initial-scale=1.0, shrink-to-fit=no"),
            meta(name="description", content="Search for content advisories for movies and TV shows."),
            meta(property="og:description", content="Search for content advisories for movies and TV shows."),
            meta(name="keywords", content="movie content advisory directory, movie content advisory, parental guide, parental guidance, content advisory, parental, movies, guidance, tv shows, advisory, ratings, clean, filter"),
            meta(name="author", content="Mahi Rahman"),
            link(rel="stylesheet", href="https://use.fontawesome.com/releases/v5.15.2/css/all.css"),
            link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap"),
            link(rel="stylesheet", href="/public/css/mdb.min.css"),
            link(rel="stylesheet", href="/public/css/style.css"),
            link(rel="stylesheet", href="/public/css/style-dark.css"),
            link(rel="icon", href= FAVICON),
            script(src="/public/js/mdb.min.js"),
            script(src="/public/js/error.js"),
            script(src="/public/js/darkmode.js"),
        )

# Main Page
LANDING_PAGE_BODY = div(
                        img(src=LOGO, alt="MCAD Logo", class_ ="logo center selector filter"),
                        br(),
                        form(name="movie_input", action="/movies", class_="form-landing", onsubmit="return validateForm()")(
                            input_(type="text", name="movie_title", placeholder="Search", class_="searchbox", autocomplete="off"),
                            button(type="Submit", value="Search", class_="btn btn-primary")(
                                i(class_="fas fa-search")
                            ),
                        ),
                        br(),
                        p(class_="center previous-searched")(
                            "Previous Searched Titles 🎬"
                        )
                    )

# Header in Movies Page
SEARCH_HEADER = div(
                    div(class_="header-flex")(
                        a(href="/")(
                            img(src=LOGO, alt="MCAD Logo", class_ ="logo-header selector filter"),
                        ),
                        form(name="movie_input", action="/movies", class_="form-header", onsubmit="return validateForm()")(
                            input_(type="text", name="movie_title", placeholder="Search", class_="searchbox", autocomplete="off"),
                            button(type="Submit", value="Search", class_="btn btn-primary")(
                                i(class_="fas fa-search")
                            ),
                        ),
                    ),
                )

# Dark/Light Mode Toggle Button
DARK_MODE_SWITCH = button(class_="btn-toggle btn-darkmode light-mode-button")(
                    span(),
                    span()
                )

# No Movies Error Box
SEARCH_NOT_FOUND = div(class_="alert")(
                    p(class_="alert-text")(
                        "Uh Oh - No Title Found 🤷"
                    )
                )

# No Advisories Available Error Box
def no_advisories(movie_ID):
    return div(class_="alert")(
            p(class_="alert-text")(
                "Uh Oh - No Content Advisories Found 🤷"  
            ),
            a(href=f'https://www.imdb.com/registration/signin?u=https%3A%2F%2Fwww.imdb.com%2Ftitle%2F{movie_ID}%2Fparentalguide', class_="alert-text", target="_blank")(
                "Be the first to evaluate this"
            )
    )

# Image container of previously searched movies
def previous_searched_movies(session):
    # Wraps the list of img into a x-scrollable container
    return div(class_="scroll-container center")(
            movie_history_img(session)
        )

# Appends the movie that was clicked into a list that constructs the HTML image
def movie_history_img(session):
    img_cards = []
    for movie_id in session:
        img_cards.append(
            a(href=f'/advisory/{movie_id}')(
                div(id="img-exist", class_="img-block")(
                    img(class_="img-width selector", src=f'{session[movie_id][0]}', alt=f'{session[movie_id][1]} ({session[movie_id][2]})')
                )   
            )
        )
    return img_cards

# Appends the movies returned into a list that constructs the HTML cards
# for the amount of movies in movie list
def construct_movie_cards(movie_list):
    movie_cards = []
    for movie_id in movie_list:
        movie_cards.append(
            div(class_="card")(
                a(href=url_for('advisory', movie_ID=movie_id))(
                    img(src=f"{movie_list[movie_id]['img']}", class_="card-img-top selector", alt=f"{movie_list[movie_id]['title']} ({movie_list[movie_id]['year']})"),
                    div(class_="card-body")(
                        h5(class_="card-title search-title")(
                            f"{movie_list[movie_id]['title']}"
                        ),
                        h5(class_="search-title")(
                            f"({movie_list[movie_id]['year']})"
                        ),
                        p(f"{format_movie_type_string(movie_list[movie_id]['type']) }")
                    )
                )
            ))
    return movie_cards

# Generates Movie Details Card
def construct_movie_details_card(title, year, title_img, rating, type, running_time, certificate, plot):
    return div(class_="card card-details")(
                        img(src=title_img, class_="card-img-top selector img-details", alt=f'{title} ({year})'),
                        div(class_="card-body card-body-details")(
                            h5(class_="card-title")(
                                title
                            ),
                            h5(class_="card-title")(
                                f'({year})'
                            ),
                            p(class_="card-subtext")(
                                f'{rating}'
                            )
                        ),
                        div(class_="list-group list-group-flush")(
                            h5(class_="list-group-item")(
                                f'{type} - {running_time}'
                            ),
                            h5(class_="list-group-item")(
                                certificate
                            ),
                            h5(class_="list-group-item")(
                                plot
                            )
                        )
                    )

# Generates the advisory text into a list
def construct_advisory_text(html_list):
    if (html_list == None):
        return None
    html_advisory_list = []
    for text in html_list:
        html_advisory_list.append(p(class_="card-text")(text))
    return html_advisory_list

# Creates the advisory HTML card
def construct_advisory(html_nudity_list, html_violence_list, html_profanity_list, html_alcohol_list, html_frightening_list, 
                        nudity_status, violence_status, profanity_status, alcohol_status, frightening_status):
    return  div(class_="card text-center advisory-box")(
                div(class_="container")(
                    h5(class_="card-title round-edges-top-only")(
                        "Sex & Nudity"
                    ),
                    h5(class_=f'status-box {nudity_status}')(
                        nudity_status
                    )
                ),
                div(class_="card-body card-advisory round-edges")(
                        html_nudity_list
                ),
                div(class_="container")(
                    h5(class_="card-title round-edges-top-only")(
                        "Violence & Gore"
                    ),
                    h5(class_=f'status-box {violence_status}')(
                        violence_status
                    )
                ),
                div(class_="card-body card-advisory round-edges")(
                        html_violence_list
                ),
                div(class_="container")(
                    h5(class_="card-title round-edges-top-only")(
                        "Profanity"
                    ),
                    h5(class_=f'status-box {profanity_status}')(
                        profanity_status
                    )
                ),
                div(class_="card-body card-advisory round-edges")(
                        html_profanity_list
                )
                ,
                div(class_="container")(
                    h5(class_="card-title round-edges-top-only")(
                        "Alcohol, Drugs & Smoking"
                    ),
                    h5(class_=f'status-box {alcohol_status}')(
                        alcohol_status
                    )
                ),
                div(class_="card-body card-advisory round-edges")(
                        html_alcohol_list
                )
                ,
                div(class_="container")(
                    h5(class_="card-title round-edges-top-only")(
                        "Frightening & Intense Scenes"
                    ),
                    h5(class_=f'status-box {frightening_status}')(
                        frightening_status
                    )
                ),
                div(class_="card-body card-advisory round-edges")(
                        html_frightening_list
                )
        )