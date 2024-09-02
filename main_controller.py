from labyrinth import*
from player import*
from interface import*

class GameController:
    def __init__(self):
        self.window = Window(1400, 1000, self)
        self.labyrinth = Labyrinth(500, 100, 20, 20, 40, self.window)
        self.interface = Interface((100, 100), self.window)
        self.player = Player(4, 2, self.labyrinth, self.interface, Triangle(self.window))
        self.player.draw_pos()
    
    def move_player(self, direction):
        self.player.move(direction)

    def wait_for_close(self):
        self.window.running = True
        while self.window.running:
            self.window.redraw()