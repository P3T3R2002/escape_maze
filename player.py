from power_up import*

class Player:
    def __init__(self, hp, attack, maze, triang):
        self.icon = triang
        self.level = 1
        self.hp = hp
        self.attack = attack
        self.gold = 0
        self.maze = maze
        self.pos = maze.get_pos()
        self.destroy = 1
        self.icon.set_points(self.get_coords())
        self.draw_pos()

    def move(self, direction):
        if self.right_dir(direction):
            self.pos.draw()
            match(direction):
                case("up"):
                        self.pos = self.pos.up
                case("down"):
                        self.pos = self.pos.down
                case("left"):
                        self.pos = self.pos.left
                case("right"):
                        self.pos = self.pos.right
                case _:
                    raise Exception("wrong direction in Player/move")
            if self.pos.power_up is not None:
                self.pos.pick_up()   
            self.draw_pos()

    def right_dir(self, dir):
         return not self.pos.walls[dir][1]

    def get_coords(self):
        return self.pos.center.pos[0], self.pos.rect.point_1.pos[1], self.pos.rect.point_1.pos[0], self.pos.rect.point_2.pos[1], self.pos.rect.point_2.pos[0], self.pos.rect.point_2.pos[1]

    def draw_pos(self):
        self.icon.set_points(self.get_coords())
        self.icon.draw("orange")
        self.maze.visible_cells(self.pos)

    def wepon_upgrade(self):
         self.attack += 1

    def heal_potion(self):
         if self.hp < 5:
            self.hp += 1

    def get_gold(self):
         self.gold += 5