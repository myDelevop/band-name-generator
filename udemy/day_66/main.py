import json
import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random_1")
def get_random_cafe_1():
    result = db.session.execute(db.select(Cafe)).scalars()
    all_cafes = result.all()
    random_cafe = random.choice(all_cafes)

    return jsonify(
        id=random_cafe.id,
        name=random_cafe.name,
        map_url=random_cafe.map_url,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        seats=random_cafe.seats,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        has_sockets=random_cafe.has_sockets,
        can_take_calls=random_cafe.can_take_calls,
        coffee_price=random_cafe.coffee_price)


@app.route("/random_2")
def get_random_cafe_2():
    result = db.session.execute(db.select(Cafe)).scalars()
    all_cafes = result.all()
    random_cafe = random.choice(all_cafes)

    return jsonify(cafe={
        # Omit the id from the response
        # id=random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,

        "amenities": {
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price
        }
    })


@app.route("/random_3")
def get_random_cafe_3():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    all_cafes = result.all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def get_cafes_by_location():
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).filter_by(location=location).order_by(Cafe.name)).scalars()
    all_cafes = result.all()
    if len(all_cafes) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    print(request.args)
    cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )

    db.session.add(cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(response={"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def caffe_closed(cafe_id):
    secret = "nsusdn1243uyA21!"
    api_key = request.args.get("api-key")
    if api_key != secret:
        return jsonify(response={"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the caffe from the database."})
    else:
        return jsonify(response={"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}})


if __name__ == '__main__':
    app.run(debug=True)
