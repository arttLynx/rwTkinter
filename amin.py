#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  amin.py
#  
#  Copyright 2021 Артем Андреевич <artemandreevich@MacBook-Air-Artem.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import Tkinter as tk
import PyLabel
import PyButton
import PyFrame
import PyTextBox
"""
#window construct
def makeWindow(localTitle, SizeX, SizeY , isMainloop): #mainLoop
    import Tkinter as tk
    global root
    root = tk.Tk()
    root.title(str(localTitle))
    tempx, tempY = int(SizeX), int(SizeY)
    root.geometry('500x500')
    if (bool(isMainloop) == True):
        root.mainloop()
    else:
        return
    #root.mainloop()
def createWindow():
    global root
    root = tk.Tk()
def setTitle(title = "SteamCMD gui"):
    root.title(title)
def setSize(x, y):
    root.geometry('{x}x{y}')
def makeMainLoop():
    root.mainloop()

#GLOBAL FUNC
def SetGrid(someObject,column2, row2):
    someObject.grid(column=column2, row=row2)
    
def pack(someObject):
    #someObject.pack(padx=padX, pady=padY)
    pass

# btn construct
def makeButton(window2, text2): #("Arial Bold", 50)
    btn = tk.Button(window2, text=str(text2))
    btn.pack()
def makeLabel(window2, text2):
    label = tk.Label(window2, text=str(text2))
    label.pack()

# TODO make TextBox construct
makeWindow("Hello", 500, 500, False)
btn = makeButton(root, "hello")
#SetGrid(btn, 1, 2)
label = makeLabel(root, "Hello, world!")
pack(btn)
makeMainLoop()"""
root = PyFrame.makeWindow("hello", 500, 500, False)
btn = PyButton.makeButton(root, "Lessons are done!!")
lbl = PyLabel.makeLabel(root, "Lessons are done forever!")
textBox = PyTextBox.makeTextBox(root,"test", None)
PyFrame.makeMainLoop()