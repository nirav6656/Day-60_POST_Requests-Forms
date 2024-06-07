import requests
from flask import Flask, render_template


app = Flask(__name__, static_folder='static', static_url_path='static')
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

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/form-entry')
def receive_data():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
