from .vector import Vector


class Matrix:
    '''
    Makes a 2d List.

    Controls all aspects of the list object by clearing of all
    item in list or adding new items.

    Parameters
    ----------
    width : int
        Sets the Width of the 2d List.
    height : int
        Sets the Height of the 2d List.
    char : str
        Set the char that will fill the 2d List.
        Default is set to ' '

    Returns
    -------
    list
        List of a single string item.

    Test
    ----
    >>> array2d = Matrix(3, 3, '1')
    >>> print(array2d)
    111
    111
    111
    '''

    def __init__(self, width, height, char=' '):
        self.width = width
        self.height = height
        self.char = char
        self._array2d = None
        self.clear()
        

    def __str__(self):
        return self.array2d



    def __iter__(self):
        self.n = 0
        return self


    def __next__(self):
        if self.n < len(self._array2d):
            result = self._array2d[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        return self._parse(self._array2d).__len__()
    
    @property
    def array2d(self):
        '''returns the array2d attribute'''
        return self._array2d
    
    @array2d.setter
    def array2d(self, value):
        '''sets the array2d attribute'''
        self._array2d = value

    def insert_at(self, text, x, y):
        '''
        Places text in 2d List.

        Text will be start at cords given to be placed in 2d List.

        Parameters
        ----------
        text : str
            Text that will be place in 2d List
        x : int
            X Cords, X is up and down.
        y : int
            Set the char that will fill the 2d List.
            Default is set to ' ' < This is a Space.

        Test
        ----
        >>> array2d = Matrix(3,3,'1')
        >>> array2d.insert_at('hello',0,0)
        >>> print(array2d)
        hel
        lo1
        111
        '''

        screen = self._parse(self._array2d)
        for i in text:
            screen[y][x] = i
            # Checks to see if letter can fit on screen
            if x >= len(screen[y])-1:
                x = 0
                if y >= self.height-1:
                    break
                else:
                    y += 1
            else:    
                x += 1
        self._array2d = self._unparse(screen)


    def insert_window(self, other):
        '''
        Takes a Window object and place's it in the Matrix at give points
        
        Parameters
        ----------
            other : Window
                Has to be Window object.
        '''
        if other.width < self.width and other.height < self.height:
            window_cells = self._get_cells(other, self.width, self._add_to_list)
            array2d = self._parse(self._array2d)
            other2d = iter(other.parse())

            for line in window_cells:
                other_cell = iter(next(other2d))
                for index in line:
                    x = self._get_x(index, self.width)
                    y = self._get_y(index, self.width)
                    array2d[y][x] = next(other_cell)
            self._array2d = self._unparse(array2d)

        else:
            raise Exception("Window will not fit in screen.")


    def clear(self):
        '''Clears 2d List by creating list.'''
        self._array2d = ''.join([self.char * self.width + '\n'] * self.height)[0:-1]

    def get_parse(self):
        return [list(i) for i in list(self._array2d.split('\n'))]

    # This need to go into Vector
    @staticmethod
    def _get_x(index, width):
        return index % width

    # This need to go into Vector
    @staticmethod
    def _get_y(index, width):
        return int(index / width)


    @staticmethod
    def _get_cells(other, width, _add_to_list):
        '''Returns window object cells in Main Screen's Matrix'''
        
        result = []
        # This could be its our method
        starting_cell = (other.point1.y * width) + other.point1.x
        ending_cell = (other.point1.y * width) + other.point2.x
        first_row = [i for i in range(starting_cell, (ending_cell + 1))]
        result.append(first_row)
        for _ in range(other.height - 1):
            result.append(_add_to_list(result[-1], width))
        return result


    @staticmethod
    def _parse(array2d):
        '''
        Takes the single string item in 2d List.
        Returns a list of list seporated by '\\n'
        '''
        return [list(i) for i in list(array2d.split('\n'))]


    @staticmethod
    def _unparse(array2d):
        '''Restores 2d List to original single string state'''
        return ''.join([i+'\n' for i in [''.join(i) for i in array2d]])[0:-1]


    @staticmethod
    def _add_to_list(cells, step):
        '''Takes in list and step number and adds step number to each list item'''
        result = []
        for num in cells:
            result.append(num + step)
        return result

