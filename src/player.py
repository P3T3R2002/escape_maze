from power_up import*
from constants import*

class Player:
    def __init__(self, maze, interface, triang):
        self.icon = triang
        self.level = 1
        self.to_next_level = self.level*100
        self.exp = 0
        self.hp = player_hp
        self.attack = player_attack
        self.gold = 0
        self.destroy = 1
        self.interface = interface
        self.maze = maze
        self.won = False
        self.pos = maze.get_pos()
        self.icon.set_points(self.get_coords())
        self.draw_pos()
        self.interface.update_interface(self)

    # calls move_'direction' and pick_up
    def move(self, func):
        if not self.won:
            func(self)
            if not self.won:
                self.interact()
                self.draw_pos()

    # called by move
    def move_up(self):
        if not self.pos.walls["up"][1]:
            self.pos.draw()
            self.pos = self.pos.up
    def move_down(self):
        if not self.pos.walls["down"][1]:
            self.pos.draw()
            if self.pos.exit:
                self.win = True
                self.interface.won()
                return
            self.pos = self.pos.down
    def move_left(self):
        if not self.pos.walls["left"][1]:
            self.pos.draw()
            self.pos = self.pos.left
    def move_right(self):
        if not self.pos.walls["right"][1]:
            self.pos.draw()
            self.pos = self.pos.right

    # called by move
    def interact(self):
        if self.pos.power_up is not None:
            self.pos.power_up.pick_up(self.pos, self)
        elif self.pos.enemy is not None:
            self.attack_enemy(self.pos.enemy)

    # called by interact/pick_up
    def get_destroy(self):
        self.destroy +=1
        self.interface.update_interface(self, "destroy")   
    def wepon_upgrade(self):
        self.attack += 1
        self.interface.update_interface(self, "attack")   
    def health_potion(self):
        self.hp += 1
        self.interface.update_interface(self, "heal")   
    def get_gold(self):
        self.gold += 5
        self.interface.update_interface(self, "gold") 

    # called by interact
    def attack_enemy(self, enemy):
        if enemy.hp*2 > self.attack:
            while True:
                self.hp -= enemy.attack
                enemy.hp -= self.attack
                self.interface.update_interface(self, "heal")
                if self.hp <= 0:
                    self.won = True
                    self.interface.lose()
                    return
                elif enemy.hp <= 0:
                    break
        self.exp += enemy.exp
        if self.exp >= self.to_next_level:
            self.level_up()
        self.interface.update_interface(self, "exp")
        self.pos.enemy = None
        self.pos.draw()

    # called by attack_enemy
    def level_up(self):
        self.level += 1
        self.hp += 1
        self.attack += 1
        self.interface.update_interface(self, "heal")
        self.interface.update_interface(self, "attack")
        self.exp -= self.to_next_level
        self.to_next_level = self.level*100
        if self.to_next_level <= self.exp:
            self.level_up()

    # draw player
    def draw_pos(self):
        self.icon.set_points(self.get_coords())
        self.icon.draw("blue")
        if not self.won:
            self.pos.visible_cells()

    # called by draw_pos
    def get_coords(self):
        return self.pos.center.pos[0], self.pos.rect.point_1.pos[1], self.pos.rect.point_1.pos[0], self.pos.rect.point_2.pos[1], self.pos.rect.point_2.pos[0], self.pos.rect.point_2.pos[1]

    # use destroy power_up
    def destroy_wall(self):
        if self.destroy > 0:
            self.destroy -= 1
            self.interface.update_interface(self, "destroy") 
            self.pos.destroy_walls()
            self.draw_pos()


