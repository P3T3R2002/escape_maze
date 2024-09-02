from drawable import Circle


class Power_up:
    def __init__(self, cell, win, color):
        self.__item = Circle(win, cell.rect.point_1, cell.rect.point_2)
        self.__color = color

    def draw(self):
        self.__item.draw(self.__color)

    def pick_up(self, cell):
        cell.power_up = None
        cell.draw()

    def __repr__(self) -> str:
        return f"{self.__item} : {self.__color}"


class Map(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "green")

    def pick_up(self, cell, player):
        player.maze.reveal_maze()
        super().pick_up(cell)
        
class Destroy(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "blue")

    def pick_up(self, cell, player):
        player.get_destroy()
        super().pick_up(cell)

class Gold(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "yellow")
        
    def pick_up(self, cell, player):
        player.get_gold()
        super().pick_up(cell)
    
class Weapon_up(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "gray")

    def pick_up(self, cell, player):
        player.wepon_upgrade()
        super().pick_up(cell)

class Heal(Power_up):
    def __init__(self, cell, win = None):
        super().__init__(cell, win, "red")

    def pick_up(self, cell, player):
        player.health_potion()
        super().pick_up(cell)




