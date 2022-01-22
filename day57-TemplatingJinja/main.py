from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", post=all_posts[num - 1])


if __name__ == "__main__":
    app.run(debug=True)
