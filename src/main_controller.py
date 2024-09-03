from labyrinth import*
from player import*
from interface import*

class GameController:
    def __init__(self):
        self.window = Window(self)
        self.labyrinth = Labyrinth(self.window)
        self.interface = Interface(self.window)
        self.player = Player(self.labyrinth, self.interface, Triangle(self.window))
        self.player.draw_pos()
    
    def move_player(self, func):
        self.player.move(func)

    def wait_for_close(self):
        self.window.running = True
        while self.window.running:
            self.window.redraw()