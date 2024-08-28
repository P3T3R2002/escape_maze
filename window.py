from tkinter import Tk, BOTH, Canvas, ttk
from player import*

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze"
        self.__root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root, width=width, height=height, background = "white")
        self.canvas.create_window(300, height/2+100, window=ttk.Button(self.__root, text="Down", command=Player.move_down()))
        self.canvas.create_window(150, height/2, window=ttk.Button(self.__root, text="Left", command=Player.move_left()))
        self.canvas.create_window(450, height/2, window=ttk.Button(self.__root, text="Right", command=Player.move_right()))
        self.canvas.create_window(300, height/2-100, window=ttk.Button(self.__root, text="Up", command=Player.move_up()))
        self.canvas.pack(fill="both", expand=True)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.__close)

    def mainloop(self):
        self.__root.mainloop()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

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
    def __init__(self, win, first, second, third):
        super().__init__(win, first, second, third)

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
    
