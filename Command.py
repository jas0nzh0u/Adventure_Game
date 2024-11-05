import re

from Player import Player

from Enemy import Enemy

import random

def normalize_command(text):
    # Will convert text to lowercase and remove punctuation
    normalized_text = re.sub(r'[^\w\s]', '', text.lower())
    return normalized_text


def extract_action_word(normalized_text):
    # Split the text into words
    words = normalized_text.split()  # .toList()

    # All possible actions
    action_words = ['move', 'go', 'take', 'use', 'look', 'drop', 'inventory', 'i', 'attack']

    # Find the action word
    action = next((word for word in words if word in action_words), None)

    if action:
        words.remove(action)

    return action, words


rooms = []


def run_command(command, roomsList, player):
    global rooms
    rooms = roomsList

    normalized_command = normalize_command(command)
    action_word, otherwords = extract_action_word(normalized_command)
    if action_word:
        print(f"Action: {action_word}")

        if action_word == "go" or action_word == "move":
            run_go_command(otherwords, player)
        if action_word == "take":
            run_take_command(otherwords, player)
        if action_word == "drop":
            run_drop_command(otherwords, player)
        if action_word == "inventory" or action_word == "i":
            run_inventory_command(player)
        if action_word == "attack":
            run_attack_command(otherwords, player)
    else:
        print("Invalid command.")


def run_go_command(words, player):
    destination = None
    string_conversion = ""

    for x in words:
        string_conversion += "" + x 
        # converts the list variable into string so directions can also be used

    for key, value in player.get_room().get_connections().items(): 
    # for keys and values in dict of connections
        if key == string_conversion and value != None: 
        # if command given = direction and has value
            return player.set_room(player.get_room().get_connections()[key]) 
            # assigns rooms appropriately

    for room in rooms.keys():
        if room.lower() in words:
            destination = room

    if destination is None:
        print("Room not found!")
    else:
        return player.set_room(rooms[destination])

def run_take_command(words, player):
    string_conversion = ""

    for x in words:
        string_conversion += "" + x 
        # converts the list variable into string so directions can also be used

    for item in player.get_room().get_items():
    # for items in the room
        if item.get_id() == string_conversion:
        # if command given = item
            player.add_item(item)
            player.get_room().get_items().remove(item)
            # adds item to inventory and removes item from room

def run_drop_command(words, player):
    string_conversion = ""

    for x in words:
        string_conversion += "" + x 
        # converts the list variable into string so directions can also be used

    for item in player.get_inventory():
    # for items in player's inventory
        if item.get_id() == string_conversion:
        # if command given = item
            player.get_room().get_items().append(item)
            player.get_inventory().remove(item)
            # removes item from inventory and adds item to room

def run_inventory_command(player):
    return_string = ""
    for item in player.get_inventory():
        return_string += item.item_name + ", "
    if return_string == "":
        print("You have nothing in your inventory")
    else:
        print("You have:", return_string[:-2])

def run_attack_command(enemy, player):

    #Randomised damage the enemy is taking
    damage = random.randint(0, 10)
    enemy = Enemy

    #Check if enemy is alive
    if enemy.get_health > 0:
        #Calling the enemy fight method
        enemy.fight(damage)
    #Check if player is alive
    if player.get_health > 0:
        #Calling the players fight method
        player.fight(damage)
        
