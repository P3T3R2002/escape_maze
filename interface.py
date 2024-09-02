from drawable import Text

class Interface:
    def __init__(self, pos, win = None) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.win = win
        self.title = Text(win, pos, "Labyrinth")
        self.title.draw()
        self.player = Text(win, (pos[0], pos[1]+35), "Player")
        self.player.draw()

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

