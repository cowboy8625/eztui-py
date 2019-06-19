from TUI import Frame, Tui, Shape


class App(Frame):
    """
    How you would use the framework.
    """

    def __init__(self, root):
        self.root = root
        self.clear()
        self.initTUI()

    def initTUI(self):
        self.root.window_geometry(rows=100, cols=30)
        self.shape = Shape().type_of(root, "square")
        self.shape.pack()
        self.root.after(0.3, self.move_shape)
        # self.move_shape()
        self.root.mainloop()

    def move_shape(self):
        # x, y = self.shape.get_location()
        # x += 1
        # y += 1
        # self.shape.place_at(x, y)
        self.root.clear()
        self.shape.move(1, 1)
        self.root.after(0.2, self.move_shape)


if __name__ == "__main__":
    root = Tui()
    app = App(root)
