from typing import Any, Union
import json
from fastapi import FastAPI, Request
from Bot.bot import lifespan,ptb
from Bot.commands import start
from Bot.botConfig import Config

import logging

logger = logging.getLogger(__name__)

app = FastAPI(lifespan=lifespan)
@app.get("/") 
async def read_root():
    logger.info("Hello World")
    return {"Hello": "World"}


@app.post("/webhook",status_code=200)
async def webhook(val:Request):
    data = await val.json()
    await ptb.bot.send_message(Config.ADMIN_ID, json.dumps(data, indent=2))
    return {"ok": True}





