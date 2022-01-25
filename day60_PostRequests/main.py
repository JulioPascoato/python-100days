from flask import Flask, render_template, request
import requests
import smtplib


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


app = Flask(__name__)
OWN_EMAIL = ""
OWN_PASSWORD = ""


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


@app.route('/contact', methods=["GET", "POST"])
def contact_me():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", post=all_posts[num-1])


if __name__ == "__main__":
    app.run(debug=True)


