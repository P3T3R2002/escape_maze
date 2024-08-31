from window import*
from power_up import*
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
        self.start = None
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
                    current.up = cells[i-1][j]

                if i+1 in range(0, self.__num_rows) and j in range(0, self.__num_cols):
                    current.down = cells[i+1][j]

                if i in range(0, self.__num_rows) and j-1 in range(0, self.__num_cols):
                    current.left = cells[i][j-1]

                if i in range(0, self.__num_rows) and j+1 in range(0, self.__num_cols):
                    current.right = cells[i][j+1]

    def __animate(self):
        self.win.redraw()
        time.sleep(0.01)

    def __break_exit(self):
        temp = self.__stack[-1]
        self.start = temp
        for i in range(self.__num_rows-1):
            temp = temp.down
        for i in range(self.__num_cols-1):
            temp = temp.right
        temp.delete_wall("down")
        self.exit = temp
        temp.exit = True

    def get_pos(self):
        return self.__stack[0]

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
            
        if current.up is not None and not current.up.visited:
            possible_next.append("up")

        if current.down is not None and not current.down.visited:
            possible_next.append("down")

        if current.right is not None and not current.right.visited:
            possible_next.append("right")

        if len(possible_next) == 0:
            return None
        return possible_next

    #for maze generation 
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

    #reset visited
    def __reset_visited(self, cells):      
        self.__stack = [cells[0][0]]
        for i in range(0, self.__num_rows):
            for j in range(0, self.__num_cols):
                cells[i][j].visited = False

    #reveals the visible Cells
    def visible_cells(self, pos):
        for dir in ["up", "left", "down", "right"]:
            looking_at = pos
            while not looking_at.walls[dir][1]:
                if not looking_at.visible:
                    looking_at.visible = True
                    looking_at.draw()
                match(dir):
                    case("up"):
                        looking_at = looking_at.up
                    case("left"):
                        looking_at = looking_at.left
                    case("down"):
                        if not looking_at.exit:
                            looking_at = looking_at.down
                        else:
                            break
                    case("right"):
                        looking_at = looking_at.right
            if not looking_at.visible:
                looking_at.visible = True
                looking_at.draw()

    #for solve_s(NOT CALLED)
    def solve(self, current = None):
        if current is None:
            current = self.__stack[-1]
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

    def map(self):
        self.__make_visible()

    def __make_visible(self):
        current_row = self.start
        while True:
            current = current_row
            while current.right is not None:
                current = current.right
                current.visible = True
                current.draw()
            if current == self.exit:
                break
            current_row = current_row.down
            current_row.visible = True
            current_row.draw()


