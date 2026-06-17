from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Sami"},
    {"id": 2, "name": "Tanaka"}
]

@app.route("/")
def home():
    return jsonify({"message": "API is running"})

@app.route("/users")
def get_users():
    return jsonify(users)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
