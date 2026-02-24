import os
import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Webhook server is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if not data:
        print("⚠️ Received request with no JSON", flush=True)
        return jsonify({"status": "error", "message": "No JSON received"}), 400

    # Print to stdout with flush so Render logs capture it
    print(f"📩 Received webhook: {data}", flush=True)

    action = data.get("action", "").lower()
    symbol = data.get("symbol", "UNKNOWN")
    price = data.get("price", "UNKNOWN")

    if action == "buy":
        print(f"🚀 BUY signal for {symbol} at price {price}", flush=True)
    elif action == "sell":
        print(f"🔻 SELL signal for {symbol} at price {price}", flush=True)
    else:
        print(f"ℹ️ No action detected, received data: {data}", flush=True)

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # debug=False and use_reloader=False so only one process logs to stdout
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
