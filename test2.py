class Animal:
    def shout(self):
        print("Animal Shouting")

    def walk(self):
        print("Animal is Walking")

class Dog(Animal):

    def speak(self):
        print("Dog Barking")


a1=Dog()
a1.speak()
a1.shout()
a1.walk()

#1. Object of Child Class always has access to Methods of Parents Class (Yes)
#2. Under What circumstances a child object will get error while calling parent method- When you dont use super init and use methods that need attributed from init functions









