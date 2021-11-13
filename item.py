# Que el Item tenga de propiedades su valor, su peso y su nombre.
class Item:
    def __init__(self, weight, value, name):
        self.weight = weight
        self.value = value
        self.name = name

    def __str__(self):
        return f'Item {self.name}, with weight: {self.weight} and value: {self.value}'

    def get_info(self):
        return [self.weight, self.value, self.name]
    

