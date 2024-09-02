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
        super().__init__(win, 10, 20, 5, pos, 1000, "purple")

class Elite(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, 6, 9, 3, pos, 600, "red")

class Basic(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, 3, 5, 2, pos, 300, "orange")

class Grunt(Enemy):
    def __init__(self, pos, win):
        super().__init__(win, 1, 2, 1, pos, 100, "yellow")

