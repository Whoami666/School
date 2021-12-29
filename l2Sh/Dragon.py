from tkinter import *
from math import sin, cos, pi

def start_draw(event):
    
   x = event.x                   
   y = event.y
   try:
      n = int(txt1.get())
      d = int(txt2.get())   
      S = "1"
      for i in range(2, n + 1):
         L = S
         t = len(S)//2
         R = S[:t] + '0' + S[t + 1:]
         S = L + '1' + R    
      
   
      cvs.create_line(x, y, x + d, y, fill = "blue")
      x = x + d
      a = 0
      if n != 0:
         for i in S:
            if i == '1':
               a += pi/2
            else:
               a -= pi/2
            cvs.create_line(x, y, x + d*cos(a), y - d*sin(a), fill = "red")
            x = x + d*cos(a)
            y = y - d*sin(a) 
      else:
         cvs.create_line(x, y, x + d, y, fill = "blue")
   except ValueError: 
      lab1["text"] = "hmm..."
      lab2["text"] = "no numbers"
   

root = Tk()
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
