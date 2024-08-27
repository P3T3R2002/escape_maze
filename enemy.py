class Enemy:
    def __init__(self, level, hp, attack, pos):
        self.level = level
        self.hp = hp
        self.attack = attack
        self.pos = pos

    def draw(self, level, color):
        self.pos.win

class Boss(Enemy):
    def __init__(self, level, hp, attack, pos):
        super().__init__(level, hp, attack, pos)

class Grunt(Enemy):
    def __init__(self, level, hp, attack, pos):
        super().__init__(level, hp, attack, pos)

