from tkinter import*
from math import sin, cos, pi, inf
root = Tk()
root.title("GEOM INTERFACE")


def f1():
    cvs.delete("all")   
    
def MOVE():
    global a, spoke, x0, dx, time
    if x0 + dx + R  >= int(cvs["width"]) or x0 + dx - R <= 0: 
        dx = -dx   
    x1 = x0 + d * cos(a) 
    y1 = y0 - d * sin(a)   
    x0 += dx
    a -= dx/R 
    x2 = x0 + d * cos(a)
    y2 = y0 - d * sin(a)
    cvs.create_line(x1, y1, x2, y2)
    cvs.move(crcl, dx, 0)
    cvs.coords(spoke, x0, y0, x2, y2)
    time = root.after(8, MOVE)   
    
def f2():                     
    global a, da, y0, spoke, d, R, x0, crcl, dx
    cvs.delete("all")
    root.after_cancel(0)
    R = txt1.get()
    dx = 1
    d = txt2.get()
    try:
        R = int(R)
        dx = 1
        d = int(d)
        a = 0                                                    
        x0 = R
        y0 = int(cvs["height"]) - R
        spoke = cvs.create_line(x0, y0, x0 + d, y0, fill = "purple")
        crcl = cvs.create_oval(x0 - R, y0 - R, x0 + R, y0 + R)
        MOVE()
    except ValueError: 
        lab1["text"] = "hmm..."
        lab2["text"] = "numbers please"
        
    
def f3():
    root.after_cancel(time) 
    


    
lab1 = Label(root, text = "print R here", font = "Ubuntu, 20", bg = "lightgrey", fg = "black")
lab2 = Label(root, text = "print d here", font = "Ubuntu, 20", bg = "lightgrey", fg = "black")
txt1 = Entry(root, font = "Ubuntu, 20")
txt2 = Entry(root, font = "Ubuntu, 20")
Button1 = Button(root, text = "STOP", width = 30, command = f3)
Button2 = Button(root, text = "START", width = 30, command = f2)
cvs = Canvas(root, width = 800, height = 200, bg = "white")



lab1.grid(row = 0, column = 0)
lab2.grid(row = 0, column = 1)
txt1.grid(row = 1, column = 0)
txt2.grid(row = 1, column = 1)
Button1.grid(row = 2, column = 0)
Button2.grid(row = 2, column = 1)
cvs.grid(row = 4, column = 0, columnspan = 2)

root.mainloop()