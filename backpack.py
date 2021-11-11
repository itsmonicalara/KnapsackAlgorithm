from item import *
# Backpack needs capacity, an optimal value, and a list of accepted items.
class Backpack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.opt_value = 0
        self.list_items = []
        self.weight_list = []
        self.values_list = []
        self.names_list = []
    
    # Get items in the backpack
    def get_items(self):
        print("You should take these items with you: ", self.list_items)

    # Method to enter item values into different lists
    def new_format(self, item):
        self.weight_list.append(item.weight)
        self.values_list.append(item.value)
        self.names_list.append(item.name)
  
        return(self.weight_list, self.values_list, self.names_list)

        

