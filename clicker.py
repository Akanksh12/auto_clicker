from pynput.mouse import Button, Controller
import tkinter as tk
from time import sleep
from sys import exit

win = tk.Tk()
mouse = Controller()

ld = tk.Label(text="Delay(s)").pack()
e = tk.Entry(text='Delay(S)')
e.pack()

def button():
    sleep(5)
    d = e.get()
    if d == '':
        d = 0

    delay = float(d) 
    while(1 > 0):
        sleep(delay)
        mouse.press(Button.left)
        mouse.release(Button.left)

win.geometry('250x100')
win.wm_title('auto clicker.exe')

b = tk.Button(text="start in 5 sec", command=button).pack()
bs = tk.Button(text="stop!", command=exit).pack()

win.mainloop()
