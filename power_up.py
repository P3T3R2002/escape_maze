from window import*
from player import Player


class __Power_up:
    def __init__(self, cell, win, color):
        self.__item = Circle(win, cell.rect.point_1, cell.rect.point_2)
        self.__color = color

    def draw(self):
        self.__item.draw(self.__color)

    def __repr__(self) -> str:
        return f"{self.__item} : {self.__color}"

    def pick_up(self):
        pass


class Map(__Power_up):
    def __init__(self, cell, maze, win = None):
        super().__init__(cell, win, "green")
        self.maze = maze
        self.max_num = None

    def pick_up(self):
        self.maze.solve(self.cell)
        
class Destroy(__Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "blue")
        self.max_num = None

class LvL_up(__Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "yellow")
        self.max_num = None
    
class Weapon_up(__Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "gray")
        self.max_num = None

class Heal(__Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "red")
        self.max_num = None






