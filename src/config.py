from pyhtml import *

# Title of the web app
TITLE = "Movie Content Advisory Directory"

# API Key can be generated from https://rapidapi.com/apidojo/api/imdb8
API_KEY = "Enter API Key"

# Favicon file
FAVICON = "public/fav/favicon.ico"

# Site logo
LOGO = "/public/img/logo.svg"

# Header Tag
HTML_HEADER_TAG = head (
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
            title(TITLE),
            link(rel="stylesheet", href="https://use.fontawesome.com/releases/v5.15.2/css/all.css"),
            link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap"),
            link(rel="stylesheet", href="public/css/mdb.min.css"),
            link(rel="stylesheet", href="public/css/style.css"),
            link(rel="icon", href= FAVICON),
            script(src="public/js/mdb.min.js")
        )
