

class Player:
    def __init__(self, hp, attack, maze, triang):
        self.icon = triang
        self.level = 1
        self.hp = hp
        self.attack = attack
        self.maze = maze
        self.pos = maze.get_pos()
        self.destroy = 1
        self.icon.set_points(self.get_coords())
        self.draw_pos()


    def move_up(self):
        if not self.pos.walls["top"][1]:
            self.pos.draw()
            self.pos = self.pos.top
            self.icon.set_points(self.get_coords())
            self.draw_pos()
            self.maze.visible_cells(self.pos)
        
    def move_down(self):
        if not self.pos.walls["bottom"][1]:
            self.pos.draw()
            self.pos = self.pos.bottom
            self.icon.set_points(self.get_coords())
            self.draw_pos()
            self.maze.visible_cells(self.pos)

    def move_left(self):
        if not self.pos.walls["left"][1]:
            self.pos.draw()
            self.pos = self.pos.left
            self.icon.set_points(self.get_coords())
            self.draw_pos()
            self.maze.visible_cells(self.pos)

    def move_right(self):
        if not self.pos.walls["right"][1]:
            self.pos.draw()
            self.pos = self.pos.right
            self.icon.set_points(self.get_coords())
            self.draw_pos()
            self.maze.visible_cells(self.pos)

    def get_coords(self):
        return self.pos.center.pos[0], self.pos.rect.point_1.pos[1], self.pos.rect.point_1.pos[0], self.pos.rect.point_2.pos[1], self.pos.rect.point_2.pos[0], self.pos.rect.point_2.pos[1]

    def draw_pos(self):
        self.icon.draw("orange")