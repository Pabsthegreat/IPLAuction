from tkinter import *
root = Tk()
title = Label(root, "Calculator")
title.pack()
e = Entry(root, width=50, borderwidth=5)
e.grid(columnspan=3, row=0,column=0, padx =10, pady =10)
e.pack()
class Buttons:
    def __init__(self) -> None:
        pass