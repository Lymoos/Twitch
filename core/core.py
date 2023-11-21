from alltwitch.twitch import TwitchStart
from alltelegram.telegram import TelegramStart
import os
from alltelegram.telegram import main_telegram
import asyncio
import multiprocessing
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def Start():
    twitch = multiprocessing.Process(target=TwitchStart(client_id,client_secret))
    telegram = multiprocessing.Process(target=asyncio.run(main_telegram()))
    twitch.start()
    telegram.start()
    twitch.join()
    telegram.join()