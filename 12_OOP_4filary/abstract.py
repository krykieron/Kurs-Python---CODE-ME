from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def sides(self):
        pass


class Square(Shape):
    def __init__(self):
        print("Powstał kwadrat ")

    def sides(self):
        print("4 sides")


class Triangle(Shape):
    def sides(self):
        print("3 sides")


kwadrat = Square()
kwadrat.sides()

trojkat = Triangle()
trojkat.sides()