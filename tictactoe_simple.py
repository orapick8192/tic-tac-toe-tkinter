from tkinter import *

window = Tk()

def press(button):
    global turn
    if turn == 1:
        b[button].config(text="O")
        turn = 2
    else:
        b[button].config(text="X")
        turn = 1

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ]

turn = 1

# Line setting
line1 = Frame(window)
line1.pack()
line2 = Frame(window)
line2.pack()
line3 = Frame(window)
line3.pack()

# Button Setting
# b00 b10 b20
# b01 b11 b21
# b02 b12 b22
b = {}

b["00"] = Button(line1, width=1, command = lambda: press("00"))
b["01"] = Button(line1, width=1, command = lambda: press("01"))
b["02"] = Button(line1, width=1, command = lambda: press("02"))

b["10"] = Button(line2, width=1, command = lambda: press("10"))
b["11"] = Button(line2, width=1, command = lambda: press("11"))
b["12"] = Button(line2, width=1, command = lambda: press("12"))

b["20"] = Button(line3, width=1, command = lambda: press("20"))
b["21"] = Button(line3, width=1, command = lambda: press("21"))
b["22"] = Button(line3, width=1, command = lambda: press("22"))

b["00"].pack(side=LEFT)
b["01"].pack(side=LEFT)
b["02"].pack(side=LEFT)

b["10"].pack(side=LEFT)
b["11"].pack(side=LEFT)
b["12"].pack(side=LEFT)

b["20"].pack(side=LEFT)
b["21"].pack(side=LEFT)
b["22"].pack(side=LEFT)
 

window.mainloop()
