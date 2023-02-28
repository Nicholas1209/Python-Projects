# Create a digital clock app

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.resizable(0, 0)  # it keeps the gui window fixed
def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('ds-digital', 80), background='blue', foreground='black')
lbl.pack(anchor='center')
time()

mainloop()
