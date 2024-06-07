from graphics import *
from maze import *

def main():
    num_rows = 10
    num_cols = 10
    margin = 40
    screen_x = 500
    screen_y = 500
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = window(screen_x, screen_y)

    mz = maze(margin, margin *2 , num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()


main()