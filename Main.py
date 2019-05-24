# python 3.7
# Start Date May 6, 2019
# Arthur Cowboy8625


# in house modules
from tui.screen import Screen
from tui.shape import Square
from tui.matrix import Matrix
from tui.terminal_size import get_terminal_size


TICKS = 0.5 #0.016666666666666666 # This is not used.


def test():
    import time
    while True:
        WIN_WIDTH, WIN_HEIGHT = get_terminal_size()
        win = Screen(WIN_WIDTH, WIN_HEIGHT, char='0')
        win.controls()
        win.map()
        win.render()
        time.sleep(TICKS)

if __name__ == "__main__":
    test()
    import doctest
    doctest.testmod()