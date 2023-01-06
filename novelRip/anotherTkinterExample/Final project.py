from tkinter import *
from tkinter import messagebox
import sys
import os

sys.path.insert(0, '/Users/CREEP/Downloads/python/novelRip/anotherTkinterExample/')
path = '/Users/CREEP/Downloads/python/novelRip/tkinter example/'
#https://drive.google.com/drive/folders/1NLhcD67jYJKnpqfIkuX6dxs2Z9hJslWn?usp=sharing
#this is the google drive with the file backed up if the zip file is broken and the program does not work

def save_data():
    if name.get() == "" or address.get() == "" or provincetitle.get() == "" or city.get() == "" or email.get() == "" or cart.get(0) == "" or postCode.get() == "":
        #if any of the entry boxes are empty, then it will have a pop up saying that there is missing information and not save the information
        messagebox.showerror(title = "Missing Information!", message = "Missing shipping information or your cart is empty")
    else:
        order = open("Orders.txt", "a") #opens the order text file
        order.write("\n---------------------------------\n\nFull Name:\n")
        #writes all the name/shipping information, as well as every line of what is in the listbox
        order.write("%s\n" % name.get())
        order.write("Email:\n")
        order.write("%s\n" % email.get())
        order.write("Address:\n")
        order.write("%s\n" % address.get())
        order.write("Province:\n")
        order.write("%s\n" % provincetitle.get())
        order.write("City:\n")
        order.write("%s\n" % city.get())
        order.write("Postal Code:\n")
        order.write("%s\n" % postCode.get())
        order.write("Order:\n")
        for x in cart.get(0, END): #for every line in the listbox for the cart, it will write the item and then \n
            order.write(str(x) + "\n")
        #deletes all the info in each entry field after
        name.delete(0, END)
        address.delete(0, END)
        provincetitle.set("")
        city.delete(0, END)
        email.delete(0, END)
        postCode.delete(0, END)
        #runs the deletelist() function to delete all of the item information and previous item settings
        deletelist()
        #shows a messagebox that displays a successful order
        messagebox.showinfo(title = "Successful order", message = "Your order has been placed!") 

def readFile(file, mode):
    fileList = []
    relPath = os.path.join(path, file)
    openFile = open(relPath, mode)
    for line in openFile:
        fileList.append(line.rstrip())
    return fileList
    
def deletelist():
    #deletes everything in the cart, as well as the quantity of every item, and size
    cart.delete(0, END)
    pineapplebunquantity.delete(0, END)
    cocobunquantity.delete(0, END)
    hotdogquantity.delete(0, END)
    #resets the quantity to 1
    pineapplebunquantity.insert(0, "1")
    cocobunquantity.insert(0, "1")
    hotdogquantity.insert(0, "1")
    #resets every item size to blank
    item1dropdown.set("")
    item2dropdown.set("")
    item3dropdown.set("")
    
def addtocart(item):
    cartlist = []
    cartlist.append(item) #appends the item from the parameter to the cartlist
    for item in cartlist:
        cart.insert(0, item) #inserts the item into the cart listbox
        
#title/window of the app
    
app = Tk()
app.title('Something apparel')
app.geometry('800x800')
app.resizable(width = False, height = False) #sets resizable false so the window isnt able to be skewed in any way

#frame background

f = Frame(app, width =800, height = 90, bd = 5, relief = "groove")#creates frame to fit the window
f.place(relx = 0.00001, rely = 0.002)
f.config(background='white smoke') 

#label of store

formTitle = Label(app, text = "Macksims Baking Delivery", font = 30)
formTitle.pack()
formTitle.place(relx = 0.425, rely = 0.075)

#show cart

cartTitle = Label(app, text = "Your Order", font = 20)
cartTitle.pack()
cartTitle.place(relx = 0.075, rely = 0.65)

#creates a listbox to store every item in the cart

cart = Listbox(app, width = 30)
cart.pack()
cart.place(relx = 0.075, rely = 0.7)

#delete item

deleteitem = Button(app, text = "Delete list", command = deletelist) #runs the deletelist function to reset every item and list
deleteitem.pack()
deleteitem.place(relx = 0.075, rely = 0.925)

#item 1 image

photo = PhotoImage(file = r"C:\Users\CREEP\Downloads\python\novelRip\anotherTkinterExample\pineapplebun.png") #makes a photo with a solid black border
item1 = Label(app, image = photo, bd = 3, relief = "solid")
item1.photo = photo
item1.pack(padx = 10, pady = 18) #makes a padding for the photo
item1.place(relx = 0.01, rely = 0.125)

#item 1 dropdown for size

item1dropdown = StringVar()
item1dropdown.set("")
itemdrop = readFile("sizes.txt", 'r') #imports the sizes from the text file and sets the dropdown to be blank
dropdown = OptionMenu(app, item1dropdown, *itemdrop) #creates and places the dropdown 
dropdown.pack()
dropdown.place(relx = 0.2125, rely = 0.4625)

#item 1 price/quantity

pineapplebun = Label(app, text = "Pineapple Bun: packs of 3", font = 30)
pineapplebun.pack()
pineapplebun.place(relx = 0.05, rely = 0.4)

#quantity of the item 

pineapplebunquantitytitle = Label(app, text = "Quantity: ", font = 20)
pineapplebunquantitytitle.pack()
pineapplebunquantitytitle.place(relx = 0.0775, rely = 0.45)

#user entry for the custom quantity of the item preset to 1

pineapplebunquantity = Entry(app)
pineapplebunquantity.insert(0, "1")
pineapplebunquantity.pack()
pineapplebunquantity.place(relx = 0.05, rely = 0.475)

#sets the base price for the price of the item

pineapplebunpricetitle = Label(app, text = "Price: ", font = 20)
pineapplebunpricetitle.pack()
pineapplebunpricetitle.place(relx = 0.0775, rely = 0.5)

pineapplebunprice = Label(app, text = "$1.40", font = 20)
pineapplebunprice.pack()
pineapplebunprice.place(relx = 0.0775, rely = 0.525)

#makes an add to cart button that calls the addtocart function to write into the listbox the item, quantity and size of the item

pineapplebuntocart = Button(app, text = "Add to cart", command = lambda:addtocart(pineapplebunquantity.get() + " x " + item1dropdown.get() + " pineapple buns"))
pineapplebuntocart.pack()
pineapplebuntocart.place(relx = 0.0775, rely = 0.55)

#item 2 image

photo = PhotoImage(file = r"C:\Users\CREEP\Downloads\python\novelRip\anotherTkinterExample\cocobun.png")
item1 = Label(app, image = photo, bd = 3, relief = "solid") #creates a border for the image
item1.photo = photo
item1.pack(padx = 10, pady = 18)
item1.place(relx = 0.35, rely = 0.125)

#item 2 dropdown (follows the same logic as the other dropdown)

item2dropdown = StringVar()
item2dropdown.set("")
itemdrop = readFile("sizes.txt", 'r')#imports the sizes from the text file and sets the dropdown to be blank
dropdown = OptionMenu(app, item2dropdown, *itemdrop)#creates and places the dropdown
dropdown.pack()
dropdown.place(relx = 0.5625, rely = 0.4625)

#item 2 price/quantity

cocobun = Label(app, text = "Coconut Bun: packs of 3", font = 30)
cocobun.pack()
cocobun.place(relx = 0.4, rely = 0.4)

#item 2 entry box for quantity

cocobunquantitytitle = Label(app, text = "Quantity: ", font = 20)
cocobunquantitytitle.pack()
cocobunquantitytitle.place(relx = 0.4375, rely = 0.45)

cocobunquantity = Entry(app)
cocobunquantity.insert(0, "1")
cocobunquantity.pack()
cocobunquantity.place(relx = 0.4, rely = 0.475)

#sets the base price for the price of the item

cocobunpricetitle = Label(app, text = "Price: ", font = 20)
cocobunpricetitle.pack()
cocobunpricetitle.place(relx = 0.4375, rely = 0.5)

cocobunprice = Label(app, text = "$1.70", font = 20)
cocobunprice.pack()
cocobunprice.place(relx = 0.4375, rely = 0.525)

#makes an add to cart button that calls the addtocart function to write into the listbox the item, quantity and size of the item

cocobuntocart = Button(app, text = "Add to cart", command = lambda:addtocart(cocobunquantity.get() + " x " + item2dropdown.get() + " coconut bun"))
cocobuntocart.pack()
cocobuntocart.place(relx = 0.4375, rely = 0.55)

#item 3 image

photo = PhotoImage(file = r"C:\Users\CREEP\Downloads\python\novelRip\anotherTkinterExample\hottodoggu.png")
item1 = Label(app, image = photo, bd = 3, relief = "solid")
item1.photo = photo
item1.pack(padx = 10, pady = 18)
item1.place(relx = 0.6875, rely = 0.125)

#item 3 dropdown
item3dropdown = StringVar()
item3dropdown.set("")
itemdrop = readFile("sizes.txt", 'r')#imports the sizes from the text file and sets the dropdown to be blank
dropdown = OptionMenu(app, item3dropdown, *itemdrop)#creates and places the dropdown
dropdown.pack()
dropdown.place(relx = 0.9, rely = 0.4625) 

#item 3 price/quantity
hotdog = Label(app, text = "Hot dog bun: packs of 3", font = 30)
hotdog.pack()
hotdog.place(relx = 0.7375, rely = 0.4)

#item 3 entry box for quantity

hotdogquantitytitle = Label(app, text = "Quantity: ", font = 20)
hotdogquantitytitle.pack()
hotdogquantitytitle.place(relx = 0.775, rely = 0.45)

hotdogquantity = Entry(app)
hotdogquantity.insert(0, "1")
hotdogquantity.pack()
hotdogquantity.place(relx = 0.7375, rely = 0.475)

#item 3 price label

hotdogpricetitle = Label(app, text = "Price: ", font = 20)
hotdogpricetitle.pack()
hotdogpricetitle.place(relx = 0.775, rely = 0.5)

hotdogpricetag = Label(app, text = "$3.00", font = 20)
hotdogpricetag.pack()
hotdogpricetag.place(relx = 0.775, rely = 0.525)

#makes an add to cart button that calls the addtocart function to write into the listbox the item, quantity and size of the item

hdbtocart = Button(app, text = "Add to cart", command = lambda:addtocart(hotdogquantity.get() + " x " + item3dropdown.get() + " hot dog bun"))
hdbtocart.pack()
hdbtocart.place(relx = 0.775, rely = 0.55)

#shipping info

shipping = Label(app, text = "Shipping Info", font = 30)
shipping.pack()
shipping.place(relx = 0.475, rely = 0.6)

#makes an address entry box

addressTitle = Label(app, text = "Address:", font = 15)
addressTitle.pack()
addressTitle.place(relx = 0.375, rely = 0.75)

address = Entry(app)
address.pack()
address.place(relx = 0.375, rely = 0.8)

#name entry box

nameTitle = Label(app, text = "Full name: ", font = 15)
nameTitle.pack()
nameTitle.place(relx = 0.375, rely = 0.65)

name = Entry(app)
name.pack()
name.place(relx = 0.375, rely = 0.7)

#province drop down menu

provinceTitle = Label(app, text = "Province: ", font = 15)
provinceTitle.pack()
provinceTitle.place(relx = 0.775, rely = 0.75)

provincetitle = StringVar()
provincetitle.set("")
provincedrop = readFile("provinces.txt", 'r')
#imports provinces from the provinces text file
province = OptionMenu(app, provincetitle, *provincedrop) #creates the dropdown and places it
province.pack()
province.place(relx = 0.775, rely = 0.8)

#makes a city entry box

cityTitle = Label(app, text = "City: ", font = 15)
cityTitle.pack()
cityTitle.place(relx = 0.575, rely = 0.75)

city = Entry(app)
city.pack()
city.place(relx = 0.575, rely = 0.8)

#makes an email entry box

emailTitle = Label(app, text = "Email: ", font = 15)
emailTitle.pack()
emailTitle.place(relx = 0.575, rely = 0.65)

email = Entry(app)
email.pack()
email.place(relx = 0.575, rely = 0.7)

#makes a postal code entry box

postCodeTitle = Label(app, text = "Postal Code: ", font = 15)
postCodeTitle.pack()
postCodeTitle.place(relx = 0.475,rely = 0.8375)

postCode = Entry(app)
postCode.pack()
postCode.place(relx = 0.475, rely = 0.8875)

#calls the save_data function to save all the entries, and to check if any of the shipping info is blank
saveOrder = Button(app, text = "Save", command = save_data) #also clears all the entries and resets the item settings to their original setting
saveOrder.pack()
saveOrder.place(relx = 0.775, rely = 0.8875)

app.mainloop() #loops the program
