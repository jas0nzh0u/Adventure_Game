import random

from Command import run_command
from Enemy import EnemyType, Enemy
from Map import Map
from Player import Player
from Room import Room

player = None
game_map = None
inventory = []
name = input("Enter your name: ")

def setup_rooms():
    global game_map, player

    game_map = Map()
    room1 = Room("Reception")
    room2 = Room("Room2")
    room3 = Room("Room3")

    room1.add_item(0)

    game_map.add_room(room1)
    game_map.add_room(room2)
    game_map.add_room(room3)
    game_map.connect_rooms("Reception", "east", "Room2")
    game_map.connect_rooms("Room2", "south", "Room3")
    player = Player(room1, inventory, name, 100)
   


def spread_enemies():
    global game_map

    # Will spawn a randnom amount in the range for each enemytype

    enemies = []

    enemies.extend(spawn_enemies(EnemyType.ZOMBIE, random.randint(3, 8)))
    enemies.extend(spawn_enemies(EnemyType.ARMORED_ZOMBIE, random.randint(2, 4)))
    enemies.extend(spawn_enemies(EnemyType.SKELETON, random.randint(3, 5)))
    enemies.extend(spawn_enemies(EnemyType.SLIME, random.randint(1, 3)))

    # Now distribute the enemies randomly throughout the rooms
    for enemy in enemies:
        rooms = list(game_map.rooms.values())  # Convert dict_values to a list
        random_room = random.choice(rooms)  # Use random.choice to select a random room
        random_room.add_enemy(enemy)
        # print(f"DEBUG: {random_room.get_name()} has added a {enemy.id}")


def spawn_enemies(type, amount):
    enemies = []
    # Will spawn a "type" of enemy for each iteration
    for i in range(amount):
        # Will instantiate a new enemy
        # Enemy id will be the types name then the number, for example zombie_2
        enemies.append(Enemy(type.value[0].lower() + "_" + str(i), type))

    # Will return a list of the enemies
    return enemies


setup_rooms()
spread_enemies()


def print_current_room():
    global player
    print("You are currently in: " + player.get_room().get_name())
    if player.get_room().get_string_items() != "":
        print("In this room, there is: " + player.get_room().get_string_items())
    print("Watch out! In this room there is " + player.get_room().get_string_enemies())
    player.get_room().print_string_connections()


def print_menu():
    print_current_room()


while True:
    print_menu()
    run_command(input("What do you want to do? \n➡ "), game_map.rooms, player,)
    
