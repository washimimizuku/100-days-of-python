from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
        dictionary = {column.name: getattr(
            self, column.name) for column in self.__table__.columns}
        return dictionary


@app.route("/")
def home():
    return render_template("index.html.jinja")


@app.route("/random")
def get_random():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_list():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def get_search():
    location_parameter = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(
        location=location_parameter).first()

    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.json["name"],
        map_url=request.json["map_url"],
        img_url=request.json["img_url"],
        location=request.json["location"],
        seats=request.json["seats"],
        has_toilet=request.json["has_toilet"],
        has_wifi=request.json["has_wifi"],
        has_sockets=request.json["has_sockets"],
        can_take_calls=request.json["can_take_calls"],
        coffee_price=request.json["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 201


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_cafe_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)

        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
