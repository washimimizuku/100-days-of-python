from bs4 import BeautifulSoup
import os
import re
import requests
from requests_html import HTMLSession


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = os.path.join(LOCATION, "100_best_movies.html")
MOVIES_FILE = os.path.join(LOCATION, "movies.txt")


# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()
 
    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)
 
def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
    return BeautifulSoup(content, "html.parser")
 
# Read web file if it exists, load from internet if it doesn't exist
soup = read_web_file()

movies_raw = soup.find_all(name="h3")
movies = [movie.text for movie in movies_raw][::-1]

with open(MOVIES_FILE, mode="w") as file:
    for i in range(len(movies)):
        movie = movies[i]

        # Fix errors on list (Some have no number, others have wrong number os symbol)
        if bool(re.search('^\d{1,3}: ', movie)):
            movie = movie[movie.index(":") + 2:]
        elif bool(re.search('^\d{1,3}\) ', movie)):
            movie = movie[movie.index(")") + 2:]
        
        # Add real index again
        movie = f"{i + 1}) {movie}"

        file.write(f"{movie}\n")
