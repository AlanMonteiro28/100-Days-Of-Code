from flask import Flask

def make_bold(function):
    def bold():
        text = function()
        return f'<b>{text}</b>'
    return bold

def make_emphasis(function):
    def emphasis():
        text = function()
        return f'<em>{text}</em>'
    return emphasis

def make_underlined(function):
    def underlined():
        text = function()
        return f'<u>{text}</u>'
    return underlined
  
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXloNDZwbngxOWZnMmY3ajR6ZzF2eDJzaHhvNmh1Y2ppMjNncHlkNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sE1fbQPozKg3q5I2W2/giphy.gif" width="300px">'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == '__main__':
    app.run(debug=True)

