import ctypes
import os

info = "http://ascii-table.com/ansi-escape-sequences-vt-100.php"
info2 = "http://ascii-table.com/ansi-escape-sequences.php"
ESC = "\x1b"


def style_by(name):
    return {
        "reset": "0",
        "bold": "1",
        "faint": "2",
        "italic": "3",
        "underline": "4",
        "slow_blink": "5",
        "rapid_blink": "6",
        "default": "99",
    }.get(name.lower(), None)


def fg_by(name):
    return {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "bright black": "90",
        "bright red": "91",
        "bright green": "92",
        "bright yellow": "93",
        "bright blue": "94",
        "bright magenta": "95",
        "bright cyan": "96",
        "bright white": "97",
    }.get(name.lower(), None)


def bg_by(name):
    return {
        "black": "40",
        "red": "41",
        "green": "42",
        "yellow": "43",
        "blue": "44",
        "magenta": "45",
        "cyan": "46",
        "white": "47",
        "reset": "49",
    }.get(name.lower(), None)


def fg_by(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"


def bg_by(r, g, b):
    return f"\x1b[48;2;{r};{g};{b}m"


def format_color(cell, style=None, fg=None, bg=None):
    end = "\x1b[0m"
    line = ""
    if style is not None:
        style += "m"
    sec = (fg, bg, style, cell, end)
    for s in sec:
        if s is not None:
            line += s
    return line


if os.name == "nt":
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
