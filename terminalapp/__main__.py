##-- Imports --##

from abc import ABC, abstractmethod
from dataclasses import dataclass
from os import name, system
from sys import stdout
from time import sleep
from types import FunctionType, MethodType

##-- Custom Imports --##

from .vectors import Index, Point, TextPoint, GridPoint
from .keyboard import getchar
from .curser_control import hide, show
from .terminal_size import get_terminal_size
from .asciiesc import font, bg, fg

##-- Tokens --##


class Token:
    def __init__(self, root, char, col, row, index=None):
        self.char = char
        self.row = row
        self.col = col
        if index == None:
            self.index = Index(root, Point(col, row)).index
        else:
            self.index = index

    def __repr__(self):
        self.char = "SPACE" if self.char == " " else self.char
        return f"{self.char}: ({self.col}, {self.row})"


class CharToken:
    def __init__(self, char, fg=None, bg=None, font=None):
        self.char = char
        self.fg = fg
        self.bg = bg
        self.font = font
        self.color = ""
        self._set_color()

    def _set_color(self):
        if self.fg != None:
            self.color += self.fg
        elif self.bg != None:
            self.color += self.bg
        elif self.font != None:
            self.color += self.font

    def __str__(self):
        return f"{self.color}{char}{bg.reset}"

##-- Window Splicer --##


class WindowSplicer:
    """
    Splices a Child Widget onto a Root Widget
    """

    def __init__(self, root, child):
        self.root = root
        self.child = child
        self.index_list = None

    def splice(self):

        self._get_index_list()
        print(self.index_list)
        '''
        self.root.grid_parse()
        child_tp = GridPoint(self.child)
        # while child_tp.current_char != None:
        for idx in self.index_list:
            point = Point.fromIndex(self.root, idx)
            self.root._grid[point.y][point.x] = child_tp.current_char
            child_tp.advance()
        self.root.grid_list_to_string()
'''

    def _get_index_list(self):
        """gets all index valuse of location on root window"""
        s_cell = Index(self.root, self.child.start_point)
        e_point = Point(
            (self.child.start_point.x + self.child.size.x), self.child.start_point.y
        )
        e_cell = Index(self.root, e_point)
        first_row = [list(range(s_cell.index, e_cell.index))]
        self.index_list = self._get_child_idx_in_root(first_row)

    def _get_child_idx_in_root(self, row):

        for i in range(self.child.size.y - 1):
            row.append(self._add_to_list(row[-1], self.root.size.x))
        return sum(row, [])

    @staticmethod
    def _add_to_list(cells, step):
        """Takes in list and step number and adds step number to each list item"""
        return [(num + step) for num in cells]

##-- HighLighter --##

class HighLighter:
    '''
    For Placing basic text.

    Parameters
    ----------
        label: Label
            label to highlight over
        color: str
            black, red, green, yellow, blue, magenta, cyan, white
        row: int
            starting row
    '''
    def __init__(self, label, color='green'):
        self.label = label
        self.color = color

    def light_up(self, row):
        self.label._grid = bg.black + self.label._grid + bg.reset

##-- Window manager class --##


class Window:
    """
    Display manager Window

    Base class to use the methods win_*
    """

    def win_pack(self, item):
        self.win_clear()
        stdout.writelines(item + "\n")
        stdout.flush()

    def win_render_line(self, x, y, text):
        stdout.write(f"\x1b7\x1b[{y};{x}f{text}\x1b8")
        stdout.flush()
    
    def win_render_box(self, x, y, box):
        for line in box:
            stdout.write(f"\x1b7\x1b[{y};{x}f{line}\x1b8")
            y += 1
        stdout.flush()

    def win_clear(self):
        system("cls" if name == "nt" else "clear")


##-- 2D Array class --##


class Grid:
    """
    Geometry manager Grid.

    Base class to use the methods grid_* in every widget.
    """
    __slots__ = ['size', 'char', '_grid']
    def __init__(self, cols=5, rows=5, char=" "):  # chr(9617)
        self.size = Point(cols, rows)
        self.char = char
        self._grid = None
        self.grid_construct_grid()

    def __repr__(self):
   
        return "Grid()"

    def __str__(self):
        return str(self._grid)

    def grid_construct_grid(self):
        self._grid = [self.char * self.size.x] * self.size.y

    def grid_clear(self):
        if hasattr(self, "_grid"):
            self.grid_construct_grid()

    def grid_parse(self):
        self._grid = [list(i) for i in self._grid]

    def grid_list_to_string(self):
        # list_to_box  New Name
        self._grid = ["".join(i) for i in self._grid]

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


##-- Shape classes --##


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
    """
    Description:
    -----------
        Draws a Square in a Frame.

    """
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
        s = WindowSplicer(self.root, self)
        s.splice()


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
    boarder lines around the widget class.
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
        self.root.grid_parse()
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
        self.root.grid_list_to_string()

    def stamp(self, locations, style):
        for spot in locations:
            self.root._grid[spot.row][spot.col] = style

    def pack(self):
        self._draw()


##-- GUI ish classes --##


class Widget(Grid, Window):
    """
    Base class for all widgets
    """

    def __init__(self, root=None, style=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = None
        self.style = style

    def render(self):
        self.win_render_box(0, 0, self._grid)


class Label(Widget):
    """
    For Placing basic text.

    Parameters
    ----------
        root: Frame = None
            takes Frame object as master/root

        text: str
            to be on screen

        anchor: tuple
            default 0, 0
            tuple of x , y location of top left corner of label box

        boarder: bool
            deault True boarder on, False boarder off

        cols: int = 5
            aka how width the screen will be.

        rows: int = 5
            aka how tall/height the screen will be
        
        char: chr, string, int = chr(9608)
            aka what is the place holder.
            can be a space ' '.
    """

    def __init__(self, root, text, anchor=(0, 0), boarder=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.text = text
        self.boarder = boarder
        if anchor == "center":
            self.start_point = Point(
                (self.root.size.x // 2) - (self.size.x // 2),
                (self.root.size.y // 2) - (self.size.y // 2),
            )
        else:
            self.start_point = Point(anchor[0], anchor[1])

    def _draw(self):
        if self.boarder:
            boarder = Boarder(self)
            boarder.pack()
            self.inside = Point(2, 2) - self.size
        else:
            self.inside = self.size
        self._insert_text()

    def _insert_text(self):
        txt = TextPoint(self.text, self.start_point)
        self.grid_parse()
        indexes = sum(self.grid_get_index(),[])
        for idx in indexes:
            point = Point().fromIndex(self, idx)
            if txt.current_char == None:
                break
            if self._grid[point.y][point.x] == ' ':
                self._grid[point.y][point.x] = CharToken(txt.current_char, bg=bg.black)
                txt.advance()
        
        self.grid_list_to_string()



    def pack(self, hl=False, bg="black", row=0):

        self._draw()
        win = WindowSplicer(self.root, self)
        win.splice()

    


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


##-- Event Class --##


@dataclass
class Event:
    time_of: float
    method: FunctionType or MethodType


##-- State Class --##


class Tui(Frame):
    """
    Base class for handling internal functions
    """

    TICKS = 0.1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 0.0
        self.events = []
        self.key = None
        self.key_len = 5
        self.previous_grid = self._grid

    def after(self, delay, func):
        delay = self.add_float(delay, self.count)
        event = Event(delay, func)
        self.events.append(event)

    def window_geometry(self, cols=None, rows=None, fullscreen=False):
        """
        Sets the Size of the bass Frame
        
        Parameters: KEYWORDS
            cols:
                width
            rows:
                height

            fullscreen:
                default: False, set to True will grab screen size.
        """
        if fullscreen:
            cols, rows = get_terminal_size()
            self.size.reset(cols, rows - 1)
        else:
            self.size.reset(cols, rows)
        self.grid_construct_grid()
        self.boarder.pack()

    def is_pressed(self, key, event=None):
        self.key_len = len(key)
        if self.key != None:
            if key == self.key:
                if event == None:
                    return True
                else:
                    event()

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

    def check_render(self, current, previous):
        if current != previous:
            self.render()
            self.previous_grid = current

    def advance_count(self):
        self.count = self.add_float(self.count, self.TICKS)

    def mainloop(self):
        while True:
            self.key = getchar(self.key_len)
            self.check_render(self._grid, self.previous_grid)
            self.advance_count()
            self._exc()
            sleep(self.TICKS)

    @staticmethod
    def add_float(num1, num2):
        return round(num1 + num2, 1)


##-- MainLoop Function --##


def mainloop(root):
    try:
        hide()
        root.mainloop()
    except KeyboardInterrupt:
        raise

    finally:
        show()
