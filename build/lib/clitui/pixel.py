from .asciiesc import RESET, bg_color, fg_color
from .point import Vector2


class Pixel:
    def __init__(self, char, index, fg=None, bg=None):

        self.char = char
        self.index = index
        self.fg = fg
        self.bg = bg

    def __repr__(self):
        return f"Pixel({self.char}, {self.index}, bg={self.bg}, fg={self.fg})"

    def __str__(self):
        if self.bg is not None and self.fg is not None:
            return f"{bg_color(self.bg)}{fg_color(self.fg)}{self.char}{RESET}"
        elif self.bg is not None and self.fg is None:
            return f"{bg_color(self.bg)}{self.char}{RESET}"
        elif self.bg is None and self.fg is not None:
            return f"{fg_color(self.fg)}{self.char}{RESET}"
        else:
            return f"{self.char}"

    def __eq__(self, other):
        if isinstance(other, Pixel):
            return (
                True
                if self.char == other.char
                and self.fg == other.fg
                and self.bg == other.bg
                else False
            )

    def __ne__(self, other):
        if isinstance(other, Pixel):
            return (
                True
                if self.char != other.char or self.fg != other.fg or self.bg != other.bg
                else False
            )

    def __hash__(self):
        return hash((self.char, self.index, self.fg, self.bg))

