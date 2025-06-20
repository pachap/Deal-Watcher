from flask import Flask
import threading
import time
import requests

REPLIT_URL = "https://14c73959-dd24-4ebe-849c-3779f27186af-00-2l4122qrzz1w0.sisko.replit.dev/"

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Render ping service is alive"

def ping_replit():
    while True:
        try:
            print("🔁 Pinging Replit...")
            response = requests.get(REPLIT_URL)
            print("✅ Replit responded with status:", response.status_code)
        except Exception as e:
            print("❌ Failed to ping Replit:", e)
        time.sleep(300)  # 5 minutes

# Start pinging loop as background daemon
threading.Thread(target=ping_replit, daemon=True).start()
