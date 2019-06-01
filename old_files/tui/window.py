from .matrix import Matrix
from .vector import Vector


class Window():

    def __init__(self, cords, title, char=' '):


        x1, y1, x2, y2 = cords
        self.point1 = Vector(x1, y1)
        self.point2 = Vector(x2, y2)
        self.master = self.point1.get_width_height_of_master(self.point2)
        self.width = self.master.x
        self.height = self.master.y
        self.array2d = Matrix(self.master.x, self.master.y, char)
        self.add_title(title)



    def __str__(self):
        return self.array2d.__str__()


    def __iter__(self):
        self.n = 0
        return self


    def __next__(self):
        if self.n < len(self.array2d):
            result =  self.array2d[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __len__(self):

        return self.array2d.get_parse().__len__()


    def parse(self):
        return self.array2d.get_parse()
    
    
    def add_title(self, text):
        x = round(self.width / 2) - round(len(text) / 2)
        self.array2d.insert_at(text, x, 0)

if __name__ == "__main__":
    import doctest
    doctest.testmod()