from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load from .env or Render environment
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    # Format pesan dari TradingView (dengan asumsi struktur JSON-nya)
    pair = data.get("pair", "UNKNOWN")
    price = data.get("price", "N/A")
    signal = data.get("signal", "N/A")
    time = data.get("time", "N/A")

    msg = f"📊 *{pair}*\n💥 *Signal:* {signal}\n💰 *Price:* {price}\n⏰ *Time:* {time}"
    send_telegram_message(msg)
    return 'ok', 200

@app.route('/', methods=['GET'])
def home():
    return "Bot is running.", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
