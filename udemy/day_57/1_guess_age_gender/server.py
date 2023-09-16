import requests
from flask import Flask, render_template
import random
import json
from datetime import date

app = Flask(__name__)


GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGIFY_ENDPOINT = "https://api.agify.io"
BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template(
        template_name_or_list="index.html",
        num=random_number,
        year=current_year,
        name="Rocco"
    )


@app.route('/guess/<name>')
def guess(name):
    name = str(name).capitalize()
    estimated_age = get_age(name)
    estimated_gender = get_gender(name)
    return render_template(
        template_name_or_list="guess_page.html",
        name=name,
        age=estimated_age,
        gender=estimated_gender
    )


@app.route("/blog/<num>")
def blog(num):
    print(num)
    response = requests.get(BLOG_URL)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


def get_age(name):
    params = {
        "name": name
    }
    response = requests.get(AGIFY_ENDPOINT, params=params)
    response.raise_for_status()
    json_data = json.loads(response.text)
    return json_data['age']


def get_gender(name):
    params = {
        "name": name
    }
    response = requests.get(GENDERIZE_ENDPOINT, params=params)
    response.raise_for_status()
    json_data = json.loads(response.text)
    return json_data['gender']


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
