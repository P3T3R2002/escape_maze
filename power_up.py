from drawable import Circle


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
        self._Power_up__item.win.controller.map()
        super().pick_up(cell)
        
class Destroy(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "blue")
        self.max_num = None

    def pick_up(self, cell):
        if cell.up is not None:
            cell.delete_wall("up")
            cell.up.delete_wall("down")
        if cell.down is not None:
            cell.delete_wall("down")
            cell.down.delete_wall("up")
        if cell.left is not None:
            cell.delete_wall("left")
            cell.left.delete_wall("right")
        if cell.right is not None:
            cell.delete_wall("right")
            cell.right.delete_wall("left")
        super().pick_up(cell)

class Gold(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "yellow")
        self.max_num = None
        
    def pick_up(self, cell):
        self._Power_up__item.win.controller.gold()
        super().pick_up(cell)
    
class Weapon_up(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "gray")
        self.max_num = None

    def pick_up(self, cell):
        self._Power_up__item.win.controller.attack_up()
        super().pick_up(cell)

class Heal(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "red")
        self.max_num = None

    def pick_up(self, cell):
        self._Power_up__item.win.controller.heal_up()
        super().pick_up(cell)




