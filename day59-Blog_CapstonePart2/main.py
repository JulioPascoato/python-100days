from flask import Flask, render_template
import requests


app = Flask(__name__)

url = "https://api.npoint.io/df9fb9dcd8f55f808c6a"
response = requests.get(url)
response.raise_for_status()
all_posts = response.json()


@app.route('/')
def get_all_posts():

    return render_template("index.html", all_posts=all_posts)


@app.route('/about')
def about_me():
    return render_template("about.html")


@app.route('/contact')
def contact_me():
    return render_template("contact.html")


@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", post=all_posts[num-1])


if __name__ == "__main__":
    app.run(debug=True)



