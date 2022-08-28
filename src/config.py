from dotenv import load_dotenv
import secrets
import os

load_dotenv()

# Title of the web app
TITLE = "Movie Content Advisory Directory"

# URL of the website where is it being hosted on
URL = "https://movie-content-advisory.herokuapp.com"

# API Key generated from https://rapidapi.com/apidojo/api/imdb8
API_KEY = os.environ['API_KEY']

# Favicon file
FAVICON = "/public/fav/favicon.ico"

# Site logo
LOGO = "/public/img/logo.svg"

# 64 BYTE User secret
SESSION_KEY = secrets.token_urlsafe(64)

# Set to a boolean value to enable debug mode when running
DEBUG = True
