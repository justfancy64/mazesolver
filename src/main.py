from graphics import *
from maze import *

def main():
    win = window(width=500, height=500)
    mz = maze(40,60,10,10,40,40,win)

    win.wait_for_close()



main()