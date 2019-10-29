from random import choices, choice, randint
from time import sleep
from string import ascii_letters, punctuation

from .point import Vector2
from .pixel import Pixel
from .output import print_at, clear_screen
from .terminal_size import get_terminal_size
from .curser_control import show, hide


class Rain:
    def __init__(self, width, height, length, idx=None, x=None, y=None):
        self.width = width
        self.height = height
        self.length = length
        self.loc_options = (idx, x, y)
        self.make_points()
        self.loc = iter(self.points)
        self.tail = []

    def make_points(self):
        x, y = self.get_loc()
        self.points = ((x, y) for y in range(y, self.height + 1))

    def get_loc(self):
        idx, x, y = self.loc_options
        if idx is not None:
            return idx % self.width, idx // self.width
        elif x is not None and y is None:
            return x, 0
        elif x is not None and y is not None:
            return x, y
        else:
            raise f"idx or x is needed to construct Rain."

    def update(self):
        try:
            point = next(self.loc)
            self.tail.append(point)
            if len(self.tail) == self.length:
                tail = self.tail.pop(0)
            else:
                tail = None
        except StopIteration:
            if len(self.tail) != 0:
                point = None
                tail = self.tail.pop(0)
            else:
                point = None
                tail = None
        return point, tail


class Screen:
    def __init__(self, width, height, amount=20, max_rain=(5, 10)):
        self.dim = Vector2(width, height)
        self.amount = amount
        self.max_rain = max_rain
        self.rain = [
            Rain(width, height, self.tail_len(), idx=self.ran_loc(anywhere=True))
            for _ in range(self.amount)
        ]

    def render(self):
        hide()
        clear_screen()
        try:
            while True:

                for index, rain in enumerate(self.rain):
                    point, tail = rain.update()

                    if point is None and tail is None:
                        self.rain.pop(index)
                        self.rain.append(
                            Rain(
                                self.dim.x,
                                self.dim.y,
                                self.tail_len(),
                                idx=self.ran_loc(),
                            )
                        )
                    if point is not None:
                        x, y = point
                        print_at(Pixel(self.get_letter(), None, fg="green"), x, y)
                    if tail is not None:
                        x, y = tail
                        print_at(" ", x, y)
                sleep(0.1)
        except Exception as e:
            print(e)
        finally:
            clear_screen()
            show()

    def tail_len(self):
        low, high = self.max_rain
        return randint(low, self.dim.y - high)

    def ran_loc(self, anywhere=False):
        if anywhere:
            return randint(1, self.dim.x*self.dim.y)
        else:
            return randint(0, self.dim.x)

    @staticmethod
    def rotated(array_2d):
        list_of_tuples = zip(*array_2d[::-1])
        return [list(elem) for elem in list_of_tuples]

    @staticmethod
    def get_letter():
        return choice(ascii_letters + punctuation)


