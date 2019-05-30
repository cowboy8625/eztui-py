# python 3.7
__start_date__ = 'May 6, 2019'
__arthur__ = 'Cowboy8625'

from time import sleep
from os import name, system

# In House Modules
from tui.shape import Square
from tui.matrix import Matrix
from tui.window import Window
from tui.terminal_size import get_terminal_size

# My Testing Module
from MyModules.inhousetest import get_memory_usage
from MyModules.loggers import Logger


TICKS = 1 # 0.016666666666666666


class Screen:

    WINDOW_LOCATIONS = {
        'controls' : [(0,11,20,20), 'Controls'],
        'map' : [(20,3,78,24), 'Map']
    }

    def __init__(self, width, height, char=' '):

        self.char = char
        self.array2d = Matrix(width, height, char)
        self.width = width
        self.height = height
        self.window_list = []



    def combat(self):
        pass

    def map(self):
        con_win = Window(self.WINDOW_LOCATIONS['map'][0],
        
        self.WINDOW_LOCATIONS['map'][1], chr(9608))
        self.window_list.append(con_win)

    def controls(self):
        con_win1 = Window(self.WINDOW_LOCATIONS['controls'][0],
        self.WINDOW_LOCATIONS['controls'][1], chr(9608))
        self.window_list.append(con_win1)


    def label(self):
        pass

    def render(self):
        for window in self.window_list:
            self.array2d.insert_window(window)

        self.clear()
        print(self.array2d)

    def clear(self):
        system('cls' if name == 'nt' else 'clear')

class Stater:
    '''
    Finite State Machine
    '''
    def __init__(self):
        self.state = self.start
        self.win_width, self.win_height = get_terminal_size()
        self.screen = Screen(self.win_width, self.win_height, char=chr(9617))

    def start(self):
        self.screen.controls()
        

    def render(self):
        self.win_width, self.win_height = get_terminal_size()
        self.screen.width = self.win_width
        self.screen.height = self.win_height
        self.screen.render()
        print(get_memory_usage())

    
def main():

    app = Stater()
    
    while True:

        app.state()
        app.render()
        sleep(TICKS)

def test():
    mx = Matrix(10, 10)
    square = Square(mx, 5, (2,2)).draw(0)
    print(square)

if __name__ == "__main__":
    main()

    # test()
    import doctest
    doctest.testmod()