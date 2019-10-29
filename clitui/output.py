from sys import stdout
from os import system, name


def clear_screen():
    system("cls" if name == "nt" else "clear")


def print_at(text, x, y):
    if isinstance(text, str):
        # if text.find("\n") != -1:
        for index, line in enumerate(text.split("\n")):
            stdout.write(f"\033[{y + index};{x}H{line}")
    else:
        stdout.write(f"\033[{y};{x}H{text}")
    stdout.flush()
