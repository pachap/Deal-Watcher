from flask import Flask
import threading
import time
import requests

REPLIT_URL = "https://14c73959-dd24-4ebe-849c-3779f27186af-00-2l4122qrzz1w0.sisko.replit.dev"

app = Flask(__name__)

@app.route('/')
def home():
    return "🔁 Ping service is active!"

def ping_replit():
    while True:
        try:
            print("🔁 Pinging Replit...")
            requests.get(REPLIT_URL)
        except Exception as e:
            print("⚠️ Ping failed:", e)
        time.sleep(300)  # 5 minutes

threading.Thread(target=ping_replit).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
