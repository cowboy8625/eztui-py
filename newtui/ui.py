##-- Module Imports --##
from .grid import Grid

class Widget:

    def __init__(self, root=None, width=5, height=5, bg=' '):
        self.grid = Grid(width, height, char=bg)
        if root is None:
            raise "Missing root for Widget"
        else:
            self.root = root 

    def place_at(self, x, y, text):
        x += self.root.startX - 1
        y += self.root.startY- 1 
        self.grid.insert_at(x,y,text)

    def clear(self):
        self.grid.clear_grid()
        
    def pack(self):
        self.grid.render()


class Label(Widget):

    def __init__(self, text="", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = text

    def pack(self,start_loc=(0,0)):
        self.grid.change_location(start_loc[0], start_loc[1])
        self.place_at(0,0,self.text)
        self.grid.render()
