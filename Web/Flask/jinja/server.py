from flask import Flask, render_template
from random import randint
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 10)
    year = datetime.date.today().year

    return render_template("index.html", num=random_number, current_year=year)


@app.route("/guess/<name>")
def guess(name):
    n = name.capitalize()
    year = datetime.date.today().year
    genderize_data = requests.get(f"https://api.genderize.io/?name={n}").json()
    agify_data = requests.get(f"https://api.agify.io/?name={n}").json()
    age = agify_data["age"]
    gender = genderize_data["gender"]

    return render_template("guess.html", name=n, age=age, gender=gender, current_year=year)


@app.route("/blog")
def get_blog():
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
