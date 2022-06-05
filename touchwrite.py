from tkinter import Label
import tkinter as tk
import PyTouchBar
import time

root = tk.Tk()
PyTouchBar.prepare_tk_windows(root)
lbl = Label(root, text="Button")
lbl1 = PyTouchBar.TouchBarItems.Label(
    text='🥰🥰🥰🥰  W E L C O M E   T O   T H E   C O D E  !!  👍🏻👍🏻👍🏻👍🏻')
PyTouchBar.set_touchbar([lbl1])
lbl.pack()
root.mainloop()
