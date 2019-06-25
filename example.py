from CommandLineApp import Frame, Tui, safe_run, Label


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
            style=2,
        )
        self.label_player_update = Label(
            self.root,
            "Welcome to my text RPG",
            anchor=(2, 2),
            cols=40,
            rows=10,
            style=1,
        )
        self.label_move.pack()
        self.label_player_update.pack()
        self.root.mainloop()


if __name__ == "__main__":
    root = Tui()
    app = App(root)
    # safe_run(App)
