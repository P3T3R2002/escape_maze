from window import*
from power_up import*
from enemy import*
from cell import*
import time
import random


class Labyrinth:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size,
        win = None,
        power_up_rarity = 0,
    ):
        self.__x = x1
        self.__y = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size = cell_size
        self.power_up_rarity = power_up_rarity
        self.win = win
        self.__found_exit = False
        self.exit = None
        self.__stack = []
        self.__create_cells()

    def __create_cells(self):
        cells = []
        for j in range(0, self.__num_rows):
            row = []
            for i in range(0, self.__num_cols):
                row.append(Cell(i*self.__cell_size + self.__x,
                                i*self.__cell_size + self.__x + self.__cell_size,
                                j*self.__cell_size + self.__y,
                                j*self.__cell_size + self.__y + self.__cell_size,
                                self.win
                                ))
                row[-1].get_power_up(self.power_up_rarity)
                if i == 0 and j == 0:
                    row[-1].draw("purple")
                else:
                    row[-1].draw("gray")
            cells.append(row)
        self.win .draw_text(700, 50, "Escape Labyrinth")
        self.__stack.append(cells[0][0])
        self.__create_graph(cells)
        self.__break_exit()
        self.__break_walls_s()
        self.__reset_visited(cells)

    def __create_graph(self, cells):
        for i in range(0, self.__num_rows):
            for j in range(0, self.__num_cols):
                current = cells[i][j]
                if i-1 in range(0, self.__num_rows) and j in range(0, self.__num_cols):
                    current.top = cells[i-1][j]

                if i+1 in range(0, self.__num_rows) and j in range(0, self.__num_cols):
                    current.bottom = cells[i+1][j]

                if i in range(0, self.__num_rows) and j-1 in range(0, self.__num_cols):
                    current.left = cells[i][j-1]

                if i in range(0, self.__num_rows) and j+1 in range(0, self.__num_cols):
                    current.right = cells[i][j+1]

    def __animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def __break_exit(self):
        temp = self.__stack[-1]
        for i in range(self.__num_rows-1):
            temp = temp.bottom
        for i in range(self.__num_cols-1):
            temp = temp.right
        temp.delete_wall("bottom")
        self.exit = temp
        temp.exit = True

    #for maze generation
    def __break_walls_s(self):
        while len(self.__stack) != 0:
            self.__stack[-1].visited = True
                
            possible_next = self.__add_unvisited_neighbors(self.__stack[-1])
            if possible_next is None:
                self.__stack.pop()
            else:
                self.__move_to_next(possible_next)

    #for maze generation
    def __add_unvisited_neighbors(self, current):
        possible_next = []
        if current.left is not None and not current.left.visited:
            possible_next.append("left")
            
        if current.top is not None and not current.top.visited:
            possible_next.append("top")

        if current.bottom is not None and not current.bottom.visited:
            possible_next.append("bottom")

        if current.right is not None and not current.right.visited:
            possible_next.append("right")

        if len(possible_next) == 0:
            return None
        return possible_next

    #for maze generation 
    def __move_to_next(self, possible_next):
            match(possible_next[random.randrange(0, len(possible_next))]):
                case("top"):
                    self.__stack[-1].delete_wall("top")
                    self.__stack[-1].top.delete_wall("bottom")
                    #self.__animate()
                    self.__stack.append(self.__stack[-1].top)

                case("bottom"):
                    self.__stack[-1].delete_wall("bottom")
                    self.__stack[-1].bottom.delete_wall("top")
                    #self.__animate()
                    self.__stack.append(self.__stack[-1].bottom)

                case("left"):
                    self.__stack[-1].delete_wall("left")
                    self.__stack[-1].left.delete_wall("right")
                    #self.__animate()
                    self.__stack.append(self.__stack[-1].left)

                case("right"):
                    self.__stack[-1].delete_wall("right")
                    self.__stack[-1].right.delete_wall("left")
                    #self.__animate()
                    self.__stack.append(self.__stack[-1].right)

                case _:
                    raise Exception("Problem in Maze/__break_walls_r")
        
    #reset visited
    def __reset_visited(self, cells):      
        self.__stack = [cells[0][0]]
        for i in range(0, self.__num_rows):
            for j in range(0, self.__num_cols):
                cells[i][j].visited = False


    #called by __solve_s maze
    def __get_next_cell(self, current):
        if not current.walls["right"][1] and current.right is not None and not current.right.visited:
            return current.right
        
        if not current.walls["bottom"][1] and current.bottom is not None and not current.bottom.visited:
            return current.bottom

        if not current.walls["left"][1] and current.left is not None and not current.left.visited:
            return current.left

        if not current.walls["top"][1] and current.top is not None and not current.top.visited:
            return current.top
        else:
            return None

    #reveals the visible Cells
    def __visible_cells(self):
        for dir in ["top", "left", "bottom", "right"]:
            looking_at = self.__stack[-1]
            while not looking_at.walls[dir][1]:
                if not looking_at.visible:
                    looking_at.visible = True
                    looking_at.draw()
                match(dir):
                    case("top"):
                        looking_at = looking_at.top
                    case("left"):
                        looking_at = looking_at.left
                    case("bottom"):
                        if not looking_at.exit:
                            looking_at = looking_at.bottom
                        else:
                            break
                    case("right"):
                        looking_at = looking_at.right
            if not looking_at.visible:
                looking_at.visible = True
                looking_at.draw()

    def create_enemy(self):
        self.exit.enemy = Boss(5, 15, 5, self.exit)



    #for the map power_up
    def solve(self, current = None):
        if current is None:
            current = self.__stack[-1]
        self.__solve_s(current)

    #solve the maze
    def __solve_s(self, current):
        self.__stack = [current]
        while not self.__found_exit or len(self.__stack) == 0:
            self.__animate()
            self.__stack[-1].visited = True 
            self.__visible_cells()
            next = self.__get_next_cell(self.__stack[-1])
            if next is None:
                self.__stack[-2].draw_move(self.__stack.pop(), True)
            else:
                self.__stack[-1].draw_move(next)
                self.__stack.append(next)
                if next.exit:
                    self.__found_exit = True
        if self.__found_exit:
            self.__visible_cells()

