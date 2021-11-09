# Y la Mochila que tenga de propiedades su capacidad, su valor óptimo
class Backpack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.opt_value = 0
        self.items = []