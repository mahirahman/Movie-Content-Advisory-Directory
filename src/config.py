import secrets

# Title of the web app
TITLE = "Movie Content Advisory Directory"

# API Key generated from https://rapidapi.com/apidojo/api/imdb8
API_KEY = "bb1ff967f9msh13ca72a9e4167fbp1cec94jsn0f000eed74db"

# Favicon file
FAVICON = "/public/fav/favicon.ico"

# Site logo
LOGO = "/public/img/logo.svg"

# 64 BYTE User secret
SESSION_KEY = secrets.token_urlsafe(64)

# Set value to boolean to enable debug mode when running
DEBUG = False
