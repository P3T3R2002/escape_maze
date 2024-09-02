
class Point:
    def __init__(self, x, y):
        self.pos = (x, y)
    
    def __repr__(self) -> str:
        return f"{self.pos[0]}:{self.pos[1]}"


class Drawable:
    def __init__(self, win, first, second = None, third = None) -> None:
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
    
class Text(Drawable):
    def __init__(self, win, first, txt) -> None:
        super().__init__(win, first)
        self.txt = txt
        self.draw(False)

    def draw(self, border = True):
        if border:
            self.delete()
        self.win.canvas.create_text(self.point_1, text=self.txt)

    def delete(self):
        self.win.canvas.create_rectangle(self.point_1[0]-50, self.point_1[1]-10, self.point_1[0]+50, self.point_1[1]+10, fill="white")

