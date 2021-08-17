import tkinter as tk
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()

canvas_height =20
canvas_width=200

y=int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()

r = tk.Tk()
r.title('Flashcard Application')

button = tk.Button(r, text='Exit Application', width=25, command=r.destroy)
button.pack()
r.mainloop()

def menu_options():

    return
