from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
db = SQLAlchemy()

# Create a New Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


def convert_scalar_to_ojb(scalars):
    all_books = []
    for s in scalars:
        obj = {
            "id": s.id,
            "title": s.title,
            "author": s.author,
            "rating": s.rating
        }
        all_books.append(obj)
    return all_books

@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = convert_scalar_to_ojb(result.scalars())
        print(all_books)

    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            book = Book(title=request.form.get("title"),
                        author=request.form.get("author"),
                        rating=request.form.get("rating"))
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    if request.method == "POST":
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
            # or book_to_update = db.get_or_404(Book, book_id)
            book_to_update.rating = request.form["new_rating"]
            db.session.commit()
        return redirect(url_for('home'))
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)

