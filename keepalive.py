from flask import Flask
import threading
import time
import requests

REPLIT_URL = "https://14c73959-dd24-4ebe-849c-3779f27186af-00-2l4122qrzz1w0.sisko.replit.dev"

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Render ping service is alive"

def ping_replit():
    while True:
        try:
            print("🔁 Pinging Replit...")

            headers = {
                'User-Agent': 'RenderHealthBot/1.0',
                'Accept': '*/*'
            }

            response = requests.get(REPLIT_URL, headers=headers, timeout=10)

            print("✅ Replit responded")
            print("    ➤ Status code:", response.status_code)
            print("    ➤ Response text (first 100 chars):", response.text[:100])

        except requests.exceptions.RequestException as e:
            print("❌ Ping failed:", repr(e))

        time.sleep(300)




# Start pinging loop as background daemon
threading.Thread(target=ping_replit, daemon=True).start()
