class Player:

    def __init__(self, starting_room, inventory, name, health):
        self.starting_room = starting_room
        self.inventory = inventory
        self.health = health
        self.name = name

    def get_room(self):
        return self.starting_room

    def set_room(self, destination):
        self.starting_room = destination

    def get_inventory(self):
        return self.inventory
    
    def add_item(self, item):
        self.inventory.append(item)
        
    def take_damage(self, damage):
        if damage >= self.health:
            print(self.name + " is dead")
            #Player dies
        else:
            # Damage is applied
            self.health -= damage

            # Example message:
            # Terrance has been damaged!
            # 100hp ➡ 50hp

            print("self.name + has been damaged!")
            print((self.health+damage) + "hp ➡ " + self.health + "hp")
    
    def get_health(self):
        return self.health
        