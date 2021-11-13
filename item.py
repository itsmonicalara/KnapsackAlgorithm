# Que el Item tenga de propiedades su valor, su peso y su nombre.
class Item:
    def __init__(self, weight, value, name):
        self.weight = weight
        self.value = value
        self.name = name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight <= 0:
            raise ValueError('Weight must be positive')    
        else:
            self._weight = weight

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError('Value must be positive')    
        else:
            self._value = value

    def __str__(self):
        return f'Item {self.name}, with weight: {self.weight} and value: {self.value}'

  

