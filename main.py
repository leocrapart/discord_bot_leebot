import discord 
import os
from dotenv import load_dotenv
import re
from tinydb import TinyDB, Query
from keep_alive import keep_alive
import xp

load_dotenv()

db = TinyDB("db.json")

client = discord.Client()


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  await print_command_and_args(message)
  author_msg(message)
  await hello_msg(message)
  await attack_msg(message)
  await add_person(message)
  await get_leo(message)
  await add_one_xp_to_leo(message)
  await ayuken_msg(message)

async def print_command_and_args(message):
  command = get_command(message)
  args = get_args(message)
  if command:
    await discord_print(f"command => {command}", message)
  if args:
    await discord_print(f"args => {args}", message)


def get_args(message):
  command = get_command(message)
  if command:
    input = message.content
    first_space_index = None
    try:
      first_space_index = input.index(" ")
    except:
      args = None
    
    if first_space_index:
      arg_string = input[first_space_index:]
      arg_string_striped = arg_string.strip()
      args = re.split(r"\ +", arg_string_striped)
    else:
      args = None
    return args

async def discord_print(text, message):
  await message.channel.send(text)

def get_command(message):
  input = message.content
  if input.startswith("$"):
    first_space_index = None 
    try:
      first_space_index = input.index(" ")
    except:
      command = input[:1]
    
    if first_space_index:
      command = input[1:first_space_index]
    else:
      command = input[1:]
    return command
  else:
    return

async def print_xp(name, xp_amount, message):
  await message.channel.send(f"{name} got +{xp_amount} xp")

async def add_one_xp_to_leo(message):
  if message.content.startswith("$xpleo+1"):
    xp.add_xp_to_player("leo", 1)
    leo = db.search(Query().name == "leo")[0]
    await print_xp(leo["name"], 1, message)

async def add_person(message):
  if message.content.startswith("$add"):
    doc = {
      "name": "leo",
      "age": 19 
    }
    db.insert(doc)
    await message.channel.send("added to db")

async def get_leo(message):
  if message.content.startswith("$get"):
    res = db.search(Query().name == "leo")
    await message.channel.send(res)

def author_msg(message):
  if message.author == client.user:
    return

async def hello_msg(message):
  if message.content.startswith("$hello"):
      await message.channel.send("Hello !")

async def attack_msg(message):
  if message.content.startswith("$attack"):
    await message.channel.send("Dragon high kick to @enbot !")
  
async def ayuken_msg(message):
  if message.content.startswith("$AYUKEN"):
    await message.channel.send("AAAYYUUUUUUUKKEN2 !!!")


keep_alive()
print("TOKEN", os.getenv("TOKEN"))
client.run(os.getenv("TOKEN"))