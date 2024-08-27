from window import*
from power_up import*
import random


class Cell:
    def __init__(self, x1, x2,y1, y2, win = None):
        self.power_up = None
        self.center = Point((x1+x2)/2, (y1+y2)/2)
        self.coordinate = ((x1, y1), (x2, y2))
        self.walls = { "right": [Line(Point(x2, y1), Point(x2, y2)), True],
                        "bottom": [Line(Point(x1, y2), Point(x2, y2)), True],
                        "top": [Line(Point(x1, y1), Point(x2, y1)), True],
                        "left": [Line(Point(x1, y1), Point(x1, y2)), True]
                        }
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None
        self.win = win
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
            if not self.visited:
                self.win.draw_rectangle(self.coordinate, "white")
            for wall in self.walls.keys():
                if self.walls[wall][1]:
                    self.win.draw_line(self.walls[wall][0], color)
                else:
                    self.win.draw_line(self.walls[wall][0], "white")
            if self.power_up is not None:
                self.power_up.draw()
        else:
            self.win.draw_rectangle(self.coordinate, color)

    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        if undo:
            self.win.draw_line(line, "white")
        else:
            self.win.draw_line(line, "blue")

    def get_power_up(self, rarity):
        if rarity == 0:
            return
        else:
            rand = random.randrange(1, 100)
            if rand < rarity:
                rand = random.randrange(1, 6)
                match(rand):
                    case(1):
                        self.power_up = Map(self, self.coordinate, self.win)
                    case(2):
                        self.power_up = Destroy(self, self.coordinate, self.win)
                    case(3):
                        self.power_up = LvL_up(self, self.coordinate, self.win)
                    case(4):
                        self.power_up = Heal(self, self.coordinate, self.win)
                    case(5):
                        self.power_up = Weapon_up(self, self.coordinate, self.win)
                    case _:
                        raise Exception("problem in labyrinth/Cell/get_power_up")

    def __repr__(self):
        return f'{self.walls["top"]}, {self.walls["right"]}, {self.walls["bottom"]}, {self.walls["left"]}'
