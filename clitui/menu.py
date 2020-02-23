from types import FunctionType
from .display import print_at, draw_brectangle, getchar, is_pressed
from .font import bg_by, fg_by, style_by, fg_color_by, bg_color_by


# TODO Menu is the Node and the Manager possable break
# this up into Two seporate classes in the next update.

# TODO Set up actions
class Menu:
    """
    Menu is a manager and node.
    """

    def __init__(
        self, name: str, x: int = None, y: int = None, border: bool = True, btype=0
    ):
        self.name = name
        self.x = x
        self.y = y
        self.border = border
        self.btype = btype
        self.bg = None
        self.hl = 0
        self.items = {}
        self.walk = []
        self.to_draw = []

    def __repr__(self):
        return f"{self.name}"

    def add(self, name: str, _id: int):
        self.items[_id] = {"name": name}
        return self

    def background_color(self, color: (tuple, list)):
        c = bg_color_by(color)
        if c is None:
            c = bg_by(color)
        self.bg = c
        return self

    def font_color_for(self, _id: int, color: (tuple, list)):
        c = fg_color_by(color)
        if c is None:
            c = fg_by(color)
        self.items.get(_id).update(fg=c)
        return self

    def submenu(self, _id: int, menu):
        """menu: Menu"""
        self.items.get(_id).update(submenu=menu)
        return self

    def add_action(self, _id: int, action: FunctionType):
        self.items.get(_id).update(action=action)
        return self

    def move_curser(self, key: str):
        if is_pressed("UP", key):
            self.hl -= 1 if self.hl > 0 else 0
        elif is_pressed("DOWN", key):
            self.hl += 1 if self.hl < len(self.items) - 1 else 0
        elif is_pressed("ENTER", key):
            self.walk.append(self.hl)
            node = self._get_node()
            subnode = node.get("submenu")
            if subnode is not None:
                self.create(subnode.items)
                self.hl = 0
            else:
                self.walk.pop(-1)
                return node.get("action")

        elif is_pressed("TAB", key):
            if len(self.walk) > 0:
                self.walk.pop(-1)
                if len(self.walk) > 0:
                    self.create(self._get_node().get("submenu").items)
                else:
                    self.create(self.items)
                self.hl = 0

    def _get_node(self):
        try:
            first, *walk = self.walk
            node = self.items.get(first)
            if node is not None:
                for i in walk:
                    node = node.get("submenu")
                    node = node.items.get(i)
        except:
            node = self.items.get(self.hl)
        return node

    @staticmethod
    def _max_option_len(items: dict):
        return max([len(v.get("name")) for v in items.values()])

    def _addwhitespace(self, name: str, w: int):
        return name + (" " * (w - len(name) - 1))

    def create(self, items: dict = None):
        items = items if items is not None else self.items
        w = self._max_option_len(items) + 1
        h = len(items) + 1
        self.to_draw = [w, h, self.x, self.y]
        for i, v in enumerate(items.values()):
            ch = self._addwhitespace(v.get("name"), w)
            fg = v.get("fg")
            posx = self.x + 1
            posy = self.y + i + 1
            iterable = (posx, posy, ch, fg)
            self.to_draw.append(iterable)

    def draw(self):
        w, h, x, y, *draw_info = self.to_draw
        if self.border:
            draw_brectangle(x, y, w, h, outline=self.btype, bg=self.bg)
        for i, (x, y, ch, fg) in enumerate(draw_info):
            style = style_by("slow_blink") if i == self.hl else None
            print_at(x, y, ch, style=style, fg=fg, bg=self.bg)
