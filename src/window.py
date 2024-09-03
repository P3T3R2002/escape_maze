from tkinter import Tk, BOTH, Canvas
from player import*

class Window:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title = "Maze"
        self.root.geometry(f"{window_width}x{window_height}")
        self.canvas = Canvas(self.root, width=window_width, height=window_height, background = "white")
        self.canvas.pack(fill="both", expand=True)
        self.root.bind("w", self.move_up)
        self.root.bind("s", self.move_down)
        self.root.bind("a", self.move_left)
        self.root.bind("d", self.move_right)
        self.root.bind("<space>", self.destroy)
        self.root.protocol("WM_DELETE_WINDOW", self.__close)
        self.running = False

    # called on keypress
    def move_up(self, event):
        self.controller.move_player(Player.move_up)
    def move_down(self, event):
        self.controller.move_player(Player.move_down)
    def move_left(self, event):
        self.controller.move_player(Player.move_left)
    def move_right(self, event):
        self.controller.move_player(Player.move_right)
    def destroy(self, event):
        self.controller.player.destroy_wall()

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def __close(self):
        self.running = False

