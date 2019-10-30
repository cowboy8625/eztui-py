from random import choices, choice, randint
from time import sleep
from string import ascii_letters, punctuation

from .point import Vector2
from .pixel import Pixel
from .output import print_at, clear_screen
from .terminal_size import get_terminal_size
from .curser_control import show, hide


def safe_run(func):
    clear_screen()
    hide()
    try:
        func()
    except:
        pass
    finally:
        clear_screen()
        show()


def ran_color():
    return choice(
        [
            # "red",
            "green",
            # "yellow",
            # "blue",
            # "magenta",
            # "cyan",
            # "white",
            # "bright black",
            # "bright red",
            # "bright yellow",
            "bright green",
            # "bright blue",
            # "bright magenta",
            # "bright cyan",
            # "bright white",
        ]
    )


class Rain:
    def __init__(self, width, height, length, idx=None, x=None, y=None, color="green"):
        self.width = width
        self.height = height
        self.length = length
        self.loc_options = (idx, x, y)
        self.color = color
        self.last = None
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
        return point, tail, self.color

    def last_update(self, char, point):
        if point is None:
            self.last = None
        else:
            x, y = point
            self.last = (char, x, y)


class Screen:
    def __init__(
        self, width=10, height=20, fullscreen=True, amount=20, max_rain=(9, 5)
    ):
        self.dim = Vector2(width, height)
        self.fullscreen = fullscreen
        self.check_screen_size()
        self._amount = amount
        self.amount = self._set_amount()
        self.max_rain = max_rain
        self.rain = [
            Rain(
                self.dim.x,
                self.dim.y,
                self.tail_len(),
                idx=self.ran_loc(anywhere=True),
                color=ran_color(),
            )
            for _ in range(self.amount)
        ]

    def _set_amount(self):
        if self._amount == "half":
            return self.dim.x // 2
        else:
            return self._amount

    def check_screen_size(self):
        resized = False
        if self.fullscreen:
            width, height = get_terminal_size()
            if width != self.dim.x:
                self.dim.x = width
                resized = True
            if height != self.dim.y:
                self.dim.y = height
                resized = True
            if resized:
                clear_screen()

    def render(self):
        pre_points = []
        while True:

            self.check_screen_size()

            for index, rain in enumerate(self.rain):
                point, tail, color = rain.update()
                c = self.get_letter()
                if point is None and tail is None:
                    self.rain.pop(index)
                    self.rain.append(
                        Rain(
                            self.dim.x,
                            self.dim.y,
                            self.tail_len(),
                            idx=self.ran_loc(),
                            color=ran_color(),
                        )
                    )
                if point is not None:
                    x, y = point
                    print_at(Pixel(c, None, fg="bright white"), x, y)

                if rain.last is not None:
                    k, x, y = rain.last
                    print_at(Pixel(k, None, fg=color), x, y)

                if tail is not None:
                    x, y = tail
                    print_at(" ", x, y)
                rain.last_update(c, point)

            sleep(0.1)

    def tail_len(self):
        low, high = self.max_rain
        return randint(low, self.dim.y - high)

    def ran_loc(self, anywhere=False):
        if anywhere:
            return randint(1, self.dim.x * self.dim.y)
        else:
            return randint(0, self.dim.x)

    @staticmethod
    def rotated(array_2d):
        list_of_tuples = zip(*array_2d[::-1])
        return [list(elem) for elem in list_of_tuples]

    @staticmethod
    def get_letter():
        return choice(ascii_letters + punctuation)

