import functools
class Knapsack:
    def __init__(self, capacity,n):
        self.capacity = capacity
        self.total = n
        self.opt_value = 0
        self.items = []
        self.discarded_items = []
        self.weight_used = 0
        self.free_weight = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity is not int:
            capacity = int(capacity)
        self._capacity = capacity

    @property
    def opt_value(self):
        return self._opt_value

    @opt_value.setter
    def opt_value(self, opt_value):
            self._opt_value = opt_value

    
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        if total is not int:
            total = int(total)
        if total <= 0:
            raise ValueError('Optimal value must be positive')    
        else:
            self._total = total

    def pack_unpack_items(self, items, table):
        res = self.opt_value
        capacity = self.capacity
        for i in range(self.total, 0, -1):
            if res <= 0:
                break
            if res == table[i - 1][self.capacity]:
                continue
            else:
                # Just in case we need weight and values of selected items
                self.items.append(items[i-1])
                res = res - items[i - 1].value
                capacity = capacity - items[i - 1].weight
        
        for o_item in items:
            if o_item not in self.items:
                self.discarded_items.append(o_item)

        self.weight_used = functools.reduce(lambda a, b: a+b, 
                                            list(map(lambda x: x.weight, self.items)))   

        self.free_weight = self.capacity - self.weight_used     

    def __str__(self):
        return f'''Backpack with capacity of : {self.capacity}
        \nTotal items to manage: {self.total}
        \nOptimal Value of : {self.opt_value} 
        \nPacked items : {[str(i) for i in self.items]}
        \nDiscarded items : {[str(i) for i in self.discarded_items]}
        \nWeight occupied : {self.weight_used}'''
