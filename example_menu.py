from terminalapp import Tui, Frame, Label, mainloop


class MainMenu(Frame):
    def __init__(self, root):
        self.root = root
        self.initUI()

    def initUI(self):
        self.root.window_geometry(fullscreen=True)
        self.label_menu = Label(
            self.root, "StartExit", anchor="center", cols=5, rows=2, boarder=False
        )
        self.label_menu.pack()


if __name__ == "__main__":
    root = Tui()
    app = MainMenu(root)
    mainloop(root)
