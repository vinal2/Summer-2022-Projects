from optparse import Values
import tkinter as tk
from tkinter import END, ttk
import sys
sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')

#GLOBAL VAR
global filePath
filePath = ''
extensionPath = ''
novelTitle = ''

class HoverButton(tk.Button):
    def __init__(self, master, command, text, color, **kw):
        tk.Button.__init__(self,master=master, text=text, command=command, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.text = text
        self.command = command
        self.color = color
        self['bg'] = self.color
        self['text'] = self.text

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
    

window = tk.Tk()
window.geometry('720x540')

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

#path to file
#
def printVal(value):
    print(value)

def getEntryValue(entry, var):
    var = entry.get()
    entry.delete(0, END)
    print(var)

def saveEntryValue(entry, var):
    getEntryValue(entry, var)

def getFileEntryValue(entry, filePath):
    filePath = entry.get()
    entry.delete(0, END)
    print(filePath)

def returnEmptyValues(values):
    index = 0
    indexList = []
    while index < len(values):
        value = values[index]
        if value == '':
            indexList.append(index)
        index += 1
    return indexList
'''for value in values:
        if value == '':
            print("is empty")
            return True'''
def getInput():
    filePath = filePathEntry.get()
    extensionPath = extensionPathEntry.get()
    novelTitle = novelEntry.get()

    global values
    values = [filePath, extensionPath, novelTitle]
    print(values)
    hasEmpty = returnEmptyValues(values)
    if len(hasEmpty) > 0:
        for index in hasEmpty:
            match index:
                case 0:
                    print("0")
                case 1:
                    print('1')
                case 2:
                    print('2')
                case _:
                    print("el trole")


greeting = tk.Label(text="Hello, Tkinter").pack()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="blue")

l1 = ttk.Label(text="Test", style="BW.TLabel").pack()
l2 = ttk.Label(text="Test", style="BW.TLabel").pack()

filePathEntry = tk.Entry(window)
filePathEntry.pack()
extensionPathEntry = tk.Entry(window)
extensionPathEntry.pack()
novelEntry = tk.Entry(window)
novelEntry.pack()
filePathButton = HoverButton(window,text="Enter File Path", command=lambda:getInput(), color= "white", activebackground='#9a7db0')
#filePathButton = HoverButton(window,text="Enter File Path", command=lambda:getFileEntryValue(filePathEntry, filePath), color= "white", activebackground='#9a7db0')
filePathButton.pack()
#extensionButton = HoverButton(window,text="Enter adblock path", command=lambda:getEntryValue(extensionPathEntry, extensionPath), color= "white", activebackground='#9a7db0')
#extensionButton.pack()
#novelTitleButton = HoverButton(window,text="Enter Novel Title", command=lambda:getEntryValue(novelEntry, novelTitle), color= "white", activebackground='#9a7db0')
#novelTitleButton.pack()
#button = HoverButton(window,text="button", command=lambda:print(filePath), color= "white", activebackground='#9a7db0')
#button.pack()
#var = classButton.returnCommand()
#print(var)
submitEntry = tk.Button(window, text = "enter", command=lambda:printVal(filePath))
submitEntry.pack()

window.mainloop()