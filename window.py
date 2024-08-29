from tkinter import Tk, BOTH, Canvas
from player import*

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
        self.__controller = controller

    def move_up(self, event):
        self.__controller.move_player('up')
    def move_down(self, event):
        self.__controller.move_player('down')
    def move_left(self, event):
        self.__controller.move_player('left')
    def move_right(self, event):
        self.__controller.move_player('right')

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def __close(self):
        self.running = False


class Point:
    def __init__(self, x, y):
        self.pos = (x, y)
    
    def __repr__(self) -> str:
        return f"{self.pos[0]}:{self.pos[1]}"


class Drawable:
    def __init__(self, win, first, second, third = None) -> None:
        self.win = win
        self.point_1 = first
        self.point_2 = second
        self.point_3 = third

    def draw(self):
        raise Exception("Should not call Drawable/draw")

class Line(Drawable):
    def __init__(self, win, first, second):
        super().__init__(win, first, second)
    
    def draw(self, color):
        self.win.canvas.create_line(self.point_1.pos, self.point_2.pos, fill=color, width=5)

    def __repr__(self) -> str:
        return f"Line: {self.point_1} -> {self.point_2}"

class Circle(Drawable):
    def __init__(self, win, first, second):
        super().__init__(win, first, second)

    def draw(self, color):
        self.win.canvas.create_oval(self.point_1.pos, self.point_2.pos, fill = color)
        
    def __repr__(self) -> str:
        return f"Circle: {self.point_1} -> {self.point_2}"
        
class Triangle(Drawable):
    def __init__(self, win, first = None, second = None, third = None):
        super().__init__(win, first, second, third)
        
    def set_points(self, pos):
        self.point_1 = Point(pos[0], pos[1])
        self.point_2 = Point(pos[2], pos[3])
        self.point_3 = Point(pos[4], pos[5])

    def draw(self, color):
        self.win.canvas.create_polygon(self.point_1.pos, self.point_2.pos, self.point_3.pos, fill=color)
        
    def __repr__(self) -> str:
        return f"Triangle: {self.point_1} -> {self.point_2} -> {self.point_3}"

class Rectangle(Drawable):
    def __init__(self, win, first, second):
        super().__init__(win, first, second)

    def draw(self, color):
        self.win.canvas.create_rectangle(self.point_1.pos, self.point_2.pos, fill=color)
        
    def __repr__(self) -> str:
        return f"Rectangle: {self.point_1} -> {self.point_2}"
    
