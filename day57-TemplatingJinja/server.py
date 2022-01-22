from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    built_by = "Julio Pascoato"
    random_number = random.randint(1, 10)

    return render_template("index_1.html", random_number=random_number, year=current_year, built_by=built_by)


@app.route("/guess/<name>")
def guess(name):
    parameters = {
        "name": name
    }

    response = requests.get("https://api.agify.io", params=parameters)
    response.raise_for_status()
    age = response.json()

    response = requests.get("https://api.genderize.io", params=parameters)
    response.raise_for_status()
    gender = response.json()

    return render_template("guess.html", age=age, gender=gender)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/8ffc54281d343e65c282"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
