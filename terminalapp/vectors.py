class Point:
    """
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
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point((self.x + other.x), (self.y + other.y))

    def __mul__(self, other):
        return Point((self.x * other.x), (self.y * other.y))

    def reset(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def fromIndex(cls, root, index):
        """
        Returns a x and y point.
        """
        x = index % root.size.x
        y = int(index / root.size.x)
        return cls(x, y)

    def x_same_as_y(self):
        if self.x == self.y:
            return True
        else:
            return False

    def mul(self, type_of, times):
        self.x = round(self.x * times)


class Index:
    """
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
    """

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
        return (point.y * root.size.x) + point.x  # (y * width) + x


##-- TextPoint Class for handling any type of text parsing --##


class GridPoint:
    def __init__(self, root):
        self.root = root
        self.grid = self.init_text(root._grid)
        self.col = -1
        self.row = 0
        self.current_char = None
        self.advance()

    def __repr__(self):
        return f"{self.current_char}"

    def __len__(self):
        return len("".join(self.root._grid.split("\n")))

    @property
    def index(self):
        return Index(self.root, Point(self.col, self.row)).index

    def advance(self):
        try:
            self.current_char = next(self.grid)
            if self.current_char != "\n":
                self.col += 1
            else:
                self.col = 0
                self.row += 1
                self.advance()
        except StopIteration:
            self.current_char == None

    def init_text(self, text):
        for i in text:
            yield i


class TextPoint:
    def __init__(self, text, start):
        self.text = self.init_text(text)
        self.start = start
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
            self.pos += 1
        except:
            self.current_char = None

    def init_text(self, text):
        for i in text:
            yield i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
