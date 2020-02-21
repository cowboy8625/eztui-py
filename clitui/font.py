import ctypes
import os

info = "http://ascii-table.com/ansi-escape-sequences-vt-100.php"
info2 = "http://ascii-table.com/ansi-escape-sequences.php"
ESC = "\x1b"


def style_by(name):
    try:
        name = name.lower()
    except:
        pass
    return {
        "reset": "\x1b[0m",
        "bold": "\x1b[1m",
        "faint": "\x1b[2m",
        "italic": "\x1b[3m",
        "underline": "\x1b[4m",
        "slow_blink": "\x1b[5m",
        "rapid_blink": "\x1b[6m",
        "default": "\x1b[99m",
    }.get(name, None)


def fg_color_by(name):
    try:
        name = name.lower()
    except:
        pass
    return {
        "black": "\x1b[30m",
        "red": "\x1b[31m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[34m",
        "magenta": "\x1b[35m",
        "cyan": "\x1b[36m",
        "white": "\x1b[37m",
        "bright black": "\x1b[90m",
        "bright red": "\x1b[91m",
        "bright green": "\x1b[92m",
        "bright yellow": "\x1b[93m",
        "bright blue": "\x1b[94m",
        "bright magenta": "\x1b[95m",
        "bright cyan": "\x1b[96m",
        "bright white": "\x1b[97m",
    }.get(name, None)


def bg_color_by(name):
    try:
        name = name.lower()
    except:
        pass
    return {
        "black": "\x1b[40m",
        "red": "\x1b[41m",
        "green": "\x1b[42m",
        "yellow": "\x1b[43m",
        "blue": "\x1b[44m",
        "magenta": "\x1b[45m",
        "cyan": "\x1b[46m",
        "white": "\x1b[47m",
        "reset": "\x1b[49m",
    }.get(name, None)


def fg_by(*args):
    try:
        if len(args) == 1:
            r, g, b = args[0]
        else:
            r, g, b = args
        return f"\x1b[38;2;{r};{g};{b}m"
    except:
        return None


def bg_by(*args):
    try:
        if len(args) == 1:
            r, g, b = args[0]
        else:
            r, g, b = args
        return f"\x1b[48;2;{r};{g};{b}m"
    except:
        return None


def format_color(cell, style=None, fg=None, bg=None):
    end = "\x1b[0m"
    line = ""
    sec = (fg, bg, style, cell, end)
    for s in sec:
        if s is not None:
            line += s
    return line


if os.name == "nt":
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
