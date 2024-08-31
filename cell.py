from window import*
from power_up import*
from drawable import*
import random


class Cell:
    def __init__(self, x1, x2,y1, y2, win = None):
        self.power_up = None
        self.center = Point((x1+x2)/2, (y1+y2)/2)
        self.rect = Rectangle(win, Point(x1, y1), Point(x2, y2))
        self.walls = { "right": [Line(win, Point(x2, y1), Point(x2, y2)), True],
                        "down": [Line(win, Point(x1, y2), Point(x2, y2)), True],
                        "up": [Line(win, Point(x1, y1), Point(x2, y1)), True],
                        "left": [Line(win, Point(x1, y1), Point(x1, y2)), True]
                        }
        self.win = win
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.exit = False
        self.enemy = None
        self.visited = False
        self.visible = False

    def set_wall(self, wall):
        self.walls[wall][1] = True

    def delete_wall(self, wall):
        self.walls[wall][1] = False

    def draw(self, color = "black"):
        if self.visible:
            self.rect.draw("white")
            for wall in self.walls.keys():
                if self.walls[wall][1]:
                    self.walls[wall][0].draw(color)
                else:
                    self.walls[wall][0].draw("white")
            if self.power_up is not None:
                self.power_up.draw()
        else:
            self.rect.draw(color)

    def draw_move(self, to_cell, color):
        Line(self.win, self.center, to_cell.center).draw(color)

    def get_power_up(self, rarity):
        if rarity == 0:
            return
        else:
            rand = random.randrange(1, 100)
            if rand < rarity:
                rand = random.randrange(1, 3)
                match(rand):
                    case(1):
                        self.power_up = Map(self, self.win)
                    case(2):
                        self.power_up = Destroy(self, self.win)
                    case(3):
                        self.power_up = LvL_up(self, self.win)
                    case(4):
                        self.power_up = Heal(self, self.win)
                    case(5):
                        self.power_up = Weapon_up(self, self.win)
                    case _:
                        raise Exception("problem in labyrinth/Cell/get_power_up")

    def pick_up(self):
        self.power_up.pick_up(self)
        self.draw()

    def __repr__(self):
        return f'{self.walls["up"]}, {self.walls["right"]}, {self.walls["down"]}, {self.walls["left"]}'
