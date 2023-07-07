from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#import pymysql as pymysql
from time import strftime

def newCust():
    root.destroy()
    import new_customer

def deleteCust():
    root.destroy()
    import del_customer

def updateCust():
    root.destroy()
    import update_customer

def viewCust():
    root.destroy()
    import view_customer

def newProd():
    root.destroy()
    import new_product

def deleteProd():
    root.destroy()
    import del_product

def updateProd():
    root.destroy()
    import update_product

def viewProd():
    root.destroy()
    import view_product

def bill():
    root.destroy()
    import billing

root = Tk()

root.title("Supermarket Billing System - Billing Page")
root.geometry("1100x700+200+60")
root.resizable(0, 0)
root.config(bg='#002f42')

homephoto = PhotoImage(file="images/home3.png")
picbill = PhotoImage(file="images/bill.png")
picnewCust = PhotoImage(file="images/newCust.png")
picupdateCust = PhotoImage(file="images/updateCust.png")
picdeleteCust = PhotoImage(file="images/deleteCust.png")
picviewCust = PhotoImage(file="images/viewCust.png")
picnewProd = PhotoImage(file="images/newProd.png")
picupdateProd = PhotoImage(file="images/updateProd.png")
picdeleteProd = PhotoImage(file="images/deleteProd.png")
picviewProd = PhotoImage(file="images/viewProd.png")
piclogout = PhotoImage(file="images/logout.png")

homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42').place(x=40, y=30)

lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 35 bold',bg='#002f42', fg='white', pady=20).place(x=220, y=10)
lbhome = Label(root, text='- HOME', font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5').place(x=860, y=42)

canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
canvas.place(x=150,y=110)


cust = LabelFrame(root, text="Customer", width = 900, height = 220, borderwidth=2, font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5')
cust.place(x=100, y=130)

btnnewCust = Button(cust, image = picnewCust, width = 40, height = 40, highlightbackground='#002f42', command = newCust)
btnnewCust.place(x=60, y=25)
lbnewCust = Label(cust, text = "New Customer", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbnewCust.place(x=130, y=25)

btnupdateCust = Button(cust, image = picupdateCust, width = 40, height = 40, highlightbackground='#002f42', command = updateCust)
btnupdateCust.place(x=420, y=25)
lbupdateCust = Label(cust, text = "Update Customer Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbupdateCust.place(x=480, y=25)

btndeleteCust = Button(cust, image = picdeleteCust, width = 40, height = 40, highlightbackground='#002f42', command = deleteCust)
btndeleteCust.place(x=60, y=110)
lbdeleteCust = Label(cust, text = "Delete Customer", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbdeleteCust.place(x=130, y=110)

btnviewCust = Button(cust, image = picviewCust, width = 40, height = 40, highlightbackground='#002f42')
btnviewCust.place(x=420, y=110)
lbviewCust = Label(cust, text = "View Customer Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbviewCust.place(x=480, y=110)


prod = LabelFrame(root, text="Product", width = 900, height = 220, borderwidth=2, font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5')
prod.place(x=100, y=350)

btnnewProd = Button(prod, image = picnewProd, width = 40, height = 40, highlightbackground='#002f42' ,command=newProd)
btnnewProd.place(x=60, y=25)
lbnewProd = Label(prod, text = "New Product", bg='#002f42', font='Montserrat 25 bold', fg = 'white' )
lbnewProd.place(x=130, y=25)

btnupdateProd = Button(prod, image = picupdateProd, width = 40, height = 40, highlightbackground='#002f42' ,command=updateProd)
btnupdateProd.place(x=420, y=25)
lbupdateProd = Label(prod, text = "Update Product Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbupdateProd.place(x=480, y=25)

btndeleteProd = Button(prod, image = picdeleteProd, width = 40, height = 40, highlightbackground='#002f42' ,command=deleteProd)
btndeleteProd.place(x=60, y=110)
lbdeleteProd = Label(prod, text = "Delete Product", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbdeleteProd.place(x=130, y=110)

btnviewProd = Button(prod, image = picviewProd, width = 40, height = 40, highlightbackground='#002f42' ,command=viewProd)
btnviewProd.place(x=420, y=110)
lbviewProd = Label(prod, text = "View Product Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbviewProd.place(x=480, y=110)


billing = Button(root, text=' Billing Page', image=picbill, compound= LEFT, fg='#002f42', highlightbackground='#70d0e5', borderwidth=2, font='Montserrat 20 bold', width=280, command = bill).place(x=375, y=600)

logout = Button(root, image=piclogout, highlightbackground='#002f42', width=230, height=40, command = bill).place(x=800, y=620)
lblogout = Label(root, text = 'Logout', font='Montserrat 25 bold', fg = 'white', bg = '#54bec7').place(x=890,y=620)

root.mainloop()