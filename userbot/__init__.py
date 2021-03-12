import ast
import logging
import os
from configparser import ConfigParser
from datetime import datetime

from userbot.userbot import UserBot

name = "userbot"

if bool(os.environ.get("ENV", False)):
    # Pyrogram details
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    USERBOT_SESSION = os.environ.get("USERBOT_SESSION", None)

    

# Extra details
__version__ = "1.0.0"
__author__ = "Mødêr(🇯🇵)"

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()

UserBot = UserBot(name)


# from pyrogram import __version__
