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

  discord_listener = DiscordListener(message)
  await discord_listener.listen_to_commands()


class DiscordListener():

  command_prefix = "$"

  def __init__(self, message):
    self.message = message

  async def listen_to_commands(self):
    await self.listen_to_hello_command()
    await self.listen_to_attack_command()
    await self.listen_to_defence_command()
  
  async def listen_to_hello_command(self):
    await self.listen_to_command("hello", "Hello!")

  async def listen_to_attack_command(self):
    await self.listen_to_command("attack", "High kick!")

  async def listen_to_defence_command(self):
    await self.listen_to_command("defence", "FORMATION TORTUE")

  async def listen_to_ayuken_command(self):
    await self.listen_to_command("ayuken", "AYUUUUKEN")

  async def listen_to_command(self, command, reply_text):
    message = self.message
    raw_command = self.command2raw_command()
    if self.message_startswith(raw_command):
      await self.send_on_actual_channel(reply_text)

  def command2raw_command(self, command):
    prefix = self.command_prefix
    return prefix + command

  def message_startswith(self, command):
    return self.message.content.startswith(command)
  
  async def send_on_actual_channel(self, text):
    await self.message.channel.send(text)

  

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


keep_alive()
print("TOKEN", os.getenv("TOKEN"))
client.run(os.getenv("TOKEN"))