##-- Imports --##

from os import O_NONBLOCK
from sys import stdin, exit
from termios import tcgetattr, ICANON, TCSANOW, ECHO, TCSAFLUSH, tcsetattr
from fcntl import fcntl, F_SETFL, F_GETFL
from dataclasses import dataclass

##-- Constants --##
class Keys:
    ARROW_UP: str = "\x1b[A"
    ARROW_DOWN: str = "\x1b[B"
    ARROW_RIGHT: str = "\x1b[C"
    ARROW_LEFT: str = "\x1b[D"
    ESC: str = "\x1b"
    ENTER: str = "\n"
    TAB: str = "\t"
    SPACE_BAR: str = " "


##-- Grabs Key --##


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


def is_pressed(key):
    if getchar() == get_ascii(key):
        return True
    else:
        False


def get_ascii(key):
    if len(key) != 0:
        print(f"length: {key}")
        print(f"ascii: {ascii(key)}")
        input("ENTER...")


def main():
    while True:
        key = getchar()
        get_ascii(key)
        if key == KeyAsciiCodes.ESC:
            exit()


def test():
    while True:
        if is_pressed("w"):
            print("Hello")


if __name__ == "__main__":
    test()
