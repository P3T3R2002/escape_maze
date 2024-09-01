from power_up import*

class Player:
    def __init__(self, hp, attack, maze, interface, triang):
        self.icon = triang
        self.level = 1
        self.to_next_level = self.level*100
        self.exp = 0
        self.hp = hp
        self.attack = attack
        self.gold = 0
        self.destroy = 1
        self.interface = interface
        self.maze = maze
        self.pos = maze.get_pos()
        self.destroy = 1
        self.icon.set_points(self.get_coords())
        self.draw_pos()
        self.interface.update_interface(self)

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
                self.pos.power_up.pick_up(self.pos, self)
            elif self.pos.enemy is not None:
                self.attack_enemy(self.pos.enemy)
            self.draw_pos()

    def right_dir(self, dir):
         return not self.pos.walls[dir][1]

    def get_coords(self):
        return self.pos.center.pos[0], self.pos.rect.point_1.pos[1], self.pos.rect.point_1.pos[0], self.pos.rect.point_2.pos[1], self.pos.rect.point_2.pos[0], self.pos.rect.point_2.pos[1]

    def draw_pos(self):
        self.icon.set_points(self.get_coords())
        self.icon.draw("orange")
        self.pos.visible_cells()

    def get_destroy(self):
        self.destroy +=1
        self.interface.update_interface(self, "destroy")   

    def destroy_wall(self):
        if self.destroy > 0:
            self.destroy -= 1
            self.interface.update_interface(self, "destroy") 
            self.pos.destroy_walls()
            self.draw_pos()

    def wepon_upgrade(self):
        self.attack += 1
        self.interface.update_interface(self, "attack")   

    def health_potion(self):
        self.hp += 1
        self.interface.update_interface(self, "heal")   

    def get_gold(self):
        self.gold += 5
        self.interface.update_interface(self, "gold") 

    def attack_enemy(self, enemy):
        defeted = False
        while True:
            self.hp -= enemy.attack
            enemy.hp -= self.attack
            if self.hp <= 0:
                defeted = True
                break
            elif enemy.hp <= 0:
                break
        if not defeted:
            self.exp += enemy.exp
            if self.exp > self.to_next_level:
                self.level_up()
            self.interface.update_interface(self)
            self.pos.enemy = None
        self.pos.draw()

    def level_up(self):
        self.level += 1
        self.exp -= self.to_next_level


