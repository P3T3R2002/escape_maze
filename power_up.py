from window import*


class __Power_up:
    def __init__(self, cell, coord, win, color):
        self.coordinate = coord
        self.cell = cell
        self.win = win
        self.color = color

    def draw(self):
        self.win.draw_circle((self.coordinate), self.color)

    def __repr__(self) -> str:
        return f"{self.coordinate} : {self.color}"

class Map(__Power_up):
    def __init__(self, cell, coord, win = None):
        super().__init__(cell, coord, win, "green")
        self.max_num = None

class Destroy(__Power_up):
    def __init__(self, cell, coord, win = None):
        super().__init__(cell, coord, win, "blue")
        self.max_num = None

class LvL_up(__Power_up):
    def __init__(self, cell, coord, win = None):
        super().__init__(cell, coord, win, "yellow")
        self.max_num = None
    
class Weapon_up(__Power_up):
    def __init__(self, cell, coord, win = None):
        super().__init__(cell, coord, win, "gray")
        self.max_num = None

class Heal(__Power_up):
    def __init__(self, cell, coord, win = None):
        super().__init__(cell, coord, win, "red")
        self.max_num = None






