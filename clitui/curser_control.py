import os
import sys


# import appropriate modules and create functions for dealing with cursor
if os.name == "nt":
    """ Windows sub-module for dealing with the console window cursor """

    import ctypes

    class _CursorInfo(ctypes.Structure):
        """ CursorInfo object
        Arguments:
            ctypes {[type]} -- [description]
        """

        _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

    def hide():
        """ Hide the cursor """
        os.system("stty -echo")
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

    def show():
        """ Show the cursor """
        os.system("stty echo")
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))


elif os.name == "posix":
    """ Linux sub-module for dealing with the console window cursor """

    def hide():
        """ Hide the cursor """
        os.system("stty -echo")
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def show():
        """ Show the cursor """
        os.system("stty echo")
        sys.stdout.write("\033[?25h")


sys.stdout.flush()

