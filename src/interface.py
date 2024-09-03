from drawable import*
from constants import*

    # draw interface
class Interface:
    def __init__(self, win = None) -> None:
        self.x = interface_x
        self.y = interface_y
        self.win = win
        self.title = Text(win, (interface_x, interface_y), "Labyrinth")
        self.title.draw()
        self.player = Text(win, (interface_x, interface_y+35), "Player")
        self.player.draw()
        self.instructions = Instractions(win, (interface_x, interface_y))

    # called by Player/interact/pick_up
    def update_interface(self, player, power_up = None):
        match(power_up):
            case("exp"):
                self.level = Text(self.win, (self.x+20, self.y+60), f"Level: {player.level}")
                self.level.draw()
                self.to_next = Text(self.win, (self.x+20, self.y+80), f"Exp: {player.to_next_level}/{player.exp}")
                self.to_next.draw()
            case("heal"):
                self.hp = Text(self.win, (self.x+20, self.y+100), f"Hp: {player.hp}")
                self.hp.draw()
            case("attack"):
                self.attack = Text(self.win, (self.x+20, self.y+120), f"Attack: {player.attack}")
                self.attack.draw()
            case("gold"):
                self.gold = Text(self.win, (self.x+20, self.y+140), f"Gold: {player.gold}")
                self.gold.draw()
            case("destroy"):
                self.destroy = Text(self.win, (self.x+20, self.y+160), f"Destroy: {player.destroy}")
                self.destroy.draw()
            case(None):
                self.level = Text(self.win, (self.x+20, self.y+60), f"Level: {player.level}")
                self.level.draw()
                self.to_next = Text(self.win, (self.x+20, self.y+80), f"Exp: {player.to_next_level}/{player.exp}")
                self.to_next.draw()
                self.hp = Text(self.win, (self.x+20, self.y+100), f"Hp: {player.hp}")
                self.hp.draw()
                self.attack = Text(self.win, (self.x+20, self.y+120), f"Attack: {player.attack}")
                self.attack.draw()
                self.gold = Text(self.win, (self.x+20, self.y+140), f"Gold: {player.gold}")
                self.gold.draw()
                self.destroy = Text(self.win, (self.x+20, self.y+160), f"Destroy: {player.destroy}")
                self.destroy.draw()
            case _:
                raise Exception("wrong case in Interface/update_interface")

    # called if won
    def won(self):
        Rectangle(self.win, Point(500, 100), Point(1300, 900)).draw("green")
        Text(self.win, (900, 500), "Congratulations\n       You Won")

    # called if lost
    def lose(self):
        Rectangle(self.win, Point(500, 100), Point(1300, 900)).draw("red")
        Text(self.win, (900, 500), "Game Over\n   You Lose")

    # draw instractions
class Instractions:
    def __init__(self, win, pos) -> None:
        Text(win, (pos[0], pos[1]+300), "move up:")
        Text(win, (pos[0]+100, pos[1]+300), "W")
        Text(win, (pos[0], pos[1]+320), "move left:")
        Text(win, (pos[0]+100, pos[1]+320), "A")
        Text(win, (pos[0], pos[1]+340), "move down:")
        Text(win, (pos[0]+100, pos[1]+340), "S")
        Text(win, (pos[0], pos[1]+360), "move right:")
        Text(win, (pos[0]+100, pos[1]+360), "D")
        Text(win, (pos[0], pos[1]+380), "use desrtoy:")
        Text(win, (pos[0]+100, pos[1]+380), "SPACE")
        
        
        Text(win, (pos[0], pos[1]+480), "Player:")
        coord = self.get_coords(pos[0]+50, pos[1]+470)
        Triangle(win, Point(coord[0], coord[1]), Point(coord[2], coord[3]), Point   (coord[4], coord[5])).draw("blue")
        Text(win, (pos[0], pos[1]+520), "Boss:")
        coord = self.get_coords(pos[0]+50, pos[1]+510, True)
        Triangle(win, Point(coord[0], coord[1]), Point(coord[2], coord[3]), Point   (coord[4], coord[5])).draw("purple")
        Text(win, (pos[0], pos[1]+560), "Elit:")
        coord = self.get_coords(pos[0]+50, pos[1]+550, True)
        Triangle(win, Point(coord[0], coord[1]), Point(coord[2], coord[3]), Point   (coord[4], coord[5])).draw("red")
        Text(win, (pos[0], pos[1]+600), "Solder:")
        coord = self.get_coords(pos[0]+50, pos[1]+590, True)
        Triangle(win, Point(coord[0], coord[1]), Point(coord[2], coord[3]), Point   (coord[4], coord[5])).draw("orange")
        Text(win, (pos[0], pos[1]+640), "Grunt:")
        coord = self.get_coords(pos[0]+50, pos[1]+630, True)
        Triangle(win, Point(coord[0], coord[1]), Point(coord[2], coord[3]), Point   (coord[4], coord[5])).draw("yellow")
        
        
        Text(win, (pos[0], pos[1]+680), "Map:")
        Circle(win, Point(pos[0]+50, pos[1]+670), Point(pos[0]+70, pos[1]+690)).draw("green")
        Text(win, (pos[0], pos[1]+720), "Destroy:")
        Circle(win, Point(pos[0]+50, pos[1]+710), Point(pos[0]+70, pos[1]+730)).draw("blue")
        Text(win, (pos[0], pos[1]+760), "Heal:")
        Circle(win, Point(pos[0]+50, pos[1]+750), Point(pos[0]+70, pos[1]+770)).draw("red")
        Text(win, (pos[0], pos[1]+800), "Attack_up:")
        Circle(win, Point(pos[0]+50, pos[1]+790), Point(pos[0]+70, pos[1]+810)).draw("gray")
    
    def get_coords(self, x, y, reverse = False):
        if reverse:
            return x, y, x+10, y+20, x+20, y
        return x+10, y, x, y+20, x+20, y+20


