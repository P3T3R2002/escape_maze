from window import *
#from maze_recursion import*
from labyrinth import*
# import only one or the other at one time
# they have the same Maze class name



def main():
    win = Window(1400, 1000)

    labyrinth = Labyrinth(300, 100, 20, 20, 40, win, 5)
    labyrinth.create_enemy()
    labyrinth.solve()


    win.wait_for_close()


main()