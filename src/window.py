from tkinter import *

class window:
    def __init__(self, txt, height, width):
        self.root = Tk()
        self.root.title("mazesolver")
        self.mylabel = Label(self.root, text =txt)
        self.mylabel.pack()      
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

    def draw(self, canvas, fill_color):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2 )

