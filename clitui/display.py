from math import cos, sin, radians
from sys import stdout, stdin, exit
from fcntl import fcntl, F_SETFL, F_GETFL
from os import system, name, O_NONBLOCK
from termios import tcgetattr, ICANON, TCSANOW, ECHO, TCSAFLUSH, tcsetattr
from textwrap import wrap

from .font import fg_by, bg_by, format_color, style_by
from .curser_control import hide, show


def print_at(x, y, ch, style=None, fg=None, bg=None):
    char = f"\x1b[{y};{x}H{format_color(ch, style=style, bg=bg, fg=fg)}"
    print(*char, sep="", end="", file=stdout, flush=False)


def clear():
    system("cls" if name == "nt" else "clear")


def safe_run(func):
    # clear()
    hide()
    try:
        func()
    except Exception as e:
        print(e)
    finally:
        # clear()
        show()


def getchar(keys_len=5):
    fd = stdin.fileno()

    oldterm = tcgetattr(fd)
    newattr = tcgetattr(fd)
    newattr[3] = newattr[3] & ~ICANON & ~ECHO
    tcsetattr(fd, TCSANOW, newattr)

    oldflags = fcntl(fd, F_GETFL)
    fcntl(fd, F_SETFL, oldflags | O_NONBLOCK)

    try:
        while True:
            try:
                key = stdin.read(keys_len)
                break
            except IOError:
                pass
    finally:
        tcsetattr(fd, TCSAFLUSH, oldterm)
        fcntl(fd, F_SETFL, oldflags)
    return key


def is_pressed(looking, key):
    k = {
        "UP": "\x1b[A",
        "DOWN": "\x1b[B",
        "RIGHT": "\x1b[C",
        "LEFT": "\x1b[D",
        "ESC": "\x1b",
        "ENTER": "\n",
        "TAB": "\t",
        "BAR": " ",
    }.get(looking, None)
    if key == k:
        return True
    elif looking == key:
        return True
    else:
        return False


##-- Style --##


def boarder_char(name, style=0):
    return {
        "h": [chr(9552), chr(9472), chr(9473)],
        "v": [chr(9553), chr(9474), chr(9475)],
        "lt": [chr(9571), chr(9508), chr(9515)],
        "rt": [chr(9568), chr(9500), chr(9507)],
        "tt": [chr(9574), chr(9516), chr(9523)],
        "bt": [chr(9577), chr(9524), chr(9531)],
        "tlc": [chr(9556), chr(9581), chr(9487)],
        "trc": [chr(9559), chr(9582), chr(9491)],
        "blc": [chr(9562), chr(9584), chr(9495)],
        "brc": [chr(9565), chr(9583), chr(9499)],
        "ls": ["/", "/", "/"],
        "rs": ["\\", "\\", "\\"],
        "+": [chr(9580), chr(9532), chr(9547)],
    }.get(name, None)[style]


##-- algorithems --##


def gen_points(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
        if D >= 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy


def _create_points(x, y, r, min_a, max_a):
    for i in range(int(max_a / min_a)):
        yield _point_on_circle(x, y, r, radians(min_a * i))


def _point_on_circle(x, y, r, angle):
    x = x + r * cos(angle)
    y = y + r * sin(angle)
    return (round(x), round(y))


##-- Drawing Helpers? --##


def draw_line(
    x0=None, y0=None, x1=None, y1=None, pos0=None, pos1=None, ch="#", fg=None, bg=None
):
    if None in (x0, y0):
        x0, y0 = pos0.x, pos0.y
    if None in (x1, y1):
        x1, y1, = pos1.x, pos1.y

    for x, y in gen_points(x0, y0, x1, y1):
        print_at(x, y, ch=ch, fg=bg, bg=bg)


def draw_circle(x, y, r, ch="#", fg=None, bg=None):
    for x, y in _create_points(x, y, r, 1, 360):
        print_at(x, y, ch=ch, fg=bg, bg=bg)


def draw_rectangle(x, y, w, h, ch="#", fg=None, bg=None):
    points = (
        (x, y, x + w, y),
        (x, y + h, x + w, y + h),
        (x, y, x + 0, y + h),
        (x + w, y, x + w, y + h),
    )
    for x0, y0, x1, y1 in points:
        draw_line(x0=x0, y0=y0, x1=x1, y1=y1, ch=ch, fg=fg, bg=bg)


def draw_brectangle(x, y, w, h, outline=0, ch="#", fg=None, bg=None):
    points = (
        (x + 1, y, x + w - 1, y),
        (x + 1, y + h, x + w - 1, y + h),
        (x, y + 1, x + 0, y + h - 1),
        (x + w, y + 1, x + w, y + h - 1),
    )
    for idx, (x0, y0, x1, y1) in enumerate(points):
        s = boarder_char("h", outline) if idx <= 1 else boarder_char("v", outline)
        draw_line(x0=x0, y0=y0, x1=x1, y1=y1, ch=s, fg=fg, bg=bg)

    # Top Left Corner
    char = boarder_char("tlc", outline)
    print_at(x, y, ch=char, fg=bg, bg=bg)

    # Bottom Left Corner
    char = boarder_char("blc", outline)
    print_at(x, y + h, ch=char, fg=bg, bg=bg)

    # Top Right Corner
    char = boarder_char("trc", outline)
    print_at(x + w, y, ch=char, fg=bg, bg=bg)

    # Bottom Right Corner
    char = boarder_char("brc", outline)
    print_at(x + w, y + h, ch=char, fg=bg, bg=bg)


def label(text, x, y, w=5, h=5, boarder=True, outline=0, style=None, fg=None, bg=None):
    text = wrap(text, w)
    w += 1
    h = len(text) + 1
    if boarder:
        draw_brectangle(x, y, w, h, outline=outline)
    for i, line in enumerate(text):
        print_at(x + 1, y + 1 + i, line, style=style, fg=fg, bg=bg)
