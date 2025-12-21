from flask import Flask, jsonify, request

app = Flask(__name__)

# Datenbank-Simulation (in-memory)
items = []

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_items():
    data = request.json
    items.append(data)
    return jsonify({"message": "Item addes" }),201

if __name__ == "__main__":
    app.run(debug=True)