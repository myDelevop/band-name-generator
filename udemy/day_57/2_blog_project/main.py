from post import Post
import requests
from flask import Flask, render_template

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

all_posts = []
response = requests.get(BLOG_URL)
response.raise_for_status()

json_data = response.json()

for post in json_data:
    p = Post(
        post_id=int(post["id"]),
        title=str(post["title"]),
        subtitle=post["subtitle"],
        body=post["body"])
    all_posts.append(p)


@app.route('/')
def home():
    return render_template("index.html", all_blogs=all_posts)

@app.route("/post/<int:blog_id>")
def show_blog(blog_id):
    blog = None
    for loop_post in all_posts:
        if loop_post.id[0] == blog_id:
            blog = loop_post
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)

