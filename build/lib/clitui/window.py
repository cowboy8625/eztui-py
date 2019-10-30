from .point import Vector2, vct_to_idx
from .terminal_size import get_terminal_size
from .asciiesc import RESET, fg_color, bg_color
from .pixel import Pixel
from .win_boarder import outline
from .output import print_at, clear_screen


class Window:
    def __init__(self, width=5, height=5, char=" ", fg=None, bg=None, boarder=False):
        self.root = None
        self.dim = Vector2(width, height)
        self.char = char
        self.fg = fg
        self.bg = bg
        self.style = (0, self.fg, self.bg)
        self.grid = None
        self.boarder = boarder
        self.pos = None
        self.fullscreen = False
        self.children = []
        self.pix_to_change = []
        self.hrow_to_change = []

    def add_child(self, child):
        self.children.append(child)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                self.__dict__[key] = value
            else:
                print("Error")
                input("Error......")

    def set_hor_row(self, x, y, row_char, fg=None, bg=None):
        w = self.dim.x
        # fg = fg if fg == None else self.fg
        # bg = fg if bg == None else self.bg
        self.hrow_to_change.append(
            [
                y,
                [
                    Pixel(char, (y * w) + i + x, fg, bg)
                    for i, char in enumerate(row_char)
                ],
            ]
        )
        if self.grid is not None:
            self.update_hrow()

    def update_hrow(self):
        if self.hrow_to_change is not None:
            for y, pix in self.hrow_to_change:
                if self.boarder:
                    pix_l = self.grid[y][0]
                    pix_r = self.grid[y][-1]
                    self.grid[y] = [pix_l] + pix + [pix_r]
                else:
                    self.grid[y] = pix
            self.hrow_to_change.clear()

    def set_pix(self, x, y, char=None, fg=None, bg=None):
        self.pix_to_change.append([x, y, char, fg, bg])
        if self.grid is not None:
            self.update_pix()

    def update_pix(self):
        if self.pix_to_change is not None:
            for x, y, char, fg, bg in self.pix_to_change:
                pix = self.grid[y][x]
                char = pix.char if char is None else char
                fg = pix.fg if fg is None else fg
                bg = pix.bg if bg is None else bg
                self.grid[y][x] = Pixel(char, pix.index, fg, bg)
            self.pix_to_change.clear()

    def pack(self):
        self.grid = self.make_grid(self.dim.x, self.dim.y, self.char, self.fg, self.bg)
        if self.boarder:
            outline(self)
        if self.children is not None:
            for child in self.children:
                child.pack()

    def render(self, clear=False):
        if self.fullscreen:
            pass
            # x, y = get_terminal_size()
            # self.dim = Vector2(x, y)
            # self.pack()
        if self.grid is None:
            self.pack()
        if clear:
            clear_screen()
        if self.children is not None:
            for child in self.children:
                self.place_frame_in(self, child)
        grid = "\n".join(("".join((str(w) for w in h)) for h in self.grid))

        if self.pos is not None:
            print_at(f"{RESET}{grid}", self.pos.x, self.pos.y)
        else:
            print(f"{RESET}{grid}")

    @staticmethod
    def make_grid(width, height, char=" ", fg=None, bg=None):
        return [
            [Pixel(char, vct_to_idx((y, x), width), fg=fg, bg=bg) for x in range(width)]
            for y in range(height)
        ]

    @staticmethod
    def place_frame_in(root, child):
        # print(root.__class__.__name__)
        # print(child.__class__.__name__)
        # print(root.pos)
        # print(root.dim)
        x, y = child.pos.x, child.pos.y
        W = child.dim.x
        for line in child.grid:
            for pix in line:
                x1 = (pix.index % W) + x
                y1 = (pix.index // W) + y
                root.grid[y1][x1] = pix
