from tkinter import Label
import tkinter as tk
import PyTouchBar
import time

root = tk.Tk()
PyTouchBar.prepare_tk_windows(root)
lbl = Label(root, text="Button")
lbl1 = PyTouchBar.TouchBarItems.Label(
    text='🥰🥰🥰🥰 T H E   G O O N I E S   ! !  👍🏻👍🏻👍🏻👍🏻')
PyTouchBar.set_touchbar([lbl1])
lbl.pack()
root.mainloop()
