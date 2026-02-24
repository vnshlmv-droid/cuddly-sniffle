
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Webhook server is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Received webhook:", data)

    # you can do anything here
    # save to file, trigger function, etc.

    return jsonify({"status": "received"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)