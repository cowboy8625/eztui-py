
class Vector:
    '''
    If given an X and Y value with a width of master screen
    an Index value is available.

        

    Parameters
    ----------
        x : int
            width value

        y : int
            height value

        width : int
            width of master screen

        index : int
            index of screen list

    Returns
    -------
        index or x and y tuple
    

    Test
    ----
    >>> vec = Vector(x=1, y=1, width=10)
    >>> vec1 = Vector(x=2, y=2, width=10)
    >>> vec2 = vec1 + vec
    >>> str(vec2)
    '(3, 3)'
    >>> vec2.index
    33
    >>> vec2.x
    3
    >>> vec2.y
    3
    >>> index = Vector(width=10, index=23)
    >>> index.x
    3
    >>> index.y
    2
    '''

    def __init__(self, x=None, y=None, width=None, index=None):

        if x is None and y is None:
            self.x, self.y = self.__set_cords(index, width)
        else:
            self.x = x
            self.y = y
        if width is not None and x is not None and y is not None:
            self.index = self.__set_index(x, y, width)
            self.width = width
        else:
            self.index = index
            self.width = width


    def __str__(self):
        return f'({self.x}, {self.y})'


    def __add__(self,other):
        if hasattr(self, 'width'):
            return Vector(x=(self.x + other.x), y=(self.y + other.y), width=self.width)
        else:
            return Vector(x=(self.x + other.x), y=(self.y + other.y))


    def get_width_height_of_master(self, other):
        '''
        Description:
        -----------
            Give a Vector class object will return a master window 
            width and height.

        Parameters:
        ----------
            other : Vector
                of type Vector
        
        Return:
        ------
            returns new Vector with master object
        '''
        if self.x > other.x:
            x = (self.x - other.x) + 1
        else:
            x = (other.x - self.x) + 1
        if self.y > other.y:
            y = (self.y - other.y) + 1
        else:
            y = (other.y - self.y) + 1

        return Vector(x=x, y=y, width=x)


    @staticmethod
    def __set_index(x, y, width):
        return (y * width) + x

    @staticmethod
    def __set_cords(index, width):
        x = index % width
        y = int(index / width)
        return x, y

