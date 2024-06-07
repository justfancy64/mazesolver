from graphics import *
import time
import random

#maze creation
class maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
        ):
        self.x = x1
        self.y = y1
        self.rows = num_rows
        self.cols = num_cols
        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self.win = win
        self.cells = []
        self.create_cells()
        self.break_walls(1,1)


    def create_cells(self):  
        x = self.x
        y = self.y
        for i in range(0, self.cols): 
            rowlst = []
            y = self.y
            for t in range(0, self.rows):
                rowlst.append(cell(self.win, x, y))
                y += self.size_y
            self.cells.append(rowlst)
            x += self.size_x

        self.break_entrance_and_exit()
        
        for col in self.cells:
            for item in col:
                #self.animate()
                item.draw()

    def animate(self):
        self.win.redraw()
        time.sleep(0.01)

    def break_entrance_and_exit(self):
        self.cells[0][0].left_wall = False
        self.cells[-1][-1].right_wall = False


    def break_walls(self, x, y):
        current_cell = self.cells[x][y]
        current_cell.visited = True

        directions = ["top", "bottom", "left", "right"]
        random.shuffle(directions)  # Shuffle to ensure randomness

        for direction in directions:
            nx, ny = x, y

            if direction == "top" and y > 0:
                ny = y - 1
            elif direction == "bottom" and y < self.cols - 1:
                ny = y + 1
            elif direction == "left" and x > 0:
                nx = x - 1
            elif direction == "right" and x < self.rows - 1:
                nx = x + 1

            if self.cells[nx][ny].visited:
                continue

        # Break down walls between the current cell and the chosen cell
            if direction == "top":
                current_cell.top_wall = False
                self.cells[nx][ny].bottom_wall = False
            elif direction == "bottom":
                current_cell.bottom_wall = False
                self.cells[nx][ny].top_wall = False
            elif direction == "left":
                current_cell.left_wall = False
                self.cells[nx][ny].right_wall = False
            elif direction == "right":
                current_cell.right_wall = False
                self.cells[nx][ny].left_wall = False

        # Recursively call to break walls from the new cell
            self.break_walls(nx, ny)

        


        
