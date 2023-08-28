#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5938684526:AAFu_sAkKAxpnsajhplxZRh3sFc1RHn451o")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13708534"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "51b384fee3c86840ee2ba7938f0beff4")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001961688904"))

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
START_MSG = os.environ.get("START_MESSAGE", "<b>Hey, {mention}!  😃\n\nThis is Royal The Permanent File Store Bot. 🤖\n\nSend me any file And I will give you a permanent Sharable Link. I Support Channel Also! Check About Bot Button.\n\nNote❗\nDon't upload any adult content otherwise you will be ban. 🚫</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1782834874").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hey, {mention}\n\n<b>You need to join in my Channel to use me\n\nKindly Please join Channel ✅</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{filename}\n\n         ❤ We Love You ❤\n🔥 ➹ Join Now [WOM-BACKUP 🚩](https://t.me/WOMBACKUP) ➷ 🔥</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", False) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>❌ Don't Send Me Any Message Or File! \nI am Work's Only For <a href='https://t.me/wombackup'>This Channel!</a>\n\nFor More Query Contact My <a href='t.me/royaldwip'>Devoloper!</a> ✅</b>"

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
