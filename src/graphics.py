from tkinter import *

#creating window
class window:
    def __init__(self, height, width):
        self.root = Tk()
        self.root.title("mazesolver")     
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False      
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        print("window closed")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)




class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class line:
    def __init__(self, A, B):
        self.a = A
        self.b = B

    def draw(self, canvas, fill_color):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2 )


class cell:
    def __init__(self, win, x, y):
        self.right_wall = True
        self.left_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.x1 = x
        self.y1 = y
        self.x2 = x + 40
        self.y2 = y - 40
        self.win = win
        self.visited = False
      

    def draw(self):
        if self.right_wall:
            ln = line(point(self.x2,self.y1),point(self.x2, self.y2))
            self.win.draw_line(ln,"black")           
        else:
            ln = line(point(self.x2,self.y1),point(self.x2, self.y2))
            self.win.draw_line(ln,"#d9d9d9")
        if self.left_wall:
            ln = line(point(self.x1, self.y1),point(self.x1, self.y2))
            self.win.draw_line(ln,"black")
        else: 
            ln = line(point(self.x1, self.y1),point(self.x1, self.y2))
            self.win.draw_line(ln,"#d9d9d9")
        if self.top_wall:
            ln = line(point(self.x1, self.y1), point(self.x2, self.y1))
            self.win.draw_line(ln,"black")
        else:
            ln = line(point(self.x1, self.y1), point(self.x2, self.y1))
            self.win.draw_line(ln,"#d9d9d9")
        if self.bottom_wall:
            ln = line(point(self.x1, self.y2), point(self.x2, self.y2))
            self.win.draw_line(ln,"black")
        else:
            ln = line(point(self.x1, self.y2), point(self.x2, self.y2))
            self.win.draw_line(ln,"#d9d9d9")



    def draw_move(self, to_cell, undo=False):
        starting_point = point((self.x1 + 20), (self.y1 - 20))
        end_point = point((to_cell.x1 + 20), (to_cell.y1 - 20))
        ln = line(starting_point, end_point)
        if undo:
            self.win.draw_line(ln, "gray")
        else:
            self.win.draw_line(ln, "red")


    




