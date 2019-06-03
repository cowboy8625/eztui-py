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

    def x_same_as_y(self):
        if self.x == self.y:
            return True
        else:
            return False



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
    #>>> root = Frame(cols=10, rows=10, char='0')
    #>>> p1 = Point(4,4)
    #>>> idx1 = Index(root, p1)
    #>>> idx1.index
    44
    '''

    def __init__(self, root, point):
        self.root = root
        self.point = point
        self._index = self.__set_index(root, point)

    def __str__(self):
        return self._index.__str__()
    
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

    def grid_parse(self):
        self._grid = [list(i) for i in list(self._grid.split('\n'))]

    def grid_list_to_string(self):
        self._grid = ''.join([i+'\n' for i in [''.join(i) for i in self._grid]])[0:-1]

    def grid_get_index(self):
        step = self.size.x
        total = (self.size.x * self.size.y)
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

    # Shape Factory

    def type_of(root, of_type):
        of_type = of_type.lower()
        if of_type == 'square':
            return Square(root)
        elif of_type == 'rectangle':
            return Rectangle(root)




class BaseShape(Grid, ABC):
    '''
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

        
    '''
    ELEMENTS = {
        'hBoarder': [chr(9552), chr(9472), chr(9473)],
        'vBoarder': [chr(9553), '|', chr(9475)], # chr(9474)
        'lTee': [chr(9571), chr(9508), chr(9515)],
        'rTee': [chr(9568), chr(9500), chr(9507)],
        'tTee': [chr(9574), chr(9516), chr(9523)],
        'bTee': [chr(9577), chr(9524), chr(9531)],
        'ltCorner': [chr(9556), chr(9581), chr(9487)],
        'rtCorner': [chr(9559), chr(9582), chr(9491)],
        'lbCorner': [chr(9562), chr(9584), chr(9495)],
        'rbCorner': [chr(9565), chr(9583), chr(9499)],
        'lSlope': ['/', '/', '/'],
        'rSlope': ['\\', '\\', '\\'],
        'cross': [chr(9580), chr(9532), chr(9547)]
        }

    def __init__(self, root=None, style=1, *args, **kwargs):
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
        '''adds shape to gird'''
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
            self.root._grid[line_point.y][line_point.x] = self._get_char('hBoarder')
            del line_point

    def bottom_line(self):

        for idx in self.index_list[-1]:
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self._get_char('hBoarder')
            del line_point

    def right_line(self):

        for idx in self.__get_vertical_index_list(self.index_list, -1):
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self._get_char('vBoarder')
            del line_point

    def left_line(self):

        for idx in self.__get_vertical_index_list(self.index_list, 0):
            line_point = Point().fromIndex(self.root, idx)
            self.root._grid[line_point.y][line_point.x] = self._get_char('vBoarder')
            del line_point

    def add_corners(self):
        top_left, top_right, bottom_left, bottom_right = self.get_corner_index()

        p1 = Point().fromIndex(self.root, top_left)
        self.root._grid[p1.y][p1.x] = self._get_char('ltCorner')

        p2 = Point().fromIndex(self.root, top_right)
        self.root._grid[p2.y][p2.x] = self._get_char('rtCorner')

        p3 = Point().fromIndex(self.root, bottom_left)
        self.root._grid[p3.y][p3.x] = self._get_char('lbCorner')

        p4 = Point().fromIndex(self.root, bottom_right)
        self.root._grid[p4.y][p4.x] = self._get_char('rbCorner')

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
        '''Takes in list and step number and adds step number to each list item'''
        return [(num + step) for num in cells]


class Square(BaseShape):
    '''
    Description:
    -----------
        Draws a Square in a Frame.

    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resize(self, width, height):
        self.size = Point(round(width * 2.5), height)
    
    def _draw(self):
        # Wrong Areafor this to be in!
        # self.size.x *= 2
        # -----------
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
    '''
        Description:
    -----------
        Draws a Rectangle in a Frame.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _draw(self):
        print('Rectangle has been drawn.')
        self._get_outline_index_list()
        print(self.index_list)


class Boarder(BaseShape):
    '''
    Boarder is a Base class to handle construction of 
    boarder lines around the widget class.
    
    Square, Rectangle have a Composition relationship with 
    the Boarder class.
    '''
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
        root: Frame = None
            takes Frame object as master/root

        cols: int = 5
            aka how width the screen will be.

        rows: int = 5
            aka how tall/height the screen will be
        
        char: chr, string, int = chr(9608)
            aka what is the place holder.
            can be a space ' '.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MessageBox(Widget):
    '''
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
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Frame(Widget):
    '''
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
    '''

    def __init__(self, style=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.boarder = Boarder(self).pack()



##-- User interface --##
#from TUI import Frame
class App(Frame):
    '''
    How you would use the API
    '''
    def __init__(self):
        self.master = Frame(cols=100, rows=40, char=chr(9608))
        self.clear()
        self.initTUI()

    def initTUI(self):
        
        self.shape = Shape.type_of(self.master, "Square")
        self.shape.place_at(5,5)
        self.shape.resize(30, 30)
        self.shape.pack()
        self.master.pack()


def test():
    root = Frame()
    root.pack()
if __name__ == "__main__":
    app = App()
    import doctest
    doctest.testmod()