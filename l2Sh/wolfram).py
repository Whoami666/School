from tkinter import *
from math import sin, cos, pi



def start_draw():
    ymax = int(txtymax.get())
    xmin = int(txtxmin.get())
    xmax = int(txtxmax.get())
    ymin = int(txtymin.get())
    h = int(cvs['height'])
    w = int(cvs['width'])
    mx = w / (xmax - xmin)
    my = h / (ymax - ymin)
    
    y0 = ymax * my
    x0 = -xmin * mx
    
    cvs.create_line(0, y0, w, y0, fill = "green")
    
    
    for x in range(int(xmin) + 1, int(xmax)):
        i = x0 + x * mx
        cvs.create_line(y0 - 2, i, y0 + 2, i)
        cvs.create_text(i + 2, y0 + 10, text=str(x), font='Verdana 10', anchor='nw')
        
    cvs.create_line(x0, h, x0, 0, fill = "green")
    
    for y in range(int(ymin) + 1, int(ymax)):
        i = y0 - y * my
        cvs.create_line(i, x0 - 2, i, x0 + 2,fill = "green")
        if str(y) != '0':
            cvs.create_text(x0 + 10, i + 2, text=str(y), font='Verdana 10', anchor='nw')
    x = xmin
    dx = 0.001
    f = txt1.get()
    
    while x < xmax:
        y = eval(f)
        x1 = x0 + x * mx
        y1 = y0 - y * my
        
        cvs.create_oval(x1, y1, x1, y1, fill="green")
        x += dx


def draw(): dr_lines()

def close(): root.destroy()

#===================================================================================
root = Tk()
txt1 = Entry(root, bg = "blue",fg = "white", width = 6, font = "Ubuntu, 20")
txtxmin = Entry(root, bg = "blue",fg = "white", width = 6, font = "Ubuntu, 20")
txtxmax = Entry(root, bg = "blue",fg = "white", width = 6, font = "Ubuntu, 20")
txtymax = Entry(root, bg = "blue",fg = "white", width = 6, font = "Ubuntu, 20")
txtymin = Entry(root, bg = "blue",fg = "white", width = 6, font = "Ubuntu, 20")

lab1 = Label(root, text = "function", font = "Ubuntu, 18", width = 6, bg = "purple", fg = "yellow")
labxmin = Label(root, text = "xmin", font = "Ubuntu, 18", width = 6, bg = "purple", fg = "yellow")
labxmax = Label(root, text = "xmax", font = "Ubuntu, 18", width = 6, bg = "purple", fg = "yellow")
labymax = Label(root, text = "ymax", font = "Ubuntu, 18", width = 6, bg = "purple", fg = "yellow")
labymin  = Label(root, text = "ymin ", font = "Ubuntu, 18", width = 6, bg = "purple", fg = "yellow")
btn1 = Button(root, text = "îê", font = "Ububuntu, 16", command = start_draw)
cvs = Canvas(root, height = 400, width = 400, bg = "#fff")

txt1.grid(row = 1, column = 2, sticky = "w")
txtxmax.grid(row = 1, column = 0, sticky = "w")
txtxmin.grid(row = 1, column = 1, sticky = "w")
txtymax.grid(row = 1, column = 3, sticky = "w")
txtymin.grid(row = 1, column = 4, sticky = "w")

lab1.grid(row = 0, column = 2, sticky = "w")
labxmax.grid(row = 0, column = 0, sticky = "w")
labxmin.grid(row = 0, column = 1, sticky = "w")
labymax.grid(row = 0, column = 3, sticky = "w")
labymin.grid(row = 0, column = 4, sticky = "w")
btn1.grid(row = 2, column = 0, columnspan = 5, sticky = "ew")

cvs.grid(row = 3, columnspan = 5)
cvs.bind("<Button-1>", start_draw)

root.mainloop()
