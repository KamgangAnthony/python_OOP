class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("Getter called")
        return self._items

    @items.setter
    def items(self, new_items):
        print("setter called")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Enter a valid list")

my_bag = Backpack()
my_bag.items = ["list of bags"]
print(my_bag.items)