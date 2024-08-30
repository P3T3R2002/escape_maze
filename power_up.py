from window import Circle


class Power_up:
    def __init__(self, cell, win, color):
        self.__item = Circle(win, cell.rect.point_1, cell.rect.point_2)
        self.__color = color

    def draw(self):
        self.__item.draw(self.__color)

    def __repr__(self) -> str:
        return f"{self.__item} : {self.__color}"

    def pick_up(self, cell):
        cell.power_up = None


class Map(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "green")
        self.max_num = None

    def pick_up(self, cell):
        self._Power_up__item.win.controller.solve(cell)
        super().pick_up(cell)
        
class Destroy(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "blue")
        self.max_num = None

class LvL_up(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "yellow")
        self.max_num = None
    
class Weapon_up(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "gray")
        self.max_num = None

class Heal(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "red")
        self.max_num = None






