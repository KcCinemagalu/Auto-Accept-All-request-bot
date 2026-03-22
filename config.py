from os import environ

API_ID = int(environ.get("API_ID", "14356452"))
API_HASH = environ.get("API_HASH", "cac21249a0c6373a1b742afb8dbc9cb7")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003863983646"))
ADMINS = int(environ.get("ADMINS", "1663497903"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "AcceptAllRequestBot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
