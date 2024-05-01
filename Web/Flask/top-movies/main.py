from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_URL = "https://api.themoviedb.org/3/search/movie"
API_INFO_URL = "https://api.themoviedb.org/3/movie"

API_HEADERS = {
    "accept": "application/json",
    "Authorization": "Your API AUTH"
}

MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/original/"

# FLASK
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
   __tablename__ = "movies"
   id: Mapped[int] = mapped_column(Integer, primary_key=True)
   title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
   year: Mapped[int] = mapped_column(Integer, nullable=False)
   description: Mapped[str] = mapped_column(String(500), nullable=False)
   rating: Mapped[float] = mapped_column(Float, nullable=False)
   ranking: Mapped[int] = mapped_column(Integer, nullable=False)
   review: Mapped[str] = mapped_column(String(250), nullable=False)
   img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()

# CREATE EDIT-FORM
class RateMovieForm(FlaskForm):
   rating = StringField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
   review = StringField(label="Your Review", validators=[DataRequired()])
   submit = SubmitField("Done")

# CREATE ADD-FORM
class FindMovieForm(FlaskForm):
   title = StringField(label="Movie Title", validators=[DataRequired()])
   submit = SubmitField("Add Movie")

# FLASK APPLICATIONS
# INDEX
@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

# EDIT
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
   movie_selected = Movie.query.get(id)
   rate_form = RateMovieForm()
   if rate_form.validate_on_submit():
      movie_to_update = Movie.query.get(id)
      movie_to_update.rating = float(rate_form.rating.data)
      movie_to_update.review = rate_form.review.data
      db.session.commit()
      return redirect(url_for('home'))
   
   return render_template("edit.html", movie=movie_selected, form=rate_form)
   
# DELETE 
@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

# ADD
@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = FindMovieForm()
    if add_form.validate_on_submit():
        response = requests.get(API_URL, headers=API_HEADERS, params={"query":add_form.title.data}).json()
        data = response["results"]
        return render_template("select.html", options=data)
    
    return render_template("add.html", form=add_form)

# SELECT
@app.route("/find")
def find():
   api_id = request.args.get("id")
   movie_api_url = f"{API_INFO_URL}/{api_id}"
   response = requests.get(movie_api_url, headers=API_HEADERS, params={"language": "en-US"})
   data = response.json()
   new_movie = Movie(
       title=data['title'],
       year=data['release_date'].split('-')[0],
       description=data['overview'],
       img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
       rating=round(data['vote_average']),
       ranking="Add ranking",
       review="Add review"
     )
   with app.app_context():
        db.session.add(new_movie)
        db.session.commit()

   return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
