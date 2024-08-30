from labyrinth import*
from player import*

class GameController:
    def __init__(self):
        self.window = Window(1400, 1000, self)
        self.labyrinth = Labyrinth(500, 100, 20, 20, 40, self.window, 5)
        self.player = Player(5, 2, self.labyrinth, Triangle(self.window))
    
    def move_player(self, direction):
        self.player.move(direction)


    def solve(self, cell):
        self.labyrinth.solve(cell)
        
    def wait_for_close(self):
        self.window.running = True
        while self.window.running:
            self.window.redraw()