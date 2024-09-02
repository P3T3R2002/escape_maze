from drawable import Triangle
from constants import*

class Enemy:
    def __init__(self, win, level, hp, attack, cell, color):
        self.level = level
        self.hp = hp
        self.attack = attack
        self.pos = cell
        self.icon = Triangle(win)
        self.icon.set_points(self.get_coords())
        self.exp = self.level*100
        self.color = color

    def draw(self):
        self.icon.set_points(self.get_coords())
        self.icon.draw(self.color)
    
    def get_coords(self):
        return self.pos.rect.point_1.pos[0], self.pos.rect.point_1.pos[1], self.pos.center.pos[0], self.pos.rect.point_2.pos[1], self.pos.rect.point_2.pos[0], self.pos.rect.point_1.pos[1]


class Boss(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, Boss_level, Boss_hp, Boss_attack, pos, "purple")

class Elite(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, Elit_level, Elit_hp, Elit_attack, pos, "red")

class Solder(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, Solder_level, Solder_hp, Solder_attack, pos, "orange")

class Grunt(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, Grunt_level, Grunt_hp, Grunt_attack, pos, "yellow")

