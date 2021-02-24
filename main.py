import discord 
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
from tinydb import TinyDB, Query
import xp

load_dotenv()

db = TinyDB("db.json")

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  #await print_command_and_args(message)
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
    await self.listen_to_ayuken_command()
  
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
    raw_command = self.command2raw_command(command)
    if self.message_startswith(raw_command):
      await self.send_on_actual_channel(reply_text)

  def command2raw_command(self, command):
    prefix = self.command_prefix
    return prefix + command

  def message_startswith(self, command):
    return self.message.content.startswith(command)
  
  async def send_on_actual_channel(self, text):
    await self.message.channel.send(text)

  


def author_msg(message):
  if message.author == client.user:
    return


keep_alive()

client.run(os.getenv("TOKEN"))