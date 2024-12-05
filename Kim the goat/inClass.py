class  Cat3:
    name = "Quack Quack"

    def __init__(self, name):
        self.cat_name = name

    def get_name(self):
        print(self.name)

my_cat = Cat3("Meow Meow")
my_cat.get_name()