from typing import Any, Union

from fastapi import FastAPI
from Bot.bot import lifespan,ptb
from Bot.commands import start


import logging

logger = logging.getLogger(__name__)

app = FastAPI(lifespan=lifespan)
@app.get("/") 
async def read_root():
    logger.info("Hello World")
    return {"Hello": "World"}


@app.post("/webhook",status_code=200)
async def webhook(val:Any):
    print(val)
    return {"ok": True}



