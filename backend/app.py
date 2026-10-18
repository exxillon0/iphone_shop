from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Каталог iPhone с ценами и картинками
IPHONES = [
    {
        "id": 1,
        "name": "iPhone 15 Pro Max",
        "price": 1199,
        "color": "Blue Titanium",
        "storage": "256 GB",
        "image": "/static/iphone15promax.jpg"
    },
    {
        "id": 2,
        "name": "iPhone 15 Pro",
        "price": 999,
        "color": "Natural Titanium",
        "storage": "128 GB",
        "image": "/static/iphone15pro.jpg"
    },
    {
        "id": 3,
        "name": "iPhone 15",
        "price": 799,
        "color": "Pink",
        "storage": "128 GB",
        "image": "/static/iphone15.jpg"
    },
    {
        "id": 4,
        "name": "iPhone 14",
        "price": 699,
        "color": "Midnight",
        "storage": "128 GB",
        "image": "/static/iphone14.jpg"
    },
    {
        "id": 5,
        "name": "iPhone SE 2022",
        "price": 429,
        "color": "Starlight",
        "storage": "64 GB",
        "image": "/static/iphonese.jpg"
    }
]

@app.route("/")
def index():
    return jsonify({"service": "iphone-shop-backend", "status": "ok"})

@app.route("/api/iphones")
def get_iphones():
    return jsonify(IPHONES)

@app.route("/api/iphones/<int:iphone_id>")
def get_iphone(iphone_id):
    for phone in IPHONES:
        if phone["id"] == iphone_id:
            return jsonify(phone)
    return jsonify({"error": "Not found"}), 404

@app.route("/api/price/<int:iphone_id>")
def get_price(iphone_id):
    for phone in IPHONES:
        if phone["id"] == iphone_id:
            return jsonify({"id": iphone_id, "price": phone["price"], "currency": "USD"})
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)