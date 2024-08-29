from main_controller import*



def main():
    game = GameController()
    game.solve()

    game.wait_for_close()

main()