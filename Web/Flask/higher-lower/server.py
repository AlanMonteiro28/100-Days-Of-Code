from flask import Flask
from random import randint

random_number = randint(0, 9)

colors = ["Gray", "Peru", "Blue", "Green", "DarkViolet", "Yellow", "Orange", "HotPink", "Red"]

def styling(function):
    def wrapper(*args, **kwargs):
        content = function(*args, **kwargs)
        color = colors[kwargs.get("number", None)]
        text = content.split("<img")[0]
        img_tag = content.split("<img")[1]
        h1_tag = f"<h1 style='color:{color}'>{text}</h1>"
        return f"{h1_tag} <img {img_tag}"
    return wrapper


app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"

@app.route("/<int:number>")
@styling
def user_number(number):
    if number < random_number:
        return f"Too low, try again!" \
                f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > random_number:
        return f"Too high, try again!" \
                f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"You found me!" \
                f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)