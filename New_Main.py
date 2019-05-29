from abc import ABC, abstractmethod
from time import sleep
from os import system, name
from sys import stdout

# in House Modules
try:
    from MyModules.loggers import Logger
    from MyModules.inhousetest import pause
except:
    pass
class Point:
    '''
    Base Class

    Description:
    -----------
        Makes adding to points together a bit easier.

    Test:
    ----
    >>> p1 = Point(1,1)
    >>> p2 = Point(2,2)
    >>> p3 = p1 + p2
    >>> p3
    (3, 3)
    >>> p1 += p1
    >>> p1
    (2, 2)
    >>> p3 = p1 * p2
    >>> p3
    (4, 4)
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Point((self.x + other.x), (self.y + other.y))

    def __mul__(self, other):
        return Point((self.x * other.x), (self.y * other.y))

    @classmethod
    def fromIndex(cls, root, index):
        '''
        Returns a x and y point.
        '''
        x = index % root.size.x
        y = int(index / root.size.x)
        return cls(x, y)



class Index:
    '''
    Base class handles all calculations for point to index.
    
    Parameters:
    ----------
        root: Frame
            Takes a Frame object for root to work. Index can be of
            child widget or of a master/root.
        
        point: Point
            Takes a Point object.

    Test:
    ----
    >>> root = Frame(cols=10, rows=10, char='0')
    >>> p1 = Point(4,4)
    >>> idx1 = Index(root, p1)
    >>> idx1.index
    44
    '''

    def __init__(self, root, point):
        self.root = root
        self.point = point
        self._index = self.__set_index(root, point)

    def __repr__(self):
        return self.index().__str__()
    
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, ndx):
        self._index = ndx

    @staticmethod
    def __set_index(root, point):
        return (point.y * root.size.x) + point.x # (y * width) + x



class TUI:
    '''
    Base class for handling internal functions
    '''
    def __init__(self):
        raise NotImplemented

    def mainloop(self):
        raise NotImplemented

class Window:
    '''
    Display manager Window

    Base class to use the methods win_*
    '''
    @staticmethod
    def win_pack(item):
        stdout.writelines(item + '\n')
    
    @staticmethod
    def clear():
        system('cls' if name == 'nt' else 'clear')


class Grid:
    '''
    Geometry manager Grid.

    Base class to use the methods grid_* in every widget.
    >>> grid = Grid()
    >>> grid
    ░░░░░
    ░░░░░
    ░░░░░
    ░░░░░
    ░░░░░
    
    '''
    def __init__(self, cols=5, rows=5, char=chr(9617)):
        self.size = Point(cols, rows)
        self.char = char
        self.grid_construct_grid()

    def __repr__(self):
        return self._grid

    def grid_construct_grid(self):
        self._grid = ''.join([self.char * self.size.x + '\n'] * self.size.y)[0:-1]

    def _parse(self):
        self._grid = [list(i) for i in list(self._grid.split('\n'))]

    def _list_to_string(self):
        self._grid = ''.join([i+'\n' for i in [''.join(i) for i in self._grid]])[0:-1]


class Shape(Grid, ABC):
    '''
    Base Class

    Description:
    -----------
        Hold all info for making a basic shape.

    Parameters
    ----------
        root: Frame
            takes frame object to place all Shapes on.
    '''
    ELEMENTS = {
        'hBoarder': [chr(9552), chr(9472), chr(9473)],
        'vBoarder': [chr(9553), chr(9474), chr(9475)],
        'lTee': [chr(9571), chr(9508), chr(9515)],
        'rTee': [chr(9568), chr(9500), chr(9507)],
        'tTee': [chr(9574), chr(9516), chr(9523)],
        'bTee': [chr(9577), chr(9524), chr(9531)],
        'ltConner': [chr(9556), chr(9581), chr(9487)],
        'rtConner': [chr(9559), chr(9582), chr(9491)],
        'lbConner': [chr(9562), chr(9584), chr(9495)],
        'rbConner': [chr(9565), chr(9583), chr(9499)],
        'lSlope': ['/', '/', '/'],
        'rSlope': ['\\', '\\', '\\'],
        'cross': [chr(9580), chr(9532), chr(9547)]
        }

    def __init__(self, root=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = root
        self.shape_points = None
        self.start_point = Point()

    @abstractmethod
    def _draw(self):
        pass

    @abstractmethod
    def place_at():
        pass

    def pack(self):
        '''adds shape to gird'''
        self._get_outline_index_list()

        self._draw()

    def _get_outline_index_list(self):

        #TODO Refine to run off genorators.
        result = []
        starting_cell = (self.start_point.y * self.size.x) + self.start_point.x
        ending_cell = (self.start_point.y * self.size.x) + self.size.x
        first_row = [i for i in range(starting_cell, (ending_cell + 1))]
        result.append(first_row)
        for _ in range(self.size.y - 1):
            result.append(self._add_to_list(result[-1], self.master.size.x))
        self.index_list = result

    @staticmethod
    def _add_to_list(cells, step):
        '''Takes in list and step number and adds step number to each list item'''
        return [(num + step) for num in cells]


class Square(Shape):
    '''
    Draws a Square on window
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _draw(self):
        pass

    def place_at(self):
        pass

    def __get_outline(self):
        top_horizontal_line = self.index_list[0]
        leftside_vertical_line = None
        rightside_vertical_line = None
        bottom_horizontal_line = self.index_list[-1]

        for idx in top_horizontal_line:
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self.ELEMENTS['hBoarder'][0]
            del line_point



class Rectangle(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Boarder(Square, Rectangle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Widget(Grid, Window):
    '''
    Base class for all widgets
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pack(self):
        self.win_pack(self._grid)

class Label(Widget):
    '''
    For Placing basic text.

    Parameters
    ----------
        root: Frame Default : None
            takes Frame object as master/root

        cols: int Default : 5
            aka how width the screen will be.

        rows: int Default : 5
            aka how tall/height the screen will be
        
        char: chr, string, int Default : chr(9608)
            aka what is the place holder.
            can be nothing.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MessageBox(Widget):
    '''
    Pops up in middle of master/root Frame to display alert messages.

    Parameters
    ----------
        root: Frame Default : None
            takes Frame object as master/root

        cols: int Default : 10
            aka how width the screen will be.

        rows: int Default : 5
            aka how tall/height the screen will be
        
        char: chr, string, int Default : chr(9608)
            aka what is the place holder.
            can be nothing.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Frame(Widget, Boarder):
    '''
    Master window class

    All Widget type objects will be held in Frame class
    
    Parameters
    ----------
        root: Frame Default : None
            takes frame object only if Frame is a Child.

        cols: int Default : 5
            aka how width the screen will be.

        rows: int Default : 5
            aka how tall/height the screen will be
        
        char: chr, string, int Default : chr(9608)
            aka what is the place holder.
            can be nothing.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


##-- User interface --##

class App(Frame):
    '''
    How you would use the API
    '''
    def __init__(self):
        self.master = Frame(cols=100, rows=30, char=chr(9608))
        self.clear()
        self.initTUI()

    def initTUI(self):

        self.square = Square(self.master, 10, 10, char=chr(9608))
        self.square.pack()
        self.master.pack()


def test():
    # Ignore Just for Testing.
    root = Frame(cols=10, rows=10)
    p1 = Point.fromIndex(root, 15)
    print(p1)

if __name__ == "__main__":
    app = App() 
    import doctest
    doctest.testmod()