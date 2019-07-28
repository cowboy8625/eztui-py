from terminalapp import Frame, Label, Tui, mainloop


class App(Frame):
    def __init__(self, root):
        self.root = root
        self.initUI()

    def initUI(self):
        self.root.window_geometry(cols=100, rows=30)
        self.label = Label(self.root, "Hello World", anchor=(1, 1), cols=20, rows=4)
        self.label.pack()


if __name__ == "__main__":
    root = Tui()
    app = App(root)
    mainloop(root)

