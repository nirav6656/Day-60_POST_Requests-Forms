import requests
from flask import Flask, render_template, request
import smtplib
import os

OWN_EMAIL = os.environ["OWN_EMAIL"]
OWN_PASSWORD = os.environ["OWN_PASSWORD"]

app = Flask(__name__, static_folder='static', static_url_path='/static')
api_endpoint = "https://api.npoint.io/8152213a3b7dd208d23f"
@app.route('/')
def home_page():
    data = requests.get(url=api_endpoint).json()
    return render_template("index.html",posts = data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<id_no>')
def post(id_no):
    data = requests.get(url=api_endpoint).json()
    return render_template("post.html", id_no = int(id_no)-1, posts = data)

# @app.route('/contact')
# def contact():
#     return render_template("contact.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)
