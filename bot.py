import telebot
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
# Initialize the bot with your token
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm your bot!")

def run_bot():
    bot.polling(none_stop=True)

# Only run the bot if this file is executed directly
if __name__ == "__main__":
    run_bot()
