from TUI import Frame, Tui, Shape
from TUI.keyboard import getchar


class App(Frame):
    """
    How you would use the framework.
    """

    def __init__(self, root):
        self.root = root
        self.initTUI()

    def initTUI(self):
        self.root.window_geometry(rows=100, cols=30)
        self.shape = Shape().type_of(root, "square")
        self.shape.pack()
        self.move_shape()
        self.root.mainloop()

    def move_shape(self):
        # x, y = self.shape.get_location()
        # x += 1
        # y += 1
        # self.shape.place_at(x, y)
        key = getchar()
        # up
        if key == "w":
            self.root.clear()
            self.shape.move(0, -1)
        # down
        elif key == "s":
            self.root.clear()
            self.shape.move(0, 1)
        # left
        elif key == "a":
            self.root.clear()
            self.shape.move(-1, 0)
        # right
        elif key == "d":
            self.root.clear()
            self.shape.move(1, 0)
        elif key == "q":
            exit()
        self.root.after(0.2, self.move_shape)


if __name__ == "__main__":
    root = Tui()
    app = App(root)
