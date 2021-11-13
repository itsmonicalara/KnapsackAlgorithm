from item import Item
# Backpack needs capacity, an optimal value, and a list of accepted items.
class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.total = 3
        self.opt_value = 0
        self.items = []

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def opt_value(self):
        return self._opt_value

    @opt_value.setter
    def opt_value(self, opt_value):
        if opt_value < 0:
            raise ValueError('Optimal value must be positive')    
        else:
            self._opt_value = opt_value
        
    def __str__(self):
        return f'''Backpack with capacity of : {self.capacity} 
                \n Optimal Value of : {self.opt_value} 
                \n List of itmes : {[str(i) for i in self.items]}'''
