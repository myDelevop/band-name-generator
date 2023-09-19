from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import os
import requests


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
Bootstrap5(app)
db = SQLAlchemy()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

ENDPOINT_SEARCH_MOVIE_DB_URL = "https://api.themoviedb.org/3/search/movie"
ENDPOINT_DETAIL_MOVIE_DB_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_API_READ_ACCESS_TOKEN = os.environ.get("MOVIE_DB_API_READ_ACCESS_TOKEN")
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(450), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(300))
    img_url = db.Column(db.String(300), nullable=False)


with app.app_context():
    db.create_all()


# with app.app_context():
#     first_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(first_movie)
#     db.session.add(second_movie)
#     db.session.commit()

class EditMovieForm(FlaskForm):
    rating = FloatField('Your Rating  Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(min=1, max=250)])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        scalar_movies = result.scalars()
        all_movies = convert_scalar_to_ojb(scalar_movies)

        for i in range(len(all_movies)):
            all_movies[i]["ranking"] = len(all_movies) - i
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditMovieForm()
    if form.validate_on_submit():
        review = request.form.get("review")
        rating = request.form.get("rating")

        # Update item in DB
        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
            movie_to_update.review = review
            movie_to_update.rating = rating
            db.session.commit()
        return redirect(url_for('home'))
    else:
        # Read A Particular Record By Query
        with app.app_context():
            current_scalar = [db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()]
            current_movie = convert_scalar_to_ojb(current_scalar)[0]
        return render_template('edit.html', movie=current_movie, form=form)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


movie_db_headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {MOVIE_DB_API_READ_ACCESS_TOKEN}"
        }

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = request.form.get("title")

        params = {
            "query": title
        }

        resp = requests.get(ENDPOINT_SEARCH_MOVIE_DB_URL, headers=movie_db_headers, params=params)
        resp.raise_for_status()
        movie_data = resp.json()["results"]

        return render_template('select.html', movies=movie_data)
    else:
        return render_template('add.html', form=form)


@app.route("/select/<movie_id>")
def select(movie_id):

    resp = requests.get(ENDPOINT_DETAIL_MOVIE_DB_URL+f"/{movie_id}", headers=movie_db_headers)
    resp.raise_for_status()
    movie_data = resp.json()

    new_movie = Movie(
        title=movie_data["title"],
        year=movie_data["release_date"].split("-")[0],
        img_url=f"{MOVIE_DB_IMAGE_URL}{movie_data['poster_path']}",
        description=movie_data["overview"]
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", movie_id=new_movie.id))


def convert_scalar_to_ojb(scalar_movies):
    all_movies = []
    for s in scalar_movies:
        obj = {
            "id": s.id,
            "title": s.title,
            "year": s.year,
            "description": s.description,
            "rating": s.rating,
            "ranking": s.ranking,
            "review": s.review,
            "img_url": s.img_url
        }
        all_movies.append(obj)
    return all_movies


if __name__ == '__main__':
    app.run(debug=True)
