### **Project Structure**

├── bot.py        # Contains the Telegram bot logic
└── app.py        # Contains both Flask application and runs the Telegram bot
```

### **Running the Application**

To run both your Flask application and Telegram bot, simply execute the `app.py` file:

```bash
python app.py
```

### Explanation:

- **Threading**: The Telegram bot runs in a separate thread to avoid blocking the Flask application. This allows both services to run concurrently.
- **Modularity**: Even though both are managed from `app.py`, the bot logic is still separated into `bot.py` for clarity and maintainability.
- **No Need for `run.py`**: By using threading within `app.py`, you consolidate the execution of both services, reducing the need for an additional file.


This setup allows you to keep your project organized while running both the Flask app and the Telegram bot efficiently.