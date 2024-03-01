import asyncio
from Bot.utils import sendMessageToAdmin


async def test_simple():
    await sendMessageToAdmin("gola")
    await asyncio.sleep(3)
