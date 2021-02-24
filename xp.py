from tinydb import TinyDB, Query

db = TinyDB("db.json")



def add_xp_to_player(player_name, xp_amount):
  res = db.search(Query().name == player_name)
  player = res[0]
  new_xp = player["xp"] + xp_amount
  db.update({"xp": new_xp}, Query().name == player_name)
  


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