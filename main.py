from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Ganti ini dengan Token Bot kamu
TOKEN = 7670500235:AAE2HWbPoT1HyUefAvP4JEbBYFjsWxXgX7Y
# Ganti ini dengan Chat ID grup kamu
CHAT_ID = -1002595552449

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
    message = data.get('message', '⚡️ Ada alert baru dari TradingView!')
    send_telegram_message(f"🚀 TradingView Alert: \n{message}")
    return 'ok', 200

@app.route('/', methods=['GET'])
def home():
    return "Bot is running.", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
