from flask import Flask
from threading import Thread
import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Flask app with a Telegram bot!"

# Function to start both the Flask app and the bot
def start_services():
    # Start the bot in a separate thread
    bot_thread = Thread(target=bot.run_bot)
    bot_thread.start()

    # Start the Flask app
    app.run(host="0.0.0.0", port=5000)

# Entry point to run the Flask app and Telegram bot together
if __name__ == "__main__":
    start_services()
