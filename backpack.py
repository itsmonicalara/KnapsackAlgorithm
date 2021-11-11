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

    # Add choosen items to the items list
    def add_items(self, list):
        self.list_items = list
        return self.list_items
    
    # Get items in the backpack
    def get_items(self):
        print("You should take these items with you: ", self.list_items)

    # Method to enter item values into different lists
    def new_format(self, item):
        self.weight_list.append(item.weight)
        self.values_list.append(item.value)
        self.names_list.append(item.name)
  
        return(self.weight_list, self.values_list, self.names_list)



if __name__ == "__main__":
    # n = 3
	# capacity = 50
	# weight = [10, 20, 30]
	# value = [60, 100, 120]

    backpack = Backpack(50)
    n = int(input("How many items do you want to choose? "))
    for i in range(n):
        name = input("Enter the name of the item: ")
        weight = int(input("Enter the weight of the item: "))
        value = int(input("Enter the value of the item: "))
        item = Item(weight, value, name)
        backpack.new_format(item)
    # item1 = Item(10, 60, "Acta de nacimiento")
    # item2 = Item(20, 100, "Agua")
    # item3 = Item(30, 120, "Medicinas")     


    # my_list = [[30, 120], [20, 100]]
    # backpack.add_items(my_list)
    # backpack.get_items()
