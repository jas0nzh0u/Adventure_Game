class Map:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def get_room(self, name):
        return self.rooms.get(name)

    def connect_rooms(self, room1_name, direction, room2_name):
        room1 = self.get_room(room1_name)
        room2 = self.get_room(room2_name)

        if room1 and room2:
            room1.connect(direction, room2)
