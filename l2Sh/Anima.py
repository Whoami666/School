from tkinter import*
from math import sin, cos, pi

root = Tk()
n = 0
m = 0
time = ""
cvs = Canvas(root, width = 0, height = 0)
root.title("Anima")

lab1 = Label(root, text = "Ââåäèòå ðàçìåðû ìàññèâà", font = "Ubuntu, 20",
             bg = "black", 
             fg = "yellow")
lab2 = Label(root, text = "Ââåäèòå R", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab3 = Label(root, text = "Ââåäèòå d", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab4 = Label(root, text = "Ââåäèòå ñêîðîñòü", font = "Ubunty, 20",
             bg = "black", fg = "yellow")
txt2 = Entry(root, font = "Ubuntu, 20")
txt3 = Entry(root, font = "Ubuntu, 20")
v = Entry(root, font = "Ubunty, 20")
tn = Entry(root, font = "Ubuntu, 20")
tm = Entry(root, font = "Ubuntu, 20")

def f1():
    global m, n, cvs
    m = tm.get()
    n = tn.get()
    try:
        cvs.grid_forget()
        n = int(n)
        m = int(m)
        cvs = Canvas(root, width = n, height = m, bg = "white")
        cvs.grid(row = 9, column = 0, columnspan = 2)
    except: showinfo("Îøèáêà", "Ââåäèòå íàòóðàëüíûå ÷èñëà")
    
def f2():
    cvs.delete("all")   
    
def vs():
    global a, time, spoke, x0, dx
    if x0 + dx + R  >= int(cvs["width"]) or x0 + dx - R <= 0: 
        dx = -dx   
    x1 = x0 + d * cos(a) 
    y1 = y0 - d * sin(a)   
    x0 += dx
    a -= dx/R 
    x = x0 + d * cos(a)
    y = y0 - d * sin(a)
    cvs.create_line(x1, y1, x, y)
    cvs.move(crcl, dx, 0)
    cvs.coords(spoke, x0, y0, x, y)
    time = root.after(10, vs)   
    
def f3():                     
    global a, da, y0, spoke, d, R, x0, crcl, dx
    cvs.delete("all")
    root.after_cancel(time)
    R = txt2.get()
    dx = v.get()
    d = txt3.get()
    try:
        R = int(R)
        dx = int(dx)
        d = int(d)
        a = 0                                                    
        x0 = R
        y0 = int(cvs["height"]) - R
        spoke = cvs.create_line(x0, y0, x0 + d, y0, fill = "green", width = 2)
        crcl = cvs.create_oval(x0 - R, y0 - R, x0 + R, y0 + R)
        vs()
    except: showinfo("Îøèáêà", "Ââåäèòå íàòóðàëüíûå ÷èñëà")
    
def f4():
    root.after_cancel(time)
    
def f5():
    root.after_cancel(time)
    vs()
    
def f6():
    root.destroy() 
    
B1 = Button(root, text = "Ñîçäàòü õîëñò", width = "25", command = f1)
B2 = Button(root, text = "Î÷èñòèòü õîëñò",  width = "25", command = f2)
B3 = Button(root, text = "Ñòàðò", width = "25", command = f3)
B4 = Button(root, text = "Ñòîï", width = "25", command = f4)
B5 = Button(root, text = "Ïðîäîëæèòü", width = "25", command = f5)
B6 = Button(root, text = "Âûõîä", width = "25", command = f6)

lab1.grid(row = 0, column = 0, columnspan = 2)
tn.grid(row = 1, column = 0)
tm.grid(row = 1, column = 1)
B1.grid(row = 2, column = 0, columnspan = 2)
lab2.grid(row = 3, column = 0)
lab3.grid(row = 3, column = 1)
txt2.grid(row = 4, column = 0)
txt3.grid(row = 4, column = 1)
B2.grid(row = 5, column = 0, columnspan = 2)
B3.grid(row = 6, column = 0)
B4.grid(row = 6, column = 1)
B5.grid(row = 7, column = 0)
B6.grid(row = 7, column = 1)
lab4.grid(row = 8, column = 0)
v.grid(row = 8, column = 1)
root.mainloop()
