from .display import print_at, draw_brectangle, getchar, is_pressed
from .font import bg_by, fg_by, style_by, fg_color_by, bg_color_by
from collections import deque


class Menu:
    def __init__(self, name, x=None, y=None):
        self.name = name
        self.x = x
        self.y = y
        self.bg = None
        self.hl = 0
        self.items = {}
        self.to_draw = []

    def __repr__(self):
        return f"{self.name}"

    def add(self, name, _id):
        self.items[_id] = {"name": name}
        return self

    def background_color(self, color):
        c = bg_color_by(color)
        if c is None:
            c = bg_by(color)
        self.bg = c
        return self

    def font_color_for(self, _id, color):
        c = fg_color_by(color)
        if c is None:
            c = fg_by(color)
        self.items.get(_id).update(fg=c)
        return self

    def submenu(self, _id, menu):
        self.items.get(_id).update(submenu=menu)
        return self

    def add_action(self, _id, action):
        self.items.get(_id).update(action=action)
        return self

    def move_curser(self, key):
        if is_pressed("UP", key):
            self.hl -= 1 if self.hl > 0 else 0
        elif is_pressed("DOWN", key):
            self.hl += 1 if self.hl < len(self.items) - 1 else 0
        elif is_pressed("ENTER", key):
            sub = self.items.get(self.hl).get("submenu", None)
            if sub is not None:
                self.create(sub.items)
                self.hl = 0
            else:
                return self.items.get(self.hl).get("action", None)

    def _max_option_len(self):
        return max([len(v.get("name")) for v in self.items.values()])

    def _addwhitespace(self, name, w):
        return name + (" " * (w - len(name) - 1))

    def create(self, items=None):
        if items is None:
            items = self.items
        x = self.x
        y = self.y
        w = self._max_option_len() + 1
        h = len(items) + 1
        self.to_draw = [w, h, x, y]
        for i, v in enumerate(items.values()):
            ch = self._addwhitespace(v.get("name"), w)
            fg = v.get("fg")
            posx = x + 1
            posy = y + i + 1
            iterable = (posx, posy, ch, fg)
            self.to_draw.append(iterable)

    def draw(self):
        w, h, x, y, *draw_info = self.to_draw
        draw_brectangle(x, y, w, h, bg=self.bg)
        for i, (x, y, ch, fg) in enumerate(draw_info):
            style = style_by("slow_blink") if i == self.hl else None
            print_at(x, y, ch, style=style, fg=fg, bg=self.bg)
