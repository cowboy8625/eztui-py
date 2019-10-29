from .matrix_rain import Screen
from .terminal_size import get_terminal_size
max_x, max_y = get_terminal_size()
screen = Screen(max_x, max_y, amount=int(max_x//2))
screen.render()


