items = {}


class Item:
    item_name = ""
    item_description = ""

    def __init__(self, id, item_name, item_description):
        self.id = id
        self.item_name = item_name
        self.item_description = item_description

    def get_id(self):
        return self.id


items[0] = Item("sword", "Sword", "This sword can totally kill zombies n that")


def get_item(item_id):
    return items.get(item_id)
