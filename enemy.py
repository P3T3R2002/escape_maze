class Enemy:
    def __init__(self, level, hp, attack, exp, triangle):
        self.level = level
        self.hp = hp
        self.attack = attack
        self.triangle = triangle
        self.exp = exp

    def draw(self, color):
        self.pos.win

class Boss(Enemy):
    def __init__(self, level, hp, attack, pos):
        super().__init__(level, hp, attack, pos)

class Grunt(Enemy):
    def __init__(self, pos):
        super().__init__(1, 2, 1, 100, pos)

