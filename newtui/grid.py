from os import system, name
from sys import stdout

##-- Module Imports --##
from .charsheet import Pixel
from .point import Point

PIX = Pixel()

class Grid:
    '''
    Discription:
    Is a 2D Matrix that holds all the values of the screen  
    Class Window: Base
    Method accsess: grid_*

    width: default = 10, set width of screen in font characters.
    height: default = 10, set height of screen in font characters.
    char: default = ' ' empyty space, set the character used for background.
    '''

    def __init__(self, width=10, height=10, char=PIX.shade_one, start_loc=(0,0)):
        self._size = Point(width, height)
        self._start = Point(start_loc[0]+1, start_loc[1]+1)
        self.char = char
        self._grid = self.construct_grid()
        self.style = 1

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, grid):
        self._grid = grid

    @property
    def size_x(self):
        return self._size.x

    @size_x.setter
    def size_y(self, x):
        self._size.x = x

    @property
    def size_y(self):
        return self._size.y

    @size_y.setter
    def size_y(self, y):
        self._size.y = y

    @property
    def startX(self):
        return self._start.x

    @startX.setter
    def startX(self, x):
        self._start.x = x

    @property
    def startY(self):
        return self._start.y

    @startY.setter
    def startY(self, y):
        self._start.y = y

    def change_location(self, x, y):
        self._start = Point(x, y)

    def construct_grid(self):
        return [self.char * self._size.x] * self._size.y

    def parser(self):
        self._grid = [list(i) for i in self._grid]

    def unparser(self):
        self._grid = ["".join(i) for i in self._grid]

    def insert_at(self, x, y, char):
        self.parser()
        self._grid[y][x] = char
        self.unparser()

    def render(self):
        x = self.startX
        y = self.startY
        for line in self._grid: 
            stdout.write(f"\x1b7\x1b[{y};{x}f{line}\x1b8")
            y += 1 
        stdout.flush()

    def clear_grid(self):
        self._grid = self.grid_construct_grid()

    def clear_screen(self):
        system("cls" if name == "nt" else "clear")


