from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def form():
    data = request.get_json()
    name = data.get("name", "")
    phone = data.get("phone", "")
    message = data.get("message", "")

    with open("requests.txt", "a", encoding="utf-8") as f:
        f.write(f"Имя: {name}\nТелефон: {phone}\nСообщение: {message}\n---\n")

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
