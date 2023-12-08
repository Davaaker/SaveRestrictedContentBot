#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "209235"
API_HASH = "169ee702e1df4b6e66d80311db36cc43"
BOT_TOKEN = "6566629090:AAHGEP1QyxXgkTXJsDEYTFeU4fsxAeucOIE"
SESSION = "BQGl_MgAf6tdfKXzP_zafaomZalwlqc4_GxkSVhZbHHWjG2kIv2lDd4k4PpBBrW60ztGOngYO_8mtITWOfPmvFx-exRS-r-boGgx1frmR1IoSBsbc7DqL2UOoydfYzhTsb0U1-eFj-_aNzwPOB-o-ge0M_Bo-m-AI7S0cpnWJwFtFrqxAUeHeVMUebcEz39cEjo_XzrAdZBiE1PP7PLhV7ZdO_PmHwn4nGiYiqj_zCZMvEu3w6QpNfKYBf7WhF_sj1OOVlUj7iUGXMaAjbDQMO40IpWFrZYS94lZEQlZIswdRXOharrx6qKXoVVCjlkrtISfNn7gIaI5fIoO3ahQZVNIhMhrMAAAAAAu3xDDAA"
FORCESUB = "MezoticStore"
AUTH = "1882202047"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
