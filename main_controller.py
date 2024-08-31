from labyrinth import*
from player import*
from interface import*

class GameController:
    def __init__(self):
        self.window = Window(1400, 1000, self)
        self.labyrinth = Labyrinth(500, 100, 20, 20, 40, self.window, 5)
        self.player = Player(5, 2, self.labyrinth, Triangle(self.window))
        self.interface = Interface((100, 100), self.player, self.window)
        self.player.draw_pos()
    
    def move_player(self, direction):
        self.player.move(direction)

    def map(self):
        self.labyrinth.map()
    def gold(self):
        self.player.get_gold()
        self.interface.update_interface("gold")
    def heal_up(self):
        self.player.heal_potion()
        self.interface.update_interface("heal")
    def attack_up(self):
        self.player.wepon_upgrade()
        self.interface.update_interface("attack")

    def wait_for_close(self):
        self.window.running = True
        while self.window.running:
            self.window.redraw()