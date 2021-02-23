from tinydb import TinyDB, Query

db = TinyDB("db.json")



def add_xp_to_player(player_name, xp_amount):
  res = db.search(Query().name == player_name)
  player = res[0]
  new_xp = player["xp"] + xp_amount
  db.update({"xp": new_xp}, Query().name == player_name)
  