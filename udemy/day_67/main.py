from time import strftime

from flask import Flask, render_template, request,redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'standard-all'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.date)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


class PostForm(FlaskForm):
    title = StringField('Blog Post Title')
    subtitle = StringField('Subtitle')
    author = StringField('Your Name')
    img_url = StringField('Blog Image URL')
    # Date
    body = CKEditorField('Blog Content')  # <--
    submit = SubmitField('Submit Post')


# TODO: add_new_post() to create a new blog post
@app.route('/add', methods=["GET", "POST"])
def add_new_post():
    form = PostForm()

    if form.validate_on_submit():
        date_now = datetime.now().strftime(strftime("%B %d, %Y"))
        title = request.form.get("title")
        subtitle = request.form.get("subtitle")
        author = request.form.get("author")
        img_url = request.form.get("img_url")
        body = request.form.get("body")  # <--

        post = BlogPost(
            title=title,
            subtitle=subtitle,
            author=author,
            date=date_now,
            img_url=img_url,
            body=body)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    else:
        return render_template("make-post.html", form=form)

# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
