from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, controller):
        self.root = Tk()
        self.root.title = "Maze"
        self.root.geometry(f"{width}x{height}")
        self.root.bind("w", self.move_up)
        self.root.bind("s", self.move_down)
        self.root.bind("a", self.move_left)
        self.root.bind("d", self.move_right)
        self.canvas = Canvas(self.root, width=width, height=height, background = "white")
        self.canvas.pack(fill="both", expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.__close)
        self.controller = controller

    def move_up(self, event):
        self.controller.move_player('up')
    def move_down(self, event):
        self.controller.move_player('down')
    def move_left(self, event):
        self.controller.move_player('left')
    def move_right(self, event):
        self.controller.move_player('right')

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def __close(self):
        self.running = False

