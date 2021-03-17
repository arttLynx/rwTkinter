import Tkinter as tk
def makeTextBox(name,window, textvar):
    name = tk.Entry(textvariable=textvar)
    name.pack()