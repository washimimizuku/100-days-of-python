from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_INFO_URL = "https://api.themoviedb.org/3/movie"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOME_REALLY_SECRET_KEY'
Bootstrap(app)

# Create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create movie table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    image_url = db.Column(db.String(250), nullable=True)


db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    # Order by rating
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html.jinja", movies=all_movies)


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(TMDB_SEARCH_URL, params={
            "api_key": TMDB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        print(data)
        return render_template("select.html.jinja", options=data)

    return render_template('add.html.jinja', form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{TMDB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={
                                "api_key": TMDB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # Remove month and day
            year=data["release_date"].split("-")[0],
            image_url=f"{TMDB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html.jinja', movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
