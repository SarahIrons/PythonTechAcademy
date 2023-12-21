"""
ABSTRACTION ASSIGNMENT
Create a class that utilizes the concept of abstraction.
Your class should contain at least one abstract method and one regular method.  
Create a child class that defines the implementation of its parents abstract method.
Create an object that utilizes both the parent and child methods.
 Add comments throughout your Python explaining your code.
Upload your code to GitHub."""
#this code example is taken from website--blog.teclado/"How to Write Cleaner Python Code Using Abstract Classes" #


from abc import ABC, abstractmethod
import datetime 

#abc is a built-in module; we have to import ABC and abstract method.
#Abstract class will force subclasses to implement all of its abstract methods. 
class Animal(ABC): #inherit from ABC(abstract base class)
    @abstractmethod #decorator to define an abstract method
    def feed(self):
        pass

class Panda(Animal): #if a class inherits from an ABC it must implement all its methods
    def feed(self): #the method's name must match the name of the ABC's method
        print("Feeding a panda some tasty bamboo!")
class Lion(Animal):
    def feed(self):
        print("Feeding a lion  with raw meat!")

class Snake(Animal):
    def feed(self):
        print("Feeding a snake with mice!")

zoo = [Lion(), Panda(), Snake()]

for animal in zoo:
    animal.feed() #this is a standard way to write the code for each of the three objects(animals)


class Animal(ABC):
    @property
    def food_eaten(self):
        return self.food_eaten
    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")
    @property
    @abstractmethod
    def diet(self):
        pass
    @abstractmethod
    def feed(self,time):
        pass
class Lion(Animal):
    @property 
    def diet(self):
        return["antelope","cheetah","buffalo"]
    def feed(self,time):
        print(f"Feeding a lion with {self._food} meat! At {time}")
class Snake(Animal):
    @property
    def diet(self):
        return["frog","rabbit"]
    def feed(self, time):
        print(f"Feeding a snake with {self._food} meat! At {time}")


#We can create 2 objects,set the food to feed them, then call the feed method. 

Leonardo = Lion()
Leonardo.food_eaten='buffalo'
Leonardo.feed("12:30 PM")
Arnold = Snake()
Arnold.food_eaten = 'frog'
Arnold.feed("3:00 PM")

#if you try to feed an animal something that it does not eat it will raise a value error:
Arnold = Snake()
Arnold.food_eaten= 'carrot'
Arnold.feed("9:00am")
