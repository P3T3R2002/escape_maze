from window import*
from power_up import*
from cell import*
import time
import random


class Labyrinth:
    def __init__(
        self,
        win = None,
    ):
        self.win = win
        self.__x = labyrinth_x
        self.__y = labyrinth_y
        self.__cell_size = cell_size
        self.is_there_map = False
        self.destroy_count = 0
        self.gold_count = 0
        self.wepon_count = 0
        self.heal_count = 0
        self.__found_exit = False
        self.exit = None
        self.start = None
        self.__stack = []
        self.__create_labyrinth()

    # create a labyrinth, called by __init__
    def __create_labyrinth(self):
        self.__create_cells()
        self.__break_walls_s()
        self.power_up()
        self.__loop_to_end(Cell.get_enemy)
        self.__loop_to_end(Cell.draw)

    # called by __create_labyrinth
    def __create_cells(self):
        cells = []
        for j in range(0, row_num):
            row = []
            for i in range(0, col_num):
                row.append(Cell(i*self.__cell_size + self.__x,
                                i*self.__cell_size + self.__x + self.__cell_size,
                                j*self.__cell_size + self.__y,
                                j*self.__cell_size + self.__y + self.__cell_size,
                                self.win
                                ))
            cells.append(row)
        self.start = cells[0][0]
        self.exit = cells[-1][-1]
        self.__stack.append(self.start)
        self.__create_graph(cells)

    # called by __create_cells
    def __create_graph(self, cells):
        for i in range(0, row_num):
            for j in range(0, col_num):
                current = cells[i][j]
                if i-1 in range(0, row_num) and j in range(0, col_num):
                    current.up = cells[i-1][j]

                if i+1 in range(0, row_num) and j in range(0, col_num):
                    current.down = cells[i+1][j]

                if i in range(0, row_num) and j-1 in range(0, col_num):
                    current.left = cells[i][j-1]

                if i in range(0, row_num) and j+1 in range(0, col_num):
                    current.right = cells[i][j+1]

    # for maze generation, called by __create_labyrinth
    def __break_walls_s(self):
        while len(self.__stack) != 0:
            self.__stack[-1].visited = True        
            possible_next = self.__add_unvisited_neighbors(self.__stack[-1])
            if possible_next is None:
                self.__stack.pop()
            else:
                self.__move_to_next(possible_next)
        self.__break_exit()
        
    # for maze generation, called by __break_walls_s
    def __add_unvisited_neighbors(self, current):
        possible_next = []
        if current.left is not None and not current.left.visited:
            possible_next.append("left")
            
        if current.up is not None and not current.up.visited:
            possible_next.append("up")

        if current.down is not None and not current.down.visited:
            possible_next.append("down")

        if current.right is not None and not current.right.visited:
            possible_next.append("right")

        if len(possible_next) == 0:
            return None
        return possible_next

    # for maze generation, called by __break_walls_s
    def __move_to_next(self, possible_next):
            match(possible_next[random.randrange(0, len(possible_next))]):
                case("up"):
                    self.__stack[-1].delete_wall("up")
                    self.__stack[-1].up.delete_wall("down")
                    self.__stack.append(self.__stack[-1].up)

                case("down"):
                    self.__stack[-1].delete_wall("down")
                    self.__stack[-1].down.delete_wall("up")
                    self.__stack.append(self.__stack[-1].down)

                case("left"):
                    self.__stack[-1].delete_wall("left")
                    self.__stack[-1].left.delete_wall("right")
                    self.__stack.append(self.__stack[-1].left)

                case("right"):
                    self.__stack[-1].delete_wall("right")
                    self.__stack[-1].right.delete_wall("left")
                    self.__stack.append(self.__stack[-1].right)

                case _:
                    raise Exception("Problem in Maze/__move_to_next")
                
            if random.randrange(1, 8) == 1:   
                match(random.randrange(1, 5)):
                    case(1):
                        if self.__stack[-1].up is not None:
                            self.__stack[-1].delete_wall("up")
                            self.__stack[-1].up.delete_wall("down")

                    case(2):
                        if self.__stack[-1].down is not None:
                            self.__stack[-1].delete_wall("down")
                            self.__stack[-1].down.delete_wall("up")

                    case(3):
                        if self.__stack[-1].left is not None:
                            self.__stack[-1].delete_wall("left")
                            self.__stack[-1].left.delete_wall("right")

                    case(4):
                        if self.__stack[-1].right is not None:
                            self.__stack[-1].delete_wall("right")
                            self.__stack[-1].right.delete_wall("left")

                    case _:
                        raise Exception("Problem in Maze/__move_to_next")
    
    # called by __break_walls_s
    def __break_exit(self):
        self.exit.exit = True
        self.exit.delete_wall("down")
   
    # helper function to __reset_visited, make_visible, make_power_up, Cell.get_enemy, Cell.draw
    def __loop_to_end(self, func):
        current_row = self.start
        while True:
            current = current_row
            while current.right is not None:
                current = current.right
                ret = func(current)
                if ret is not None:
                    ret(self)
            if current == self.exit:
                break
            current_row = current_row.down
            ret = func(current_row)
            if ret is not None:
                ret(self)
            
    # reveals the maze with __loop_to_end
    def reveal_maze(self):
        self.__loop_to_end(self.make_visible)

    #makes cell visible
    def make_visible(self, current):
        current.visible = True
        current.draw()

    #places pover ups in cells
    def make_power_up(self, cell):
        ret = cell.get_power_up(self.is_there_map, self.gold_count, self.destroy_count, self.wepon_count, self.heal_count)
        if ret is None:
            return
        match(ret):
            case("map"):
                self.is_there_map = True
            case("gold"):
                self.gold_count += 1
            case("destroy"):
                self.destroy_count += 1
            case("wepon"):
                self.wepon_count += 1
            case("heal"):
                self.heal_count += 1
            case _:
                raise Exception("wrong return in Labirinth/make_power_up")

    #loops until the required power ups are met
    def power_up(self):
        while not self.is_there_map or self.destroy_count < min_destroy or self.wepon_count < min_wepon or self.heal_count < min_heal:
            self.__loop_to_end(self.make_power_up)

    # return starting pos to player
    def get_pos(self):
        return self.start

    # for solve(NOT CALLED)
    def __reset_visited(self, cell):  
        cell.visited = False  

    # (NOT CALLED)
    def __animate(self):
        self.win.redraw()
        time.sleep(0.01)

    #for solve_s(NOT CALLED)
    def solve(self, current = None):
        if current is None:
            current = self.start
        self.__loop_to_end(self.__reset_visited)
        self.__solve_s(current)

    #solve the maze(NOT CALLED)
    def __solve_s(self, current, color = "blue"):
        self.__stack = [current]
        while not self.__found_exit or len(self.__stack) == 0:
            self.__animate()
            self.__stack[-1].visited = True
            next = self.__get_next_cell(self.__stack[-1])
            if next is None:
                self.__stack.pop()
            else:
                self.__stack.append(next)
                if next.exit:
                    self.__found_exit = True
        if self.__found_exit:
            current = self.__stack[-1]
            for i in range(len(self.__stack)):
                current.visited = False
                pop = self.__stack.pop()
                current.draw_move(pop, color)
                current = pop

    #called by __solve_s maze(NOT CALLED)
    def __get_next_cell(self, current):
        if not current.walls["right"][1] and current.right is not None and not current.right.visited:
            return current.right
        
        if not current.walls["down"][1] and current.down is not None and not current.down.visited:
            return current.down

        if not current.walls["left"][1] and current.left is not None and not current.left.visited:
            return current.left

        if not current.walls["up"][1] and current.up is not None and not current.up.visited:
            return current.up
        else:
            return None
