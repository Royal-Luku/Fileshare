#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7085783660:AAE-gZ59W1wyBsOpfa1xapw-gzjR7XaeuG0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13708534"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "51b384fee3c86840ee2ba7938f0beff4")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002073649382"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1782834874"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://RoyalTelegram:RoyalTelegram@cluster0.ixfndqo.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Royal")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001774060800"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello, {mention}\n\nThis Is a Permanent File Store Bot Of @MovieVillaYT 🍸</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1782834874").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Oye, {mention}\n\nMovies And Series Dekhna Hoon Toh mera updated channel join karo 😒</i></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{filename}\n\n         ❤ We Love You ❤\n🔥 ➹ Join Now [ <a href='t.me/wombackup'>WOM-BACKUP</a> ] ➷ 🔥</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", False) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>Giving Movies Is My Job\nTaking Movies Is Your Job\nSo Mind Your Own Business 😹☕</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
