# Que el Item tenga de propiedades su valor, su peso y su nombre.
class Item:
    def __init__(self, weight, value, name):
        self.weight = weight
        self.value = value
        self.name = name

    def __repr__(self):
        string = "Weight: {}\nValue: {}\nName: {}\n".format(self.weight, self.value, self.name)
        return string


if __name__ == "__main__":
    item = Item(10, 5, "Acta de nacimiento")
    print(item)

