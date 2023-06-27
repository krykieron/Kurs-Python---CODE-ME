from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def travel(self):
        pass

    @abstractmethod
    def poop(self):
        pass


class Horse(Animal):
    def travel(self):
        print("Ride with speed 20km/h")

    def poop(self):
        return '💩'


class Unicorn(Animal):
    def travel(self):
        print("I can fly..... frrryyy")

    def poop(self):
        return '🌈'


def move(animal: Animal):
    print(type(animal).__name__)
    animal.travel()
    print(animal.poop())

arrow = Horse()
cute = Unicorn()

move(arrow)
move(cute)

