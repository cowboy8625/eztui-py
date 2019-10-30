from time import sleep

from .frame import Frame
from .point import Vector2
from .output import print_at, clear_screen


def add_float(num1, num2):
    return round(num1 + num2, 1)


class Token:
    def __init__(self, delay, func):
        self.delay = delay
        self.step = delay
        self.func = func

    def update(self):
        self.delay = add_float(self.delay, self.step)


class Tui(Frame):
    """
    Base class for handling internal functions
    """

    TICKS = 0.1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.dim == Vector2(5, 5):
            self.dim = Vector2(50, 25)
        self.count = 0
        self.previous_grid = None
        self.events = []

    def check_render(self, current, previous):
        if previous is not None:
            grid = "\n".join(("".join((str(w) for w in h)) for h in self.grid))
            print_at(grid, self.pos.x + self.dim.x + 5, self.pos.y)
            if current != previous:
                self.render()
                self.previous_grid = current
        else:
            self.render()
            self.previous_grid = current

    def after(self, delay, func):
        self.events.append(Token(delay, func))

    def advance_count(self):
        self.count = add_float(self.count, self.TICKS)

    def check_for_events(self):
        for event in self.events:
            if event.delay == self.count:
                event.func()
                event.update()

    def mainloop(self):
        clear_screen()
        while True:

            self.render()
            self.check_for_events()
            # self.check_render(self.grid, self.previous_grid)
            self.advance_count()
            sleep(self.TICKS)

