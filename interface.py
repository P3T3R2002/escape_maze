from drawable import Text

class Interface:
    def __init__(self, pos, player, win = None) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.win = win
        self.player = player
        self.title = Text(win, pos, "Labyrinth")
        self.title.draw()
        self.the_guy = Text(win, (self.x, self.y+35), "Player:")
        self.the_guy.draw()
        self.hp = Text(win, (self.x+20, self.y+60), f"Hp: {player.hp}")
        self.hp.draw()
        self.attack = Text(win, (self.x+20, self.y+80), f"Attack: {player.attack}")
        self.hp.draw()
        self.gold = Text(win, (self.x+20, self.y+100), f"Gold: {player.gold}")
        self.hp.draw()

    def update_interface(self, power_up):
        match(power_up):
            case("heal"):
                self.hp = Text(self.win, (self.x+20, self.y+60), f"Hp: {self.player.hp}")
                self.hp.draw()
            case("attack"):
                self.attack = Text(self.win, (self.x+20, self.y+80), f"Attack: {self.player.attack}")
                self.attack.draw()
            case("gold"):
                self.gold = Text(self.win, (self.x+20, self.y+100), f"Gold: {self.player.gold}")
                self.gold.draw()
            case _:
                raise Exception("wrong case in Interface/update_interface")

