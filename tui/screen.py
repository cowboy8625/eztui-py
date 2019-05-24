from os import name, system

from .matrix import Matrix
from .window import Window


class Screen:

    WINDOW_LOCATIONS = {
        'controls' : [(0,11,20,20), 'Controls'],
        'map' : [(20,3,78,24), 'Map']
    }

    def __init__(self, width, height, char=' '):

        self.char = char
        self.array2d = Matrix(width, height, char)
        self.width = width
        self.height = height
        self.window_list = []



    def combat(self):
        pass

    def map(self):
        con_win = Window(self.WINDOW_LOCATIONS['map'][0],
        self.WINDOW_LOCATIONS['map'][1], chr(9608))
        self.window_list.append(con_win)

    def controls(self):
        con_win1 = Window(self.WINDOW_LOCATIONS['controls'][0],
        self.WINDOW_LOCATIONS['controls'][1], chr(9608))
        self.window_list.append(con_win1)


    def label(self):
        pass

    def render(self):
        for window in self.window_list:
            self.array2d.insert_window(window)

        self.clear()
        print(self.array2d)

    def clear(self):
        system('cls' if name == 'nt' else 'clear')
