from terminalapp import Frame, Tui, Label, mainloop

##-- Constaints --##


##-- Main App Class --##
class App(Frame):
    def __init__(self, root):

        self.root = root
        self.initUI()

    def initUI(self):
        self.root.window_geometry(fullscreen=True)
        self.label_move = Label(
            self.root,
            "W - up   A - left S - down D - right",
            anchor=(2, -8),
            cols=11,
            rows=6,
            style=1,
            # bg=green,
        )
        self.label_player_update = Label(
            self.root,
            "Welcome to my text RPG",
            anchor=(2, 1),
            cols=40,
            rows=10,
            style=1,
        )
        self.label_map = Label(
            self.root, "Map", anchor=(79, 1), cols=60, rows=35, style=1
        )
        self.label_map.pack()
        self.label_move.pack()
        self.label_player_update.pack()
        self.root.mainloop()


if __name__ == "__main__":
    root = Tui()
    app = App(root)
    mainloop(root)
