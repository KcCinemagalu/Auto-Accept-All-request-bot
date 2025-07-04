from os import environ

API_ID = int(environ.get("API_ID", "27669314"))
API_HASH = environ.get("API_HASH", "21895efc9c1187db53f3d542e4c23051")
BOT_TOKEN = environ.get("BOT_TOKEN", "7958738359:AAEuzYErqPNWVkiStd0SUj9d2micYMpoJho")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", "7072018503"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://max20:max20@cluster0.y6vu6gp.mongodb.net/?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "cluster0")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
