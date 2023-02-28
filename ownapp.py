# Source: Code from class
# Create a digital clock app

# Import modules

from tkinter import *
from tkinter.ttk import *
import time

root = Tk()  # create tkinter window
root.title("Digital Clock")  # give window name
root.resizable(0, 0)  # it keeps the gui window fixed
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    weekday = time.strftime("%A")  # New: Gives weekday (Monday, Tuesday, ...)
    day_month = time.strftime("%-d")  # New: Gives day of month
    month_name = time.strftime("%B")  # New: Gives name of month
    timezone = time.strftime("%Z")  # New: Gives timezone

    lbl.config(text=hour + ":" + minute + ":" + second + " " + am_pm)  # Concatenate previously defined variables
    lbl.after(1000, clock)  # Every second it will run the clock function again

    lbl2.config(text= weekday + "," + day_month + " / " + month_name)  # Concatenate previously defined variables

    lbl3.config(text = timezone)  # Display timezone

lbl = Label(root, font=('ds-digital', 60), background='blue', foreground='black')  # Display time in GUI
lbl.pack(pady=20)  # Positioning of time

lbl2 = Label(root, text = "", font=("times-new-roman, 30"))  # Display lbl2 in GUI (Weekday, Day of Month, Month Name)
lbl2.pack(pady=15)  # Positioning of lbl2 in GUI

lbl3 = Label(root, text = "", font=("times-new-roman, 30"))  # Display lbl3 in GUI (timezone)
lbl3.pack(pady=10)  # Positioning of lbl3 in GUI


clock()  # Run clock function

mainloop()
