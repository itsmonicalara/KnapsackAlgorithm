from item import *
# Y la Mochila que tenga de propiedades su capacidad, su valor óptimo
class Backpack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.opt_value = 0
        self.list_items = []

    # Add choosen items to the items list
    def add_item(self, list):
        self.list_items = list
        return self.list_items

    
    # Get items in the backpack
    def get_items(self):
        print("The choosen items are: ", self.list_items)

if __name__ == "__main__":
    backpack = Backpack(10)
    my_list = [[30, 120], [20, 100]]
    backpack.add_item(my_list)
    backpack.get_items()
