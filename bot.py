import os
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from pyrogram import idle

# Define your bot token, API ID, API hash, session string, and download directory
BOT_TOKEN = "your_bot_token"
API_ID = your_api_id
API_HASH = "your_api_hash"
SESSION_STRING = "your_session_string"
DOWN_DIR = "./DOWNLOADS"

# Clear log file if exists
if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=50000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram")
logging.getLogger("pySmartDL")
logging.getLogger("aria2p")
# Logger for printing
LOGGER = logging.getLogger(__name__)

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
