import os
from pyrogram import Client, filters
import rapidjson as json
import requests
import time

StartTime = time.time()


API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
SESSION = os.environ.get("SESSION", None) 
PREFIX = os.environ.get("PREFIX", None) 


app = Client(
      session_name=SESSION,
      api_id=API_ID,
      api_hash=API_HASH,
)

REPOLINK = """ Source code: [Github](https://github.com/Moezilla/vc-userbot)
License: [ GPL-3.0 License](https://github.com/moezilla/vc-userbot/blob/master/LICENSE.md)"""

@app.on_message(filters.command("repo", PREFIX))
async def repo(_, message):
    await message.reply_text(REPOLINK)


@app.on_message(filters.command("smug", PREFIX))
def truth(_, message):
    smug = requests.get("https://nekos.life/api/v2/img/smug").json()
    smug = url.get("smug")
    message.reply_text(smug)
