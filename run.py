from threading import Thread
import app
import bot

# Start the Flask app in a separate thread
def run_flask():
    app.app.run(host="0.0.0.0", port=5000)

# Create threads for Flask and the bot
flask_thread = Thread(target=run_flask)
bot_thread = Thread(target=bot.run_bot)

# Start both threads
flask_thread.start()
bot_thread.start()

# Join both threads to keep them running
flask_thread.join()
bot_thread.join()
