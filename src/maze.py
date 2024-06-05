from graphics import *
import time

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
        
        for col in self.cells:
            for item in col:
                self.animate()
                item.draw()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)


