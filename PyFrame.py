import Tkinter as tk
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