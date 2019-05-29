from abc import ABC, abstractmethod

from .matrix import Matrix
from .window import Window
from .vector import Vector

class Shape(ABC):

    ELEMENTS = {
        'hBoarder': [chr(9552), chr(9472), chr(9473)],
        'vBoarder': [chr(9553), chr(9474), chr(9475)],
        'rTee': [chr(9568), chr(9500), chr(9507)],
        'lTee': [chr(9571), chr(9508), chr(9515)],
        'tTee': [chr(9574), chr(9516), chr(9523)],
        'bTee': [chr(9577), chr(9524), chr(9531)],
        'rtConner': [chr(9559), chr(9582), chr(9491)],
        'ltConner': [chr(9556), chr(9581), chr(9487)],
        'rbConner': [chr(9565), chr(9583), chr(9499)],
        'lbConner': [chr(9562), chr(9584), chr(9495)],
        'cross': [chr(9580), chr(9532), chr(9547)]
        }

    def __init__(self, array2d, size, place_at):
        self.array2d = array2d
        self.size = size
        self.cords = Vector(place_at[0], place_at[1])

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def outline(self):
        pass


class Square(Shape):

    def __init__(self, array2d, size, place_at):
        super().__init__(array2d, size, place_at)

    def make_square(self):
        pass

    def outline(self, style):
        pass

    def draw(self, style):
        line1 = [
            self.ELEMENTS['ltConner'][style] + 
            (self.ELEMENTS['hBoarder'][style] * (self.size - 2)) + 
            self.ELEMENTS['rtConner'][style]
            ]
        lastLine = [
            self.ELEMENTS['lbConner'][style] + 
            (self.ELEMENTS['hBoarder'][style] * (self.size - 2)) + 
            self.ELEMENTS['rbConner'][style]
            ]
        array2d = self.array2d._parse(self.array2d.array2d)

        for i in array2d:
            print(i)
        return 'awdadawd'



class Circle(Shape):

    def __init__(self, array2d, size, place_at):
        super().__init__(array2d, size, place_at)

    def draw(self):
        pass

class Rectangle(Shape):

    def __init__(self, array2d, size, place_at):
        super().__init__(array2d, size, place_at)

    def draw(self):
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()