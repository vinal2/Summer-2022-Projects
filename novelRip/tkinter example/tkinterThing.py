import sys
import os

sys.path.insert(0, '/Users/CREEP/Downloads/python/novelRip/tkinter example/')
from tkinter import *
from tkinter import messagebox

path = '/Users/CREEP/Downloads/python/novelRip/tkinter example/'

def save_data():
    order = open("Orders.txt", "a")
    order.write("Full Name:\n")
    order.write("%s\n" % name.get())
    order.write("Address:\n")
    order.write("%s\n" % address.get())
    order.write("Province:\n")
    order.write("%s\n" % provincetitle.get())
    order.write("City:\n")
    order.write("%s\n" % city.get())
    order.write("Email:\n")
    order.write("%s\n" % email.get())
    name.delete(0, END)
    address.delete(0, END)
    provincetitle.set("select")
    city.delete(0, END)
    email.delete(0, END)
    
    
def readFile(file, mode):
    fileList = []
    relPath = os.path.join(path, file)
    openFile = open(relPath, mode)
    for line in openFile:
        fileList.append(line.rstrip())
    return fileList

def dropdownbox(file, mode):
    dropdowntitle = StringVar()
    dropdowntitle.set("select")
    itemdrop = readFile(file, mode)
    dropdown = OptionMenu(app, dropdowntitle, *itemdrop)
    dropdown.pack()
    

app = Tk()
app.title('Something apparel')
app.geometry('800x800+200+200')
app.resizable(width = False, height = False)

f = Frame(app, width =800, height = 90, bd = 5, relief = "groove")#creates frame
f.place(relx = 0.00001, rely = 0.002)
f.config(background='white smoke')

formTitle = Label(app, text = "Something apparel", font = 30)
formTitle.pack()
formTitle.place(relx = 0.425, rely = 0.075)

item1dropdown = StringVar()
item1dropdown.set("select")
itemdrop = readFile("sizes.txt", 'r')
dropdown = OptionMenu(app, item1dropdown, *itemdrop).pack()

shipping = Label(app, text = "Shipping Info", font = 30)
shipping.pack()
shipping.place(relx = 0.475, rely = 0.6)

addressTitle = Label(app, text = "Address:")
addressTitle.pack()
addressTitle.place(relx = 0.375, rely = 0.75)

address = Entry(app)
address.pack()
address.place(relx = 0.375, rely = 0.8)

nameTitle = Label(app, text = "Full name: ")
nameTitle.pack()
nameTitle.place(relx = 0.375, rely = 0.65)

name = Entry(app)
name.pack()
name.place(relx = 0.375, rely = 0.7)

provincetitle = StringVar()
provincetitle.set("select")
provincedrop = readFile("provinces.txt", 'r')
province = OptionMenu(app, provincetitle, *provincedrop).pack()

cityTitle = Label(app, text = "City: ")
cityTitle.pack()
cityTitle.place(relx = 0.575, rely = 0.65)

city = Entry(app)
city.pack()
city.place(relx = 0.575, rely = 0.7)

emailTitle = Label(app, text = "Email: ")
emailTitle.pack()
emailTitle.place(relx = 0.575, rely = 0.75)

email = Entry(app)
email.pack()
email.place(relx = 0.575, rely = 0.8)

saveOrder = Button(app, text = "Save", command = save_data)
saveOrder.pack()
saveOrder.place(relx = 0.475, rely = 0.875)

app.mainloop()