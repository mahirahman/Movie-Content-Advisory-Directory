from pyhtml import *
from flask import url_for
from src.config import TITLE, URL, FAVICON, LOGO
from src.movie_cards import format_movie_type_string

# Header Tag
def construct_head():
    return head(
        meta(charset="utf-8"),
        meta(name="twitter:card", content="summary"),
        title(TITLE),
        meta(property="og:title", content=TITLE),
        meta(property="og:site_name", content=TITLE),
        meta(property="og:url", content=URL),
        meta(property="og:image", content="/public/img/movies-page.png"),
        meta(name="viewport", content="width=device-width, initial-scale=1.0, shrink-to-fit=no"),
        meta(name="description", content="Search for content advisories for movies and TV shows."),
        meta(property="og:description", content="Search for content advisories for movies and TV shows."),
        meta(name="keywords", content="movie content advisory directory, movie content advisory, parental guide, parental guidance, content advisory, parental, movies, guidance, tv shows, advisory, ratings, clean, filter"),
        meta(name="author", content="Mahi Rahman"),
        meta(name="theme-color", content="#16181a"),
        link(rel="stylesheet", href="https://use.fontawesome.com/releases/v5.15.2/css/all.css"),
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap"),
        link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.9.0/mdb.min.css"),
        link(rel="stylesheet", href="/public/css/style.css"),
        link(rel="manifest", href="/public/manifest.json"),
        link(rel="icon", href= FAVICON),
        script(src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.9.0/mdb.min.js"),
        script(src="/public/js/error.js"),
        script(src="/public/js/events.js", type="module")
    )

# Main Page
def construct_landing_page_body(session):
    return div(
        img(src=LOGO, alt="MCAD Logo", class_ ="logo center selector filter"),
        br(),
        form(name="movie_input", action="/movies", class_="text-center", onsubmit="return validateForm()")(
            input_(type="text", name="movie_title", placeholder="Search", class_="searchbox", autocomplete="off"),
            button(type="Submit", value="Search", class_="btn btn-primary", aria_label="Search")(i(class_="fas fa-search")),
        ),
        br(),
        p(class_="center previous-searched")("Previous Searched Titles 🎬") if bool(session) else None
    )

# Header in Movies Page
def construct_search_header():
    return div(
        div(class_="header")(
            a(href="/")(img(src=LOGO, alt="MCAD Logo", class_ ="logo-header selector filter"),),
            form(name="movie_input", action="/movies", class_="form-header", onsubmit="return validateForm()")(
                input_(type="text", name="movie_title", placeholder="Search", class_="searchbox", autocomplete="off"),
                button(type="Submit", value="Search", class_="btn btn-primary", aria_label="Search")(i(class_="fas fa-search")),
            ),
        ),
    )

# No Movies Error Box
def construct_search_not_found():
    return div(class_="alert text-center")(
        p("Uh Oh - No Title Found 🤷")
    )

# No Advisories Available Error Box
def construct_no_advisories(movie_id):
    return div(class_="alert text-center")(
        p("Uh Oh - No Content Advisories Found 🤷")
    )
    
def construct_scroll_to_up():
    return div(class_="rounded p-2", id="scroll-to-top")(
        i(class_="fas fa-arrow-up")
    )

# Image container of previously searched movies
def construct_previous_searched_movies(session):
    img_cards = []
    for movie_id in session:
        img_cards.append(
            a(href=f'/advisory/{movie_id}')(
                div(id="img-exist", class_="d-inline-block overflow-hidden")(
                    img(class_="img-width selector", src=f'{session[movie_id][0]}', alt=f'{session[movie_id][1]} ({session[movie_id][2]})')
                )   
            )
        )
    return div(class_="scroll-container center")(img_cards)

# Appends the movies returned into a list that constructs the HTML cards
def construct_movie_cards(movie_list):
    movie_cards = []
    for movie_id in movie_list:
        movie_cards.append(
            div(class_="card movies-card")(
                a(href=url_for('advisory', movie_ID=movie_id))(
                    img(src=f"{movie_list[movie_id]['img']}", class_="card-img selector", alt=f"{movie_list[movie_id]['title']} ({movie_list[movie_id]['year']})"),
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
        img(src=title_img, class_="card-img selector img-details", alt=f'{title} ({year})'),
        div(class_="card-body p-2")(
            h5(class_="card-title")(title),
            h5(class_="card-title")(f'({year})'),
            p(class_="m-0")(f'{rating}')
        ),
        div(class_="list-group list-group-flush")(
            h5(class_="list-group-item")(f'{type} - {running_time}'),
            h5(class_="list-group-item")(certificate),
            h5(class_="list-group-item")(plot)
        )
    )

# Generates the advisory text into a list
def construct_advisory_text(html_list):
    return [p(class_="card-text")(text) for text in html_list] if html_list is not None else None

# Creates the advisory HTML card
def construct_advisory(html_nudity_list, html_violence_list, html_profanity_list, html_alcohol_list, html_frightening_list,
                        nudity_status, violence_status, profanity_status, alcohol_status, frightening_status):
    advisory_sections = [
        (
            "Sex & Nudity",
            nudity_status,
            html_nudity_list
        ),
        (
            "Violence & Gore",
            violence_status,
            html_violence_list
        ),
        (
            "Profanity",
            profanity_status,
            html_profanity_list
        ),
        (
            "Alcohol, Drugs & Smoking",
            alcohol_status,
            html_alcohol_list
        ),
        (
            "Frightening & Intense Scenes",
            frightening_status,
            html_frightening_list
        )
    ]
    
    advisory_cards = []

    for title, status, html_list in advisory_sections:
        advisory_cards.append(
            (
                div(class_="d-flex justify-content-center mt-3")(
                    h5(class_="card-title")(title),
                    h5(class_=f'align-self-center mx-2 text-uppercase status-box {status}')(status)
                ),
                div(class_="card-body align-self-center p-2 card-advisory rounded")(html_list)
            )
        )
    
    return div(class_="card text-center w-auto mt-4 mx-2")(advisory_cards)
