from tkinter import *
from math import sin, cos, pi
phy = 0
a = 0
after_id = ""
def start_draw():
    global R, r, d

    x0 = int(cvs["width"]) // 2
    y0 = int(cvs["height"]) // 2
    cvs.delete("all") 
    R = int(txt1.get())
    r = int(txt2.get())
    d = int(txt3.get())
    crcl = cvs.create_oval(x0 - R, y0 - R, x0 + R, y0 + R)
    draw_line()

def draw_line():
    global a, after_id, phy

    x0 = int(cvs["width"])//2
    y0 = int(cvs["height"])//2

    xc = x0 + (R + r)  * cos(a)
   
    yc = y0 - (R + r) * sin(a)

    x1 = xc + d * cos(a + phy)
    y1 = yc - d * sin(a + phy)

    a += 0.09
    phy = a * R/r

    xc = x0 + (R + r) * cos(a)
    yc = y0 - (R + r) * sin(a)

    x2 = xc + d * cos(a + phy)
    y2 = yc - d * sin(a + phy)

    cvs.create_line(x1, y1, x2, y2, fill = "blue", width = 2)
    after_id = root.after(10, draw_line)
 
root = Tk()
lab1 = Label(root, text = "R", font = "Ubuntu, 20", bg = "purple", fg = "yellow", width = 10)
lab2 = Label(root, text = "r", font = "Ubuntu, 20", bg = "purple", fg = "yellow", width = 10)
lab3 = Label(root, text = "d", font = "Ubuntu, 20", bg = "purple", fg = "yellow", width = 10)
txt1 = Entry(root, bg = "blue",fg = "white", width = 5, font = "Ubuntu, 20")
txt2 = Entry(root, bg = "blue",fg = "white", width = 5, font = "Ubuntu, 20")
txt3 = Entry(root, bg = "blue",fg = "white", width = 5, font = "Ubuntu, 20")
btn1 = Button(root, text = "Start", font = "Ububuntu, 16", command = start_draw)
cvs = Canvas(root, height = 800, width = 800, bg = "#fff")

txt1.insert(END, 100)
txt2.insert(END, 50)
txt3.insert(END, 50)
lab1.grid(row = 0, column = 0, sticky = "w")
lab2.grid(row = 0, column = 2, sticky = "w")
lab3.grid(row = 0, column = 4, sticky = "w")
txt1.grid(row = 0, column = 1, sticky = "w")
txt2.grid(row = 0, column = 3,  sticky = "w")
txt3.grid(row = 0, column = 5,  sticky = "w")
btn1.grid(row = 1, column = 0, sticky = "ew")
cvs.grid(row = 2, columnspan = 2)

root.mainloop()