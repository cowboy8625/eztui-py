from abc import ABC, abstractmethod

##-- Module Imports --##
from .grid import Grid
from .point import Point

##-- Shape classes --##

class Token:
    def __init__(self, root, char, col, row):
        self.char = char
        self.row = row
        self.col = col

    def __repr__(self):
        self.char = "SPACE" if self.char == " " else self.char
        return f"{self.char}: ({self.col}, {self.row})"


class Shape:

    """
    Shape Factory
    use type_of
    """

    @staticmethod
    def type_of(root, of_type):
        '''
        args:
        root: Frame
        of_type: str, OPTIONS: "rectangle", "square"
        '''
        if of_type.lower() == "square":
            return Square(root)
        elif of_type.lower() == "rectangle":
            return Rectangle(root)


class BaseShape(Grid, ABC):

    def __init__(self, root=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.shape_points = None
        self.start_point = Point(1, 1)
        self.style = root.style

    @abstractmethod
    def _draw(self):
        pass

    def resize(self, width, height):
        self.size = Point(width, height)

    def pack(self):
        """adds shape to gird"""
        self._draw()

    def move(self, x, y):
        self.start_point.x += x
        self.start_point.y += y
        self._draw()

    def place_at(self, x, y):
        self.start_point = Point(x, y)


class Square(BaseShape):

    RESIZE = 2.5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size.mul("x", self.RESIZE)
        self.grid_construct_grid()

    def resize(self, width, height):
        self.size = Point(round(width * self.RESIZE), height)

    def _draw(self):
        boarder = Boarder(self)
        boarder.pack()
        s = WindowSplicer(self.root, self)
        s.splice()


class Rectangle(BaseShape):
    """
        Description:
    -----------
        Draws a Rectangle in a Frame.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _draw(self):
        boarder = Boarder(self)
        boarder.pack()
        self.root.render()
        # s = WindowSplicer(self.root, self)
        # s.splice()


##-- Styling --##


class BoardStyle:

    ELEMENTS = {
        "hBoarder": [chr(9552), chr(9472), chr(9473)],
        "vBoarder": [chr(9553), chr(9474), chr(9475)],
        "lTee": [chr(9571), chr(9508), chr(9515)],
        "rTee": [chr(9568), chr(9500), chr(9507)],
        "tTee": [chr(9574), chr(9516), chr(9523)],
        "bTee": [chr(9577), chr(9524), chr(9531)],
        "ltCorner": [chr(9556), chr(9581), chr(9487)],
        "rtCorner": [chr(9559), chr(9582), chr(9491)],
        "lbCorner": [chr(9562), chr(9584), chr(9495)],
        "rbCorner": [chr(9565), chr(9583), chr(9499)],
        "lSlope": ["/", "/", "/"],
        "rSlope": ["\\", "\\", "\\"],
        "cross": [chr(9580), chr(9532), chr(9547)],
    }

    def __init__(self, style):
        self.style = style
        self.hBoarder = self.get_char("hBoarder")
        self.vBoarder = self.get_char("vBoarder")
        self.lTee = self.get_char("lTee")
        self.rTee = self.get_char("rTee")
        self.tTee = self.get_char("tTee")
        self.bTee = self.get_char("bTee")
        self.ltCorner = self.get_char("ltCorner")
        self.rtCorner = self.get_char("rtCorner")
        self.lbCorner = self.get_char("lbCorner")
        self.rbCorner = self.get_char("rbCorner")
        self.lSlope = self.get_char("lSlope")
        self.rSlope = self.get_char("rSlope")
        self.cross = self.get_char("cross")

    def get_char(self, name):
        return self.ELEMENTS[name][self.style]


##-- Boarder box drawer --##


class Boarder:
    """
    Boarder class is to handle construction of 
    boarder lines around the window class.
    """

    def __init__(self, root):
        self.root = root
        self.style = BoardStyle(root.style)

    def get_outline(self):
        grid = self.map_grid(self.root._grid)
        top = grid[0][1:-1]
        left = [i[0] for i in grid[1:-1]]
        right = [i[-1] for i in grid[1:-1]]
        bottom = grid[-1][1:-1]
        corners = [grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1]]
        return (top + bottom), (left + right), corners

    def map_grid(self, grid):
        result = []
        for idx1, line in enumerate(grid):
            result1 = []
            for idx2, char in enumerate(line):
                result1.append(Token(root=self.root, char=char, col=idx2, row=idx1))
            result.append(result1)
        return result

    def _draw(self):
        self.root.grid_parser()
        horizontal, vertical, corners = self.get_outline()
        cb = [
            self.style.ltCorner,
            self.style.rtCorner,
            self.style.lbCorner,
            self.style.rbCorner,
        ]
        self.stamp(horizontal, self.style.hBoarder)
        self.stamp(vertical, self.style.vBoarder)

        for spot, boarder in zip(corners, cb):
            self.root._grid[spot.row][spot.col] = boarder
        self.root.grid_unparser()

    def stamp(self, locations, style):
        for spot in locations:
            self.root._grid[spot.row][spot.col] = style

    def pack(self):
        self._draw()


