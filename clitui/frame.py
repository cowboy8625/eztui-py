from .point import Vector2
from .window import Window
from .win_boarder import outline


class Frame(Window):
    def __init__(
        self,
        root=None,
        width=5,
        height=5,
        char=" ",
        fg=None,
        bg=None,
        pos=None,
        boarder=False,
    ):
        super().__init__(width, height, char, fg, bg, boarder)
        self.root = root
        if pos is None:
            self.pos = Vector2(1, 1)
        else:
            self.pos = pos

        self.add_to_root()

    def add_to_root(self):
        if self.root is not None:
            self.root.add_child(self)

    def can_fit(self):
        if self.dim.x < self.root.dim.x and self.dim.y < self.root.dim.y:
            return True
        else:
            return False
