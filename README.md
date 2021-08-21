# Movie-Content-Advisory-Directory 🎬

![Image](/public/img/logo.svg)

Modern and mobile friendly web application that allows users to search for content advisories for movies and TV shows. 🍿

Live Deployment: [movie-content-advisory.herokuapp.com](https://movie-content-advisory.herokuapp.com)

[![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See below for prerequisite libraries and notes on how to deploy the project on a live system.

`git clone https://github.com/mahirahman/Movie-Content-Advisory-Directory`

To run the application locally:

1. CD to the directory of the project
2. Install the requirements by using the command `pip install -r requirements.txt`
3. Head over to [RapidAPI's IMDb API](https://rapidapi.com/apidojo/api/IMDb8/) and subscribe to get an API Key
4. Open `/src/config.py` and replace the value of `API_KEY` with the API Key from RapidAPI
5. Head over to the root directory of the project and run `app.py`
6. Enter `127.0.0.1:5000` into a browser to access the web app

## Prerequisites

```
Python 3.7.x
pyHTML 1.3.1
Flask 1.1.2
Requests 2.25.1
gunicorn 20.1.0
```
## Notes

The landing page allows the user to input any movie name, input can be gramatically incorrect or lower/upper-case.
After clicking search it will provide user with a list of Movies, TV Shows, Video Games, Videos, Shorts and TV Movies in the form of cards.
Once clicking on a desired title from the page, they are then redirected to the advisory page where all the content advisories are displayed.
History of the titles viewed are stored in session cookies to be viewed in a previously searched list on all the pages.

*RapidAPI's IMDb API requires a valid RapidAPI account. The API has a free plan of 500 requests a month. Subscriptions available for further API requests.*

## Pages

### Landing

![Image](/public/img/landing-page.PNG)

### Searched

![Image](/public/img/movies-page.png)

### Advisories

![Image](/public/img/advisories-page.PNG)

## Built With

* [Python 3.7](https://www.python.org) - Programming Language
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Web Framework
* [Requests](https://requests.readthedocs.io) - HTTP Library
* [Gunicorn](https://gunicorn.org) - WSGI HTTP Server
* [Material Design Bootstrap](https://mdbootstrap.com) - CSS Framework
* [RapidAPI's IMDb API](https://rapidapi.com/apidojo/api/IMDb8/) - IMDb API

## License

* [General Public License v2.0](https://github.com/mahirahman/Movie-Content-Advisory-Directory/blob/master/LICENSE)

## Authors

* Mahi Rahman