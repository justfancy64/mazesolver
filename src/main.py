from graphics import *

def main():
    #p1= point(5,5)
    #p2= point(5,10)
    win = window(width=500, height=500)
    #ln = line(p1,p2)
    #ln.draw(win.canvas,)
    for i in range(40,400,40):
        starter_cell = cell(i,50,top_wall=True,bottom_wall=True,right_wall=True,left_wall=True)
        starter_cell.draw(win.canvas)

    win.wait_for_close()



main()