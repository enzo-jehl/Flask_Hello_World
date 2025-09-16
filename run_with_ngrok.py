from flask import Flask
from pyngrok import ngrok
import threading
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask via Docker and ngrok!"

def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print(f"🌐 Server is publicly available at: {public_url}")

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    time.sleep(120)
    print("⏳ 120 seconds elapsed. Shutting down...")
    ngrok.disconnect(public_url)
    ngrok.kill()
