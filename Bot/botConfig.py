from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN")
    BOT_NAME = getenv("BOT_NAME")
    ADMIN_ID = getenv("ADMIN_ID")
    HOST = getenv("BOT_HOST")

