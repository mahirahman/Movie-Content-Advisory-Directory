from src.config import *
from pyhtml import *

# Header Tag
HTML_HEAD_TAG = head(
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
            title(TITLE),
            link(rel="stylesheet", href="https://use.fontawesome.com/releases/v5.15.2/css/all.css"),
            link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap"),
            link(rel="stylesheet", href="/public/css/mdb.min.css"),
            link(rel="stylesheet", href="/public/css/style.css"),
            link(rel="icon", href= FAVICON),
            script(src="/public/js/mdb.min.js"),
            script(src="/public/js/script.js")
        )

# Main Page
LANDING_PAGE_BODY = body(
                        img(src=LOGO, alt="MCAD Logo", class_ ="logo center selector"),
                        br(),
                        form(name="movie_input", action="/movies", class_="form-landing", onsubmit="return validateForm()")(
                            input_(type="text", name="movie_title", placeholder="Search", class_="searchbox"),
                            button(type="Submit", value="Search", class_="btn btn-primary")(
                                i(class_="fas fa-search")
                            ),
                        )
                    )

# Header in Movies Page
SEARCH_HEADER = body(
                    div(class_="header-flex")(
                        a(href="/")(
                            img(src=LOGO, alt="MCAD Logo", class_ ="logo-header selector"),
                        ),
                        form(name="movie_input", action="/movies", class_="form-header", onsubmit="return validateForm()")(
                            input_(type="text", name="movie_title", placeholder="Search", class_="searchbox"),
                            button(type="Submit", value="Search", class_="btn btn-primary")(
                                i(class_="fas fa-search")
                            ),
                        )
                    ),
                )

# No Movies Error Box
SEARCH_NOT_FOUND = div(class_="alert")(
                    p("Uh Oh - No Title Found 🤷")
                )

# No Advisory Error Box


