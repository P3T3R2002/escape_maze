from window import*
from power_up import*
from drawable import*
from enemy import*
import random


class Cell:
    def __init__(self, x1, x2,y1, y2, win = None):
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
        self.power_up = None
        self.enemy = None
        self.exit = False
        self.visited = False
        self.visible = False

    # set wall
    def set_wall(self, wall):
        self.walls[wall][1] = True

    # delete wall
    def delete_wall(self, wall):
        self.walls[wall][1] = False

    # draw walls
    def draw(self, color = "black"):
        if self.visible:
            self.rect.draw("white")
            for wall in self.walls.keys():
                if self.walls[wall][1]:
                    self.walls[wall][0].draw(color)
                else:
                    self.walls[wall][0].draw("white")
            if self.enemy is not None:
                self.enemy.draw()
            elif self.power_up is not None:
                self.power_up.draw()
        else:
            self.rect.draw(color)
    
    #reveals the visible Cells after move
    def visible_cells(self):
        for dir in ["up", "left", "down", "right"]:
            looking_at = self
            while not looking_at.walls[dir][1]:
                if not looking_at.visible:
                    looking_at.visible = True
                    looking_at.draw()
                match(dir):
                    case("up"):
                        looking_at = looking_at.up
                    case("left"):
                        looking_at = looking_at.left
                    case("down"):
                        if not looking_at.exit:
                            looking_at = looking_at.down
                        else:
                            break
                    case("right"):
                        looking_at = looking_at.right
            if not looking_at.visible:
                looking_at.visible = True
                looking_at.draw()

    # create random power_up
    def get_power_up(self, map, gold, destroy, wepon, heal):
        rand = random.randrange(0, 200)
        if rand < 10:
            rand = random.randrange(1, 11)
            match(rand):
                case(1):
                    if not map:
                        self.power_up = Map(self, self.win)
                        return "map"
                case(2):
                    if destroy < max_destroy:
                        self.power_up = Destroy(self, self.win)
                        return "destroy"
                case(3):
                    if destroy < max_destroy:
                        self.power_up = Destroy(self, self.win)
                        return "destroy"
                case(4):
                    if gold < max_gold:
                        self.power_up = Gold(self, self.win)
                        return "gold"
                case(5):
                    if gold < max_gold:
                        self.power_up = Gold(self, self.win)
                        return "gold"
                case(6):
                    if wepon < max_wepon:
                        self.power_up = Weapon_up(self, self.win)
                        return "wepon"
                case(7):
                    if wepon < max_wepon:
                        self.power_up = Weapon_up(self, self.win)
                        return "wepon"
                case(8):
                    if heal < max_heal:
                        self.power_up = Heal(self, self.win)
                        return "heal"
                case(9):
                    if heal < max_heal:
                        self.power_up = Heal(self, self.win)
                        return "heal"
                case(10):
                    if heal < max_heal:
                        self.power_up = Heal(self, self.win)
                        return "heal"
                case _:
                    raise Exception("problem in labyrinth/Cell/get_power_up")
        self.draw()

    # create random enemys
    def get_enemy(self):
        if self.exit:
            self.enemy = Boss(self, self.win)
            return
        rand = random.randrange(1, 100)
        if not self.power_up:
            if rand < 4:
                self.enemy = Grunt(self, self.win)
            elif rand < 6:
                self.enemy = Solder(self, self.win)
            elif rand < 7:
                self.enemy = Elite(self, self.win)

    # destroy walls by desrtoy power_up
    def destroy_walls(self):
        if self.up is not None:
            self.delete_wall("up")
            self.up.delete_wall("down")
        if self.down is not None:
            self.delete_wall("down")
            self.down.delete_wall("up")
        if self.left is not None:
            self.delete_wall("left")
            self.left.delete_wall("right")
        if self.right is not None:
            self.delete_wall("right")
            self.right.delete_wall("left")
        self.draw()

    def __repr__(self):
        return f'{self.walls["up"]}, {self.walls["right"]}, {self.walls["down"]}, {self.walls["left"]}'
