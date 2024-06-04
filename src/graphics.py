from tkinter import *

class window:
    def __init__(self, height, width):
        self.root = Tk()
        self.root.title("mazesolver")     
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
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

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2 )


class cell:
    def __init__(self, x, y, right_wall=False, left_wall=False, top_wall=False, bottom_wall=False):
        self.right_wall = right_wall
        self.left_wall = left_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.x1 = x
        self.y1 = y
        self.x2 = x + 40
        self.y2 = y - 40
      

    def draw(self, canvas):
        if self.right_wall:
            ln = line(point(self.x2,self.y1),point(self.x2, self.y2))
            ln.draw(canvas)
        if self.left_wall:
            ln = line(point(self.x1, self.y1),point(self.x1, self.y2))
            ln.draw(canvas)
        if self.top_wall:
            ln = line(point(self.x1, self.y1), point(self.x2, self.y1))
            ln.draw(canvas)
        if self.bottom_wall:
            ln = line(point(self.x1, self.y2), point(self.x2, self.y2))
            ln.draw(canvas)

    




