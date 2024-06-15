import os
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from pyrogram import idle
from Uploader.config import *





# Prepare bot client
bot = Client(
    "botclient",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    sleep_threshold=30
)

# Prepare user client if session string is provided
if SESSION_STRING:
    user_client = Client(
        "UserClient",
        session_string=SESSION_STRING,
        api_id=API_ID,
        api_hash=API_HASH,
        sleep_threshold=30,
        no_updates=True
    )
else:
    user_client = None

# Start the clients
if __name__ == "__main__":
    # Create download directory if it does not exist
    if not os.path.isdir(DOWN_DIR):
        os.makedirs(DOWN_DIR)
        
    # Start bot client
    bot.start()
    
    # Start user client if available
    if user_client:
        user_client.start()
    
    # Keep the main thread running
    idle()
    
    # Stop the clients
    bot.stop()
    if user_client:
        user_client.stop()
