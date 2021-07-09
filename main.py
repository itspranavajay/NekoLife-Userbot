import os
from pyrogram import Client, filters
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
