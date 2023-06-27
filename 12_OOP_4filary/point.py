class Point:
    def __init__(self, value):
        self.__x = 0
        self.__y = 0
        self.value = value

    def get_x(self):
        return self.__x

    def set_x(self, move):
        self.__x = move



point1 = Point(3)
print(point1.value)
print(point1.get_x())
point1.set_x(5)
print(point1.get_x())