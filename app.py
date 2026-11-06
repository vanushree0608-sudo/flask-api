from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/users")
def users():
    user_data = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "David"},
        {"id": 3, "name": "Alice"}
    ]
    return jsonify(user_data)

if __name__ == "__main__":
    app.run(debug=True)