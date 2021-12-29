# coding: cp1251
from tkinter import*
from math import sin, cos, pi

root = Tk()


def f1(event):
    global x, y, s, d, n, i, l, t, r, a, x1, y1, cvs
    x, y = event.x, event.y
    d = int(txt2.get())
    n = int(txt1.get())
    try:
        d = int(d)
        n =  int(n)
        cvs.create_line(x, y, x + d, y, fill = "purple")
        x = x + d
        a = 0
        s = "1"
        for i in range(2, n + 1):
            l = s
            t = len(s) // 2
            r = s[:t] + '0' + s[t+1:]
            s = l + '1' + r
        if n != 0:
            for i in s:
                if i == '1':
                    a += pi/2
                else:
                    a -= pi/2
                cvs.create_line(x, y, x + d*cos(a), y - d*sin(a), fill = "red")
                x = x + d*cos(a)
                y = y - d*sin(a)
  

lab1 = Label(root, text = "Ïîðÿäîê", font = "Ubuntu, 20", bg = "purple", fg = "yellow", width = 10)
lab2 = Label(root, text = "Äëèíà", font = "Ubuntu, 20", bg = "purple", fg = "yellow", width = 10)
txt1 = Entry(root, bg = "blue",fg = "white", width = 5, font = "Ubuntu, 20")
txt2 = Entry(root, bg = "blue",fg = "white", width = 5, font = "Ubuntu, 20")
cvs = Canvas(root, height = 400, width = 400, bg = "#fff")


lab1.grid(row = 0, column = 0, sticky = "w")
lab2.grid(row = 0, column = 2, sticky = "w")
txt1.grid(row = 0, column = 1, sticky = "w")
txt2.grid(row = 0, column = 3,  sticky = "w")
cvs.grid(row = 2, columnspan = 2)
cvs.bind("<Button-1>", start_draw)
root.mainloop()
