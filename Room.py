import Item


class Room:

    def __init__(self, name):
        self.name = name
        self.connections = {'north': None, 'south': None, 'east': None, 'west': None}
        self.items = []
        self.enemies = []

    def get_name(self):
        return self.name
    
    def get_connections(self):
    # returns entire dict for directions
        return self.connections
    
    def get_items(self):
        return self.items

    #
    # CONNECTIONS
    #

    def connect(self, direction, room):
        self.connections[direction] = room
        room.connections[get_opposite_direction(direction)] = self

    def print_string_connections(self):

        for direction, room in self.connections.items():
            if room is None:
                continue
            print(direction.upper() + " -> " + room.get_name())

    #
    # ITEMS
    #

    def add_item(self, item_id):
        self.items.append(Item.get_item(item_id))

    def get_string_items(self):
        return_string = ""
        for item in self.items:
            return_string += item.item_name + ", "

        return return_string[:-2]

    #
    # ENEMIES
    #

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def get_string_enemies(self):
        enemy_types = {}
        return_string = ""

        for enemy in self.enemies:
            if enemy.type in enemy_types.keys():
                current_amount = enemy_types.get(enemy.type)
                enemy_types[enemy.type] = current_amount+1
            else:
                enemy_types.update({enemy.type: 1})

        for enemy_type in enemy_types.keys():
            amount = enemy_types[enemy_type]

            if amount == 1:
                return_string += "a " + enemy_type.value[0]
            elif amount > 1:
                return_string += str(amount) + " " + enemy_type.value[0] + "s"

            return_string += ", "

        return return_string


def get_opposite_direction(direction):
    opposites = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
    return opposites[direction]
