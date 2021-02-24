import os
from dotenv import load_dotenv
import event
import asyncio
from asgiref.sync import async_to_sync

def print_camion():
  print("camion")

def print_something(something: str):
  print(something)

event.connect("camion_registered", print_camion)
event.connect("camion_registered", print_something)

async def trigger_camion_registered():
  await event.trigger("camion_registered", "something about trucks")

print("async_to_sync ...")
async_to_sync(trigger_camion_registered)()

def token_print():
  load_dotenv()
  print("TOKEN", os.getenv("TOKEN"))

def run():
  token_print()