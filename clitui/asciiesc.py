from dataclasses import dataclass
import ctypes
import os

info = "http://ascii-table.com/ansi-escape-sequences-vt-100.php"
info2 = "http://ascii-table.com/ansi-escape-sequences.php"
ESC = "\x1b"


def cmd_ascii():
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


@dataclass
class FontColor:
    black: str = f"{ESC}[30m"
    red: str = f"{ESC}[31m"
    green: str = f"{ESC}[32m"
    yellow: str = f"{ESC}[33m"
    blue: str = f"{ESC}[34m"
    magenta: str = f"{ESC}[35m"
    cyan: str = f"{ESC}[36m"
    white: str = f"{ESC}[37m"
    bright_black: str = f"{ESC}[90m"
    bright_red: str = f"{ESC}[91m"
    bright_green: str = f"{ESC}[92m"
    bright_yellow: str = f"{ESC}[93m"
    bright_blue: str = f"{ESC}[94m"
    bright_magenta: str = f"{ESC}[95m"
    bright_cyan: str = f"{ESC}[96m"
    bright_white: str = f"{ESC}[97m"
    reset: str = f"{ESC}[49m"


@dataclass
class Font:
    reset: str = f"{ESC}[0m"
    bold: str = f"{ESC}[1m"
    faint: str = f"{ESC}[2m"
    italic: str = f"{ESC}[3m"
    underline: str = f"{ESC}[4m"
    slow_blink: str = f"{ESC}[5m"
    rapid_blink: str = f"{ESC}[6m"
    default: str = f"{ESC}[99m"


@dataclass
class BackGround:
    black: str = f"{ESC}[40m"
    red: str = f"{ESC}[41m"
    green: str = f"{ESC}[42m"
    yellow: str = f"{ESC}[43m"
    blue: str = f"{ESC}[44m"
    magenta: str = f"{ESC}[45m"
    cyan: str = f"{ESC}[46m"
    white: str = f"{ESC}[47m"
    reset: str = f"{ESC}[49m"


if os.name == "nt":
    cmd_ascii()

bg = BackGround()
fg = FontColor()
font = Font()
RESET = font.reset


def fg_color(color):
    return {
        "black": fg.black,
        "red": fg.red,
        "green": fg.green,
        "yellow": fg.yellow,
        "blue": fg.blue,
        "magenta": fg.magenta,
        "cyan": fg.cyan,
        "white": fg.white,
        "bright black": fg.bright_black,
        "bright red": fg.bright_red,
        "bright green": fg.bright_green,
        "bright yellow": fg.bright_yellow,
        "bright blue": fg.bright_blue,
        "bright magenta": fg.bright_magenta,
        "bright cyan": fg.bright_cyan,
        "bright white": fg.bright_white,
    }.get(color.lower(), None)


def bg_color(color):
    return {
        "black": bg.black,
        "red": bg.red,
        "green": bg.green,
        "yellow": bg.yellow,
        "blue": bg.blue,
        "magenta": bg.magenta,
        "cyan": bg.cyan,
        "white": bg.white,
    }.get(color.lower(), None)
