from contextlib import asynccontextmanager
from fastapi import FastAPI
from Bot.botConfig import Config
from telegram.ext import Application

# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Handling-network-errors
ptb = (
    Application.builder()
    .token(Config.BOT_TOKEN)
    .read_timeout(7)
    .get_updates_read_timeout(42)
)

ptb = ptb.updater(None)
ptb = ptb.build()


@asynccontextmanager
async def lifespan(_: FastAPI):
    if Config.HOST:
        await ptb.bot.setWebhook(Config.HOST+"/webhook")
    async with ptb:
        await ptb.start()
        yield
        await ptb.stop()
