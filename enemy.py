from drawable import Triangle

class Enemy:
    def __init__(self, win, level, hp, attack, cell, exp, color):
        self.level = level
        self.hp = hp
        self.attack = attack
        self.pos = cell
        self.icon = Triangle(win)
        self.icon.set_points(self.get_coords())
        self.exp = exp
        self.color = color

    def draw(self):
        self.icon.set_points(self.get_coords())
        self.icon.draw(self.color)
    
    def get_coords(self):
        return self.pos.rect.point_1.pos[0], self.pos.rect.point_1.pos[1], self.pos.center.pos[0], self.pos.rect.point_2.pos[1], self.pos.rect.point_2.pos[0], self.pos.rect.point_1.pos[1]


class Boss(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, 5, 15, 3, pos, 1000, "red")

class Grunt(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, 1, 2, 1, pos, 100, "purple")

