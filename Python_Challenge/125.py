from tkinter import *
import random

def click1():
    message = random.randint(1, 6)
    textbox2["text"] = message

def click2():
    message = random.randint(1, 6)
    textbox2["text"] = message

window = Tk()
window.geometry("500x200")

label1 = Label(text="Enter your name:")
label1.place(x=30, y=20)

textbox1 = Entry(text="")
textbox1.place(x=150, y=20, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text='press me', command=click1)
button1.place(x=30, y=80, width=120, height=25)

button2 = Button(text='press me', command=click2)
button2.place(x=30, y=50, width=120, height=25)

textbox2 = Message(text="", width=200)
textbox2.place(x=150, y=50, width=200, height=25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()
