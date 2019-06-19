from abc import ABC, abstractmethod
from dataclasses import dataclass
from os import name, system
from sys import stdout
from time import sleep
from types import FunctionType, MethodType

from .vectors import Index, Point


class Window:
    """
    Display manager Window

    Base class to use the methods win_*
    """

    def win_pack(self, item):
        self.win_clear()
        stdout.writelines(item + "\n")

    def win_clear(self):
        system("cls" if name == "nt" else "clear")


class Grid:
    """
    Geometry manager Grid.

    Base class to use the methods grid_* in every widget.
    >>> grid = Grid()
    >>> grid
    ░░░░░
    ░░░░░
    ░░░░░
    ░░░░░
    ░░░░░
    
    """

    def __init__(self, cols=5, rows=5, char=" "):  # chr(9617)
        self.size = Point(cols, rows)
        self.char = char
        self.grid_construct_grid()

    def __repr__(self):
        return "Grid()"

    def __str__(self):
        return self._grid

    def grid_construct_grid(self):
        self._grid = "".join([self.char * self.size.x + "\n"] * self.size.y)[0:-1]

    def grid_clear(self):
        if hasattr(self, "_grid"):
            self.grid_construct_grid()

    def grid_parse(self):
        self._grid = [list(i) for i in list(self._grid.split("\n"))]

    def grid_list_to_string(self):
        self._grid = "".join([i + "\n" for i in ["".join(i) for i in self._grid]])[0:-1]

    def grid_get_index(self):
        step = self.size.x
        total = self.size.x * self.size.y
        return self.__get_index_list(total, step)

    @staticmethod
    def __get_index_list(total, step):
        result = []
        t = list(range(total))
        for _ in range(total // step):
            result.append(list(t[0:step]))
            for _ in range(step):
                t.pop(0)
        return result


class Shape:

    """
    Shape Factory
    use type_of
    """

    @staticmethod
    def type_of(root, of_type):
        of_type = of_type.lower()
        if of_type == "square":
            return Square(root)
        elif of_type == "rectangle":
            return Rectangle(root)


class BaseShape(Grid, ABC):
    """
    Base Class

    Description:
    -----------
        Hold all info for making a basic shape.

    Parameters
    ----------
        root: Frame
            takes frame object to place all Shapes on.

        FROM GRID
        ---------
        cols: int = 5
            aka how width the screen will be.
        rows: int = 5
            aka how tall/height the screen will be
        char: chr, str = chr(9617)
            aka what is the place holder.
            can be a space ' '.

        
    """

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

    def __init__(self, root=None, style=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.shape_points = None
        self.start_point = Point(1, 1)
        self.style = style

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

    def _get_char(self, name):
        return self.ELEMENTS[name][self.style]

    def _get_outline_index_list(self):

        s_cell = Index(self.root, self.start_point)
        e_point = Point((self.start_point.x + self.size.x), self.start_point.y)
        e_cell = Index(self.root, e_point)
        first_row = [list(range(s_cell.index, e_cell.index))]
        self.index_list = self._get_inner_shape_index_list(first_row)

    def _get_inner_shape_index_list(self, row):
        for i in range(self.size.y - 1):
            row.append(self._add_to_list(row[-1], self.root.size.x))
        return row

    def top_line(self):

        for idx in self.index_list[0]:
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self._get_char("hBoarder")
            del line_point

    def bottom_line(self):

        for idx in self.index_list[-1]:
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self._get_char("hBoarder")
            del line_point

    def right_line(self):

        for idx in self.__get_vertical_index_list(self.index_list, -1):
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self._get_char("vBoarder")
            del line_point

    def left_line(self):

        for idx in self.__get_vertical_index_list(self.index_list, 0):
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self._get_char("vBoarder")
            del line_point

    def add_corners(self):
        top_left, top_right, bottom_left, bottom_right = self.get_corner_index()

        p1 = Point().fromIndex(self.root, top_left)
        self.root._grid[p1.y][p1.x] = self._get_char("ltCorner")

        p2 = Point().fromIndex(self.root, top_right)
        self.root._grid[p2.y][p2.x] = self._get_char("rtCorner")

        p3 = Point().fromIndex(self.root, bottom_left)
        self.root._grid[p3.y][p3.x] = self._get_char("lbCorner")

        p4 = Point().fromIndex(self.root, bottom_right)
        self.root._grid[p4.y][p4.x] = self._get_char("rbCorner")

    def get_corner_index(self):
        top_left = self.index_list[0][0]
        top_right = self.index_list[0][-1]
        bottom_left = self.index_list[-1][0]
        bottom_right = self.index_list[-1][-1]
        return top_left, top_right, bottom_left, bottom_right

    @staticmethod
    def __get_vertical_index_list(grid, index):
        return [line[index] for line in grid]

    @staticmethod
    def _add_to_list(cells, step):
        """Takes in list and step number and adds step number to each list item"""
        return [(num + step) for num in cells]


class Square(BaseShape):
    """
    Description:
    -----------
        Draws a Square in a Frame.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size.mul("x", 2.5)

    def resize(self, width, height):
        self.size = Point(round(width * 2.5), height)

    def _draw(self):
        self._get_outline_index_list()
        self.root.grid_parse()
        self.top_line()
        self.bottom_line()
        self.right_line()
        self.left_line()
        self.add_corners()
        del self.index_list
        self.root.grid_list_to_string()


class Rectangle(BaseShape):
    """
        Description:
    -----------
        Draws a Rectangle in a Frame.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _draw(self):
        self._get_outline_index_list()
        self.root.grid_parse()
        self.top_line()
        self.bottom_line()
        self.right_line()
        self.left_line()
        self.add_corners()
        del self.index_list
        self.root.grid_list_to_string()


class Boarder(BaseShape):
    """
    Boarder class is to handle construction of 
    boarder lines around the widget class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def place_at(self):
        raise NotImplemented

    def resize(self, width, height):
        raise NotImplemented

    def _draw(self):
        self.root.grid_parse()
        self.index_list = self.root.grid_get_index()
        self.top_line()
        self.bottom_line()
        self.right_line()
        self.left_line()
        self.add_corners()
        del self.index_list
        self.root.grid_list_to_string()


class Widget(Grid, Window):
    """
    Base class for all widgets
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pack(self):
        self.win_pack(self._grid)


class Label(Widget):
    """
    For Placing basic text.

    Parameters
    ----------
        root: Frame = None
            takes Frame object as master/root

        cols: int = 5
            aka how width the screen will be.

        rows: int = 5
            aka how tall/height the screen will be
        
        char: chr, string, int = chr(9608)
            aka what is the place holder.
            can be a space ' '.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MessageBox(Widget):
    """
    Pops up in middle of master/root Frame to display alert messages.

    Parameters
    ----------
        root: Frame = None
            takes Frame object as master/root

        cols: int = 10
            aka how width the screen will be.

        rows: int = 5
            aka how tall/height the screen will be
        
        char: chr, string, int = chr(9608)
            aka what is the place holder.
            can be nothing.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Frame(Widget):
    """
    Master window class

    All Widget type objects will be held in Frame class
    
    Parameters
    ----------
        style : int = 0
            3 styles to choose from.
        root: Frame = None
            takes frame object only if Frame is a Child.

        cols: int = 5
            aka how width the screen will be.

        rows: int = 5
            aka how tall/height the screen will be
        
        char: chr, string, int = chr(9608)
            aka what is the place holder.
            can be nothing.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_boarder()

    def init_boarder(self):
        self.boarder = Boarder(self)
        self.boarder.pack()

    def clear(self):
        self.grid_clear()
        self.init_boarder()


@dataclass
class Event:
    time_of: float
    method: FunctionType or MethodType


class Tui(Frame):
    """
    Base class for handling internal functions
    """

    TICKS = 0.1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 0.0
        self.events = []

    def after(self, delay, func):
        delay = self.add_float(delay, self.count)
        event = Event(delay, func)
        self.events.append(event)

    def window_geometry(self, *, rows=None, cols=None):
        """Sets the Size of the bass Frame"""
        self.size.reset(rows, cols)
        self.grid_construct_grid()
        self.boarder.pack()

    def _exc(self):
        ran_methods = 0
        for event in self.events:
            if event.time_of == self.count:
                event.method()
                ran_methods += 1
        if ran_methods != 0:
            self.events = self._del_old_events()

    def _del_old_events(self):
        result = []
        for event in self.events:
            if event.time_of > self.count:
                result.append(event)
        return result

    def advance_count(self):
        self.count = self.add_float(self.count, self.TICKS)

    def mainloop(self):
        while True:
            self.pack()
            self.advance_count()
            self._exc()
            sleep(self.TICKS)

    @staticmethod
    def add_float(num1, num2):
        return round(num1 + num2, 1)
