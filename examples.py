from TUI import Frame, Tui, Shape


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
        self.move()
        self.root.mainloop()

    def move(self):
        # up
        self.root.is_pressed("w", self.up)  # key you want to active event, the event
        # down
        self.root.is_pressed("s", self.down)
        # left
        self.root.is_pressed("a", self.left)
        # right
        self.root.is_pressed("d", self.right)
        # exit
        self.root.is_pressed("q", exit)
        self.root.after(0.1, self.move)

    def up(self):
        self.root.clear()
        self.shape.move(0, -1)

    def down(self):
        self.root.clear()
        self.shape.move(0, 1)

    def left(self):
        self.root.clear()
        self.shape.move(-1, 0)

    def right(self):
        self.root.clear()
        self.shape.move(1, 0)


if __name__ == "__main__":
    root = Tui()
    app = App(root)
