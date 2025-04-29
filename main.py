from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Ambil Token dan Chat ID dari environment variables
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return "Invalid request: no JSON", 400

    # Ambil data dari TradingView webhook
    pair = data.get("pair", "Unknown")
    price = data.get("price", "N/A")
    signal = data.get("signal", "N/A").upper()
    time = data.get("time", "N/A")

    # Format pesan ke Telegram
    message = f"""
📢 *Trading Signal Received!*
Pair: *{pair}*
Price: *{price}*
Signal: *{signal}*
Time: `{time}`
"""
    send_telegram_message(message)
    return "ok", 200

@app.route('/', methods=['GET'])
def home():
    return "Bot is running.", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
