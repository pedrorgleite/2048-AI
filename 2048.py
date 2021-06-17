import tkinter as tk
GAME_COLOR = "#a6bdbb"
EMPTY_COLOR = "#8eaba8"
EMPTY_CELL_COLOR = "#c2b3a9"
SCORE_LABEL_FONT = ("Verdana", 24)


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        self.main_grid = tk.Frame(master=
            self, bg=GAME_COLOR, bd=4, width=600, height=600
        )
        self.main_grid.grid(pady=(100,0))

        self.mainloop()



Game()