import os, time, datetime, pytz



class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    API_ID = int(os.environ.get("API_ID", ""))
    
    API_HASH = os.environ.get("API_HASH", "")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    SESSION_STRING = os.environ.get("SESSION_STRING", "")

    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "LinkToFileUploaderBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))

    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "5305133820").split(" ")]
    
  
