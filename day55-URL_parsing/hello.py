from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function


@app.route('/')
def hello_world():
    return "<h1>Hello, world!</h1>" \
           "<p>This is a paragraph</p>"


@app.route("/bye")
@make_bold
@make_emphasis
def say_bye():
    return "Bye."


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
