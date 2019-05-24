from .matrix import Matrix
from .vector import Vector

class Shape:

    def __init__(self, array2d, width, height):
        self.cords = Vector(width, height)
        self.array2d = array2d

    def draw(self):
        self.array2d.get_parse()
        print(self.array2d)
        height = len(self.array2d)
        width = len(self.array2d.array2d[0])
        self.array2d[(width // 2)-2][height // 2] = 'S'
        self.array2d[(width // 2)-1][height // 2] = 'h'
        self.array2d[(width // 2)][height // 2] = 'a'
        self.array2d[(width // 2)+1][height // 2] = 'p'
        self.array2d[(width // 2)+2][height // 2] = 'e'
        self.get_unparse()
        return self.array2d

    def __parse(self):
        '''
        Discretion:
        ----------
            Takes the single string item in 2d List.
        
        Returns:
        -------
            A list of list seporated by '\\n'.
        '''
        return [list(i) for i in list(self.array2d.split('\n'))]


    def __unparse(self):
        '''
        Discretion:
        ----------
            Restores 2d List to original single string state
        
        Returns:
        -------
            A string object with '\n' placed where len() == width
        '''
        return ''.join([i+'\n' for i in [''.join(i) for i in self.array2d]])[0:-1]

class Square(Shape):

    def __init__(self, array2d, width, height):
        super().__init__(array2d, width, height)

    

class Circle(Shape):

    def __init__(self, array2d, width, height):
        super().__init__(array2d, width, height)

    def draw(self):
        pass

class Rectangle(Shape):

    def __init__(self, array2d, width, height):
        super().__init__(array2d, width, height)

    def draw(self):
        pass


