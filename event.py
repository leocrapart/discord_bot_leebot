connections = {}

def connect(event, func):
    if not event in connections:
        connections[event] = []
    connections[event].append(func)

def trigger(event, args=None):
    if not event in connections:
        return

    for func in connections[event]:
        func()


print("connections", connections)

def print_yeah():
    print("yeah")

connect("player_level_up", print_yeah)


print("connections", connections)

trigger("player_level_up")

