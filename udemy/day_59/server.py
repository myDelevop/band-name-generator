from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOG_ENDPOINT = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
response = requests.get(BLOG_ENDPOINT)
response.raise_for_status()
all_blogs = response.json()

@app.route('/')
def home():
    return render_template(template_name_or_list="index.html", json_blogs=all_blogs)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
