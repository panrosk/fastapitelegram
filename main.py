from typing import Any, Union

from fastapi import FastAPI
from telegram import Update
from Bot.bot import lifespan
 
import logging

logger = logging.getLogger(__name__)

app = FastAPI(lifespan=lifespan)
@app.get("/") 
async def read_root():
    logger.info("Hello World")
    return {"Hello": "World"}


@app.post("/webhook")
async def webhook(val:Any):

    print(val)
    return {"ok": True}
