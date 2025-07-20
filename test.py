class Animal:
    def __init__(self):
        print("Animal Created")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Created")

d=Dog()
