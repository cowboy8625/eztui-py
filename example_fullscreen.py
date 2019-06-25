from TerminalApp import Frame, Tui, safe_run

"""
This is how you get full screen.  
As of right now the program is not dynamically resized.
If you resize window while program is running 
it will try and keep it's original size.
"""


class App:
    def __init__(self, root):
        self.root = root
        self.initUI()

    def initUI(self):
        # window_geometry takes keyword args
        self.root.window_geometry(fullscreen=True)
        self.root.mainloop()


if __name__ == "__main__":
    """
    Using the safe_run insures that your terminal 
    returns to its original state.
    While program is running the curser is 
    disables among other things.  If your program
    crashes safe_run will make sure all is places back as was.
    """
    safe_run(App)
