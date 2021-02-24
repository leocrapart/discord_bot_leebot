import re

async def print_command_and_args(message):
  command = get_command(message)
  args = get_args(message)
  if command:
    await message.channel.send(f"command => {command}", message)
  if args:
    await message.channel.send(f"args => {args}", message)


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

