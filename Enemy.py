from enum import Enum


class Enemy:

    # Initialise with an id, and an EnemyType
    def __init__(self, id, type):
        self.id = id
        self.type = type

        # Assign starting attributes from the EnemyType enum
        values = type.value
        self.name = values[0]
        self.health = values[1]
        self.description = values[2]

    def fight(self, player, damage):
        if damage > self.health:
            pass
            # Enemy dies
        else:
            # Damage is applied
            self.health -= damage

            # Example message:
            # The Zombie has been damaged!
            # 100hp ➡ 50hp

            print("The " + self.name + " has been damaged!")
            print((self.health+damage) + "hp ➡ " + self.health + "hp")
    #Returning the value of health when it needs to be called
    def get_health(self):
        return self.health


class Enemy_Type(Enum):
    # ( EnemyName, StartingHealth, Description )
    ZOMBIE = ("Zombie", 100, "An undead warrior")
    ARMORED_ZOMBIE = ("Armored Zombie", 150, "An undead warrior with armor")
    SKELETON = ("Skeleton", 50, "Raised from the dead")
    SLIME = ("Slime", 25, "Is this minecraft?")
