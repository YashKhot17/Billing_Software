from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mysql
from time import strftime
from fpdf import FPDF
from datetime import date
count=0
cost=0
total=0

def newCust():
    def home():
        root.destroy()

    def confirm():
        cust_name = name_entry.get()
        cust_phone = phne_entry.get()
        cust_email = email_entry.get()
        if cust_name=="" or cust_phone=="" or cust_email=="":
            messagebox.showinfo(title="Error", message="Enter All Details")
        elif len(cust_phone)!=10:
            messagebox.showinfo(title="Error", message="Enter 10-digit Number")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute("insert into customer(name,phoneno,email) values(%s,%s,%s)", (cust_name, cust_phone, cust_email))
                messagebox.showinfo(title='Status', message='Customer added successfully!')
                con.commit()
                con.close()
                name_entry.delete(0, END)
                phne_entry.delete(0, END)
                email_entry.delete(0, END)
            except IndexError:
                messagebox.showinfo(title="Error", message="Data Already Exists")
            except Exception as e:
                messagebox.showinfo(title="Error", message=e)

    def reset():
        name_entry.delete(0, END)
        phne_entry.delete(0, END)
        email_entry.delete(0, END)

    root = Toplevel()

    root.title("Supermarket Billing System - New Customer")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home)
    homeButton.place(x=40, y=30)
    picConfirm = PhotoImage(file="images/13.png")
    picReset = PhotoImage(file="images/14.png")

    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold',bg='#002f42', fg='white', pady=20)
    lbmain.place(x=220, y=15)
    lbsub = Label(root, text='New Customer', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7')
    lbsub.place(x=420, y=165)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    name = Label(root, text='Customer Name :', fg='white', bg='#002f42', font='Montserrat 20 bold').place(x=250, y=265)
    name_entry = Entry(root, width=27, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    name_entry.place(x=500, y=265)
    phne = Label(root, text='Phone Number :', fg='white', bg='#002f42', font='Montserrat 20 bold').place(x=262, y=340)
    phne_entry = Entry(root, width=27, font='Montserrat 20 bold', bg='white', highlightthickness=0)
    phne_entry.place(x=500, y=345)
    email = Label(root, text='Email ID :', fg='white', bg='#002f42', font='Montserrat 20 bold').place(x=340, y=420)
    email_entry = Entry(root, width=27, font='Montserrat 20 bold', bg='white', highlightthickness=0)
    email_entry.place(x=500, y=420)

    confirm = Button(root, text='Confirm', image=picConfirm, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground = '#5ce1e6', font='arial 25', width=250, command=confirm)
    confirm.place(x=250, y=530)
    reset = Button(root, text='Reset', image=picReset, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 25', width=250, command = reset)
    reset.place(x=620, y=530)

    root.mainloop()

def deleteCust():
    def home():
        root.destroy()

    def search():
        cust_phone = txtPhoneNo.get()
        try:
            con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
            cursor = con.cursor()
            cursor.execute(f"select name,email from customer where phoneno='{cust_phone}'")
            data = cursor.fetchall()
            txtname['text']=data[0][0]
            txtemail['text']=data[0][1]
            txtname['bg']='white'
            txtemail['bg']='white'
            txtPhoneNo.config(state=DISABLED)
            con.commit()
            con.close()
        except IndexError:
            messagebox.showinfo(title="Error", message="Data not found!")

    def delete():
        cust_phone = txtPhoneNo.get()
        if cust_phone=="":
            messagebox.showinfo(title='Error', message='Enter Customer Phone Number')
        elif txtname.cget('text')=="":
            messagebox.showinfo(title='Error', message='Search Customer Details first')
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute(f"delete from customer where phoneno='{cust_phone}'")
                messagebox.showinfo(title='Status', message='Customer deleted successfully!')
                txtPhoneNo.config(state=NORMAL)
                txtPhoneNo.delete(0, END)
                txtname['text']=""
                txtemail['text']=""
                txtname['bg']='#95a2aa'
                txtemail['bg']='#95a2aa'
                con.commit()
                con.close()
            except IndexError:
                messagebox.showinfo(title="Error", message="Data not found!")

    def reset():
        txtPhoneNo.config(state=NORMAL)
        txtPhoneNo.delete(0, END)
        txtname['text']=""
        txtemail['text']=""
        txtname['bg']='#95a2aa'
        txtemail['bg']='#95a2aa'

    root = Toplevel()

    root.title("Supermarket Billing System - Delete Customer")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    picSearch = PhotoImage(file="images/search1.png")
    picDelete = PhotoImage(file="images/15.png")
    picReset = PhotoImage(file="images/16.png")

    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)
    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold', bg='#002f42', fg='white',pady=20).place(x=220, y=15)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    lbsub = Label(root, text='Delete Customer', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7').place(x=420, y=165)

    lbPhoneNo = Label(root, text='Phone Number :', fg='white', bg='#002f42', font='Montserrat 20 bold').place(x=248, y=265)
    txtPhoneNo = Entry(root, width=27, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    txtPhoneNo.place(x=480, y=265)

    btnsearch = Button(root, image=picSearch, width=30, height=30, highlightbackground='#002f42', command=search)
    btnsearch.place(x=900, y=265)

    canvas2=Canvas(root, width=700, highlightthickness=0, height=3, bg='#54bec7').place(x=220, y=320)

    lbname = Label(root, text='Customer Name :', fg='white', bg='#002f42', font='Montserrat 20 bold').place(x=235, y=340)
    txtname = Label(root, width=25, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtname.place(x=480, y=340)
    lbemail = Label(root, text='Email ID :', fg='white', bg='#002f42', font='Montserrat 20 bold').place(x=332, y=420)
    txtemail = Label(root, width=25, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtemail.place(x=480, y=420)

    confirm = Button(root, text='Delete', image=picDelete, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground = '#5ce1e6', font='arial 25', width=250, command=delete)
    confirm.place(x=250, y=530)
    reset = Button(root, text='Reset', image=picReset, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 25', width=250, command = reset)
    reset.place(x=650, y=530)

    root.mainloop()

def updateCust():
    def home():
        root.destroy()

    def search():
        cust_phone = txtPhoneNo.get()
        txtPhoneNo.config(state=DISABLED)
        txtname['bg']='white'
        txtemail['bg']='white'
        try:
            con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
            cursor = con.cursor()
            cursor.execute(f"select name,email from customer where phoneno='{cust_phone}'")
            data = cursor.fetchall()
            txtname.delete(0, END)
            txtname.insert(0, data[0][0])
            txtemail.delete(0, END)
            txtemail.insert(0, data[0][1])
            con.commit()
            con.close()
        except IndexError:
            messagebox.showinfo(title="Error", message="Data not found!")

    def update():
        cust_name = txtname.get()
        cust_phone = txtPhoneNo.get()
        cust_email = txtemail.get()
        if cust_phone=="":
            messagebox.showinfo(title='Status', message='Enter Customer Phone Number')
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute(f"update customer set name='{cust_name}', email='{cust_email}' where phoneno='{cust_phone}'")
                messagebox.showinfo(title='Status', message='Customer details updated successfully!')
                txtPhoneNo.config(state=NORMAL)
                txtname.delete(0, END)
                txtPhoneNo.delete(0, END)
                txtemail.delete(0, END)
                txtname['bg']='#95a2aa'
                txtemail['bg']='#95a2aa'
                con.commit()
                con.close()
            except IndexError:
                messagebox.showinfo(title="Error", message="Data not found!")

    def reset():
        txtPhoneNo.config(state='normal')
        txtname.delete(0, END)
        txtPhoneNo.delete(0, END)
        txtemail.delete(0, END)
        txtname['bg']='#95a2aa'
        txtemail['bg']='#95a2aa'

    root = Toplevel()

    root.title("Supermarket Billing System - Update Customer")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    picSearch = PhotoImage(file="images/search1.png")
    picUpdate = PhotoImage(file="images/17.png")
    picReset = PhotoImage(file="images/14.png")

    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)
    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold', bg='#002f42', fg='white',pady=20).place(x=220, y=15)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    lbsub = Label(root, text='Update Customer', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7').place(x=420, y=165)

    lbPhoneNo = Label(root, text='Phone Number :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=210, y=260)
    txtPhoneNo = Entry(root, width=30, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    txtPhoneNo.place(x=480, y=265)

    btnsearch = Button(root, image=picSearch, width=30, height=30, highlightbackground='#002f42', command=search)
    btnsearch.place(x=950, y=265)

    canvas2=Canvas(root, width=700, highlightthickness=0, height=3, bg='#54bec7').place(x=220, y=320)

    lbname = Label(root, text='Customer Name :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=190, y=340)
    txtname = Entry(root, width=30, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtname.place(x=480, y=345)
    lbemail = Label(root, text='Email ID :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=310, y=420)
    txtemail = Entry(root, width=30, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtemail.place(x=480, y=420)

    update = Button(root, text='Update', image=picUpdate, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground = '#5ce1e6', font='arial 25', width=250, command=update)
    update.place(x=250, y=530)
    reset = Button(root, text='Reset', image=picReset, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 25', width=250, command = reset)
    reset.place(x=650, y=530)

    root.mainloop()

def viewCust():
    def home():
        root.destroy()

    def search():
        cust_phone = txtphone.get()
        try:
            con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
            cursor = con.cursor()
            cursor.execute(f"select name,email from customer where phoneno='{cust_phone}'")
            data1 = cursor.fetchall()
            txtname['text']=""
            txtname['text'] = data1[0][0]
            txtname['bg']='white'
            txtemail['text']=""
            txtemail['text'] = data1[0][1]
            txtemail['bg']='white'
            txtphone.config(state=DISABLED)

            cursor.execute(f"select date,billno,totalbill from billing where cust_phno='{cust_phone}'")
            data2 = cursor.fetchall()
            for i in data2:
                billsTV.insert(parent='', index=END, values=(i[0], i[1], f"Rs. {i[2]}"))
            con.commit()
            con.close()
        except IndexError:
            messagebox.showinfo(title="Error", message="Data not found!")

    def reset():
        txtphone.config(state='normal')
        txtphone.delete(0, END)
        txtname['text']=""
        txtemail['text']=""
        txtname['bg']='#95a2aa'
        txtemail['bg']='#95a2aa'
        for item in billsTV.get_children():
            billsTV.delete(item)

    root = Toplevel()

    root.title("Supermarket Billing System - View Customer Details")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    picviewProd = PhotoImage(file="images/viewProd.png")
    picsearch = PhotoImage(file="images/search1.png")
    picReset = PhotoImage(file="images/14.png")

    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)

    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold', bg='#002f42', fg='white',pady=20).place(x=220, y=15)
    lbsub = Label(root, text='Customer Details', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7').place(x=400, y=125)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    lbphone = Label(root, text='Phone Number :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=100, y=185)
    txtphone = Entry(root, width=35, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    txtphone.place(x=365, y=190)

    btn_customer_Search = Button(root, image=picsearch, width=30,height=30, highlightthickness=0, highlightbackground='#002f42', command = search)
    btn_customer_Search.place(x=910, y=190)

    canvas1=Canvas(root, width=980, highlightthickness=0, height=3, bg='#70d0e5')
    canvas1.place(x=60,y=240)

    lbname = Label(root, text='Customer Name :', font='Montserrat 20 bold',bg='#002f42', fg='white').place(x=50, y=260)
    lbemail = Label(root, text='Email ID :', font='Montserrat 20 bold',bg='#002f42', fg='white').place(x=580, y=260)

    txtname = Label(root, width=16, font='Montserrat 20 bold', bg='#95a2aa', fg='black')
    txtname.place(x=292, y=260)
    txtemail = Label(root, width=20, font='Montserrat 20 bold', bg='#95a2aa', fg='black')
    txtemail.place(x=720, y=260)

    TableFrame = Frame(root,bg="#002f42",width=800,height=350)
    TableFrame.place(x=260,y=320)

    billsTV = ttk.Treeview(TableFrame,height=12, columns=('Date','Bill No','Total Bill'))
    billsTV.grid(row=5, column=0, columnspan=5)

    billLabel=Label(TableFrame, text="Customer History", font="Arial 20", fg='white',bg='#002f42')
    billLabel.grid(row=4, column=2)

    scrollBar = Scrollbar(TableFrame, orient="vertical",command=billsTV.yview)
    scrollBar.grid(row=5, column=4, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.column('#0', width=0, stretch=NO)
    billsTV.column('#1', anchor=CENTER)
    billsTV.column('#2', anchor=CENTER)
    billsTV.column('#3', anchor=CENTER)

    billsTV.heading('#0',text="")
    billsTV.heading('#1',text="Date")
    billsTV.heading('#2',text="Bill ID")
    billsTV.heading('#3',text="Total Bill")

    reset = Button(root, text='Reset', image=picReset, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 20', width=200, command = reset)
    reset.place(x=440, y=640)

    root.mainloop()

def newProd():
    def home():
        root.destroy()

    def confirm():
        prod_name = name_entry.get()
        prod_price = price_entry.get()
        prod_id = id_entry['text']
        if prod_name=="" or prod_price=="":
            messagebox.showinfo(title='Error', message='Enter all Product Details')
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute("insert into product(id,name,price) values(%s,%s,%s)", (prod_id,prod_name, prod_price))
                messagebox.showinfo(title='Status', message='Product added successfully!')
                global count
                count = count+1
                id_entry['text']=count
                name_entry.delete(0, END)
                price_entry.delete(0, END)
                con.commit()
                con.close()
            except IndexError:
                messagebox.showinfo(title="Error", message="Data Already Exists")
            except Exception as es:
                messagebox.showinfo(title='Error', message=es)

    def reset():
        price_entry.delete(0, END)
        name_entry.delete(0, END)


    root = Toplevel()

    root.title("Supermarket Billing System - New Product")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')


    homephoto = PhotoImage(file="images/home3.png")
    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)
    picConfirm = PhotoImage(file="images/13.png")
    picReset = PhotoImage(file="images/14.png")

    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold', bg='#002f42', fg='white',pady=20)
    lbmain.place(x=220, y=15)
    lbsub = Label(root, text='New Product', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7')
    lbsub.place(x=420, y=165)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    id = Label(root, text='Product ID :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=280, y=260)
    id_entry = Label(root, width=25, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    id_entry.place(x=480, y=265)
    name = Label(root, text='Product Name :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=220, y=340)
    name_entry = Entry(root, width=30, font='Montserrat 20 bold', bg='white', highlightthickness=0)
    name_entry.place(x=480, y=345)
    price = Label(root, text='Price :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=360, y=415)
    price_entry = Entry(root, width=30, font='Montserrat 20 bold', bg='white', highlightthickness=0)
    price_entry.place(x=480, y=420)

    confirm = Button(root, text='Confirm', image=picConfirm, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground = '#5ce1e6', font='arial 25', width=250, command=confirm)
    confirm.place(x=250, y=530)
    reset = Button(root, text='Reset', image=picReset, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 25', width=250, command=reset)
    reset.place(x=650, y=530)


    try:
        con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
        cursor = con.cursor()
        cursor.execute("SELECT id FROM product WHERE id=(SELECT max(id) FROM product)")
        data = cursor.fetchall()
        global count
        count = int(data[0][0]) + 1
        id_entry['text']=count
        con.commit()
        con.close()
    except IndexError:
        messagebox.showinfo(title="Error", message="Data not found!")

    root.mainloop()

def deleteProd():
    def home():
        root.destroy()

    def search():
        product_id = txtProductID.get()
        txtProductID.config(state=DISABLED)
        try:
            con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
            cursor = con.cursor()
            cursor.execute(f"select name,price from product where id='{product_id}'")
            data = cursor.fetchall()
            txtProductName['text']=data[0][0]
            txtPrice['text']=data[0][1]
            txtProductName['bg']="white"
            txtPrice['bg']="white"
            con.commit()
            con.close()
        except IndexError:
            messagebox.showinfo(title="Error", message="Data not found!")

    def delete():
        product_id = txtProductID.get() 
        if product_id=="":
            messagebox.showinfo(title='Error', message='Enter Product ID')
        elif txtProductName.cget('text')=="":
            messagebox.showinfo(title='Enter', message='Search Product Details first') 
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute(f"delete from product where id='{product_id}'")
                messagebox.showinfo(title='Status', message='Product deleted successfully!')
                txtProductID.config(state=NORMAL)
                txtProductID.delete(0, END)
                txtProductName['text']=""
                txtPrice['text']=""
                txtProductName['bg']="#95a2aa"
                txtPrice['bg']="#95a2aa"
                con.commit()
                con.close()
            except IndexError:
                messagebox.showinfo(title="Error", message="Data not found!")
            except Exception as es:
                messagebox.showinfo(title='Error', message=es)

    def reset():
        txtProductID.config(state=NORMAL)
        txtProductID.delete(0, END)
        txtProductName['text']=""
        txtPrice['text']=""
        txtProductName['bg']="#95a2aa"
        txtPrice['bg']="#95a2aa"

    root = Toplevel()

    root.title("Supermarket Billing System - Delete Product")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    picSearch = PhotoImage(file="images/search1.png")
    picDelete = PhotoImage(file="images/15.png")
    picReset = PhotoImage(file="images/16.png")

    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)
    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold', bg='#002f42', fg='white',pady=20)
    lbmain.place(x=220, y=15)
    lbsub = Label(root, text='Delete Product', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7')
    lbsub.place(x=420, y=165)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    lbProductID = Label(root, text='Product ID :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=280, y=260)
    txtProductID = Entry(root, width=30, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    txtProductID.place(x=480, y=265)

    btnsearch = Button(root, image=picSearch, width=30, height=30, highlightbackground='#002f42', command=search)
    btnsearch.place(x=950, y=265)

    canvas2=Canvas(root, width=700, highlightthickness=0, height=3, bg='#54bec7').place(x=220, y=320)

    lbProductName = Label(root, text='Product Name :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=220, y=340)
    txtProductName = Label(root, width=30, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtProductName.place(x=480, y=345)
    lbePrice = Label(root, text='Price :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=360, y=420)
    txtPrice = Label(root, width=30, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtPrice.place(x=480, y=425)

    btndelete = Button(root, text='Delete', image=picDelete, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground = '#5ce1e6', font='arial 25', width=250, command=delete)
    btndelete.place(x=250, y=530)
    reset = Button(root, text='Reset', image=picReset, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 25', width=250, command = reset)
    reset.place(x=650, y=530)

    root.mainloop()

def updateProd():
    def home():
        root.destroy()

    def search():
        prod_ID = txtProductID.get()
        txtProductID.config(state=DISABLED)
        txtName['bg']='white'
        txtPrice['bg']='white'
        try:
            con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
            cursor = con.cursor()
            cursor.execute(f"select name,price from product where id='{prod_ID}'")
            data = cursor.fetchall()
            txtName.delete(0, END)
            txtName.insert(0, data[0][0])
            txtPrice.delete(0, END)
            txtPrice.insert(0, data[0][1])
            con.commit()
            con.close()
        except IndexError:
            messagebox.showinfo(title="Error", message="Data not found!")

    def update():
        prod_name = txtName.get()
        prod_id = txtProductID.get()
        prod_price = txtPrice.get()
        if prod_id=="":
            messagebox.showinfo(title="Error", message="Enter Product ID")
        elif prod_name=="":
            messagebox.showinfo(title="Error", message="Enter Product Name")
        elif prod_price=="":
            messagebox.showinfo(title="Error", message="Enter Product Price")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute(f"update product set name='{prod_name}', price='{prod_price}' where id='{prod_id}'")
                messagebox.showinfo(title='Status', message='Product details updated successfully!')
                txtProductID.config(state=NORMAL)
                txtName.delete(0, END)
                txtProductID.delete(0, END)
                txtPrice.delete(0, END)
                txtName['bg']='#95a2aa'
                txtPrice['bg']='#95a2aa'
                con.commit()
                con.close()
            except IndexError:
                messagebox.showinfo(title="Error", message="Data not found!")

    def reset():
        txtProductID.config(state='normal')
        txtName.delete(0, END)
        txtProductID.delete(0, END)
        txtPrice.delete(0, END)
        txtName['bg']='#95a2aa'
        txtPrice['bg']='#95a2aa'

    root = Toplevel()

    root.title("Supermarket Billing System - Update Product")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    picSearch = PhotoImage(file="images/search1.png")
    picUpdate = PhotoImage(file="images/17.png")
    picReset = PhotoImage(file="images/14.png")

    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)
    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold', bg='#002f42', fg='white',pady=20)
    lbmain.place(x=220, y=15)
    lbsub = Label(root, text='Update Product', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7')
    lbsub.place(x=420, y=165)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    lbProductID = Label(root, text='Product ID :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=275, y=260)
    txtProductID = Entry(root, width=30, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    txtProductID.place(x=480, y=265)

    btnsearch = Button(root, image=picSearch, width=30, height=30, highlightbackground='#002f42', command=search)
    btnsearch.place(x=950, y=265)

    canvas2=Canvas(root, width=700, highlightthickness=0, height=3, bg='#54bec7').place(x=220, y=320)

    lbName = Label(root, text='Product Name :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=220, y=340)
    txtName = Entry(root, width=30, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtName.place(x=480, y=345)
    lbPrice = Label(root, text='Price ID :', fg='white', bg='#002f42', font='Montserrat 25 bold').place(x=320, y=420)
    txtPrice = Entry(root, width=30, font='Montserrat 20 bold', bg='#95a2aa', highlightthickness=0, fg='black')
    txtPrice.place(x=480, y=425)

    update = Button(root, text='Update', image=picUpdate, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground = '#5ce1e6', font='arial 25', width=250, command=update)
    update.place(x=250, y=530)
    reset = Button(root, text='Reset', image=picReset, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 25', width=250, command = reset)
    reset.place(x=650, y=530)

    root.mainloop()

def viewProd():
    def home():
        root.destroy()

    def view():
        try:
            con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
            cursor = con.cursor()
            cursor.execute("select * from product")
            records = cursor.fetchall()
            for record in records:
                productsTV.insert(parent='', index=END, values=(record[0],record[1],record[2]))
            con.commit()
            con.close()
        except IndexError:
            messagebox.showinfo(title="Error", message="Data Already Exists")

    def refresh():
        for item in productsTV.get_children():
            productsTV.delete(item)
        view()

    root = Toplevel()

    root.title("Supermarket Billing System - View Product Details")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    picviewProd = PhotoImage(file="images/viewProd.png")
    picRefresh = PhotoImage(file="images/17.png")

    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)

    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 40 bold', bg='#002f42', fg='white', pady=20)
    lbmain.place(x=220, y=15)
    lbsub = Label(root, text='View Product Details', font='Montserrat 30 bold', bg='#002f42', fg='#54bec7')
    lbsub.place(x=380, y=150)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    TableFrame = Frame(root,bg="white",width=800,height=450)
    #TableFrame = Frame(root,bg="#002f42",width=800,height=450)
    TableFrame.place(x=250,y=210)

    productsTV = ttk.Treeview(TableFrame,height=20, columns=('Product ID','Product Name','Price'))
    productsTV.grid(row=5, column=0, columnspan=4)

    scrollBar = Scrollbar(TableFrame, orient="vertical",command=productsTV.yview)
    scrollBar.grid(row=5, column=4, sticky="NSE")

    productsTV.configure(yscrollcommand=scrollBar.set)

    productsTV.column('#0', width=0, stretch=NO)
    productsTV.column('#1', anchor=CENTER)
    productsTV.column('#2', anchor=CENTER)
    productsTV.column('#3', anchor=CENTER)

    productsTV.heading('#0',text="")
    productsTV.heading('#1',text="Product ID")
    productsTV.heading('#2',text="Product Name")
    productsTV.heading('#3',text="Price")

    view()

    refresh = Button(root, text='Refresh', image=picRefresh, compound= LEFT, fg='#002f42', borderwidth=0, highlightbackground='#5ce1e6', font='arial 20', width=220, command=refresh)
    refresh.place(x=440, y=640)

    """billing = Button(root, text='View Products', image=picviewProd, compound= LEFT, fg='#002f42', highlightbackground='#70d0e5', borderwidth=2, font='Montserrat 30 bold', command=view, width=300)
    billing.place(x=375, y=600)
    """
    root.mainloop()

def bill():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size = 15)

    def home():
        root.destroy()

    def time():
        hr = strftime("%I")
        min = strftime("%M")
        sec = strftime("%S")
        mer = strftime("%p")

        lbTime1.config(text=hr+":"+min+":"+sec+" "+mer)
        lbTime1.after(1000, time)

    def customer_search():
        cust_phone = txtphone.get()
        if cust_phone=="":
            messagebox.showinfo(title="Error", message="Enter Customer Phone Number")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute(f"select name,email from customer where phoneno='{cust_phone}'")
                data = cursor.fetchall()
                txtname['text']=""
                txtname['text'] = data[0][0]
                txtname['bg']='white'
                txtemail['text']=""
                txtemail['text'] = data[0][1]
                txtemail['bg']='white'
                txtphone.config(state=DISABLED)
                con.commit()
                con.close()
            except IndexError:
                messagebox.showinfo(title="Error", message="Data not found!")

    def product_search():
        prod_id = txtProductID.get()
        if prod_id=="":
            messagebox.showinfo(title="Error", message="Enter Product ID")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute(f"select name,price from product where id='{prod_id}'")
                data = cursor.fetchall()
                txtProductName['text'] = data[0][0]
                txtProductName['bg']='white'
                txtrate['text'] = data[0][1]
                txtrate['bg']='white'
                txtquant.config(state=NORMAL)
                con.commit()
                con.close()
            except IndexError:
                messagebox.showinfo(title="Error", message="Data not found!")

    def add():
        item = txtProductName.cget('text')
        rate = txtrate.cget('text')
        quantity = txtquant.get()
        if txtProductID.get()=="" or item=="" or rate=="":
            messagebox.showinfo(title="Error", message="Enter Product ID")
        else:
            cost = int(rate)*int(quantity)
            billsTV.insert(parent='', index=END, values=(item, rate, quantity, cost))
            txtProductID.delete(0, END)
            txtProductName['text'] = ""
            txtrate['text'] = ""
            txtquant.delete(0,END)
            txtquant.insert(0, "1")
            txtProductName['bg']='#95a2aa'
            txtrate['bg']='#95a2aa'
            global total 
            total = total+cost
            lbTotal['text']=total
            txtquant.config(state=DISABLED)

    def delete():
        try:
            selected = billsTV.focus()
            values = billsTV.item(selected, 'values')
            cost = int(values[3])
            global total 
            total = total-cost
            lbTotal['text']=total
            selected_item = billsTV.selection()[0]
            billsTV.delete(selected_item)
        except:
            messagebox.showinfo(title="Error", message="Select Item to be Deleted")

    def reset():
        txtphone.config(state=NORMAL)
        txtphone.delete(0, END)
        txtProductID.delete(0, END)
        txtname['text']=""
        txtemail['text']=""
        global total
        total = 0
        lbTotal['text']=total
        txtname['bg']='#95a2aa'
        txtemail['bg']='#95a2aa'
        txtProductID.delete(0, END)
        txtProductName['text'] = ""
        txtrate['text'] = ""
        txtquant.delete(0,END)
        txtquant.insert(0, "1")
        txtProductName['bg']='#95a2aa'
        txtrate['bg']='#95a2aa'
        txtquant.config(state=DISABLED)
        for item in billsTV.get_children():
            billsTV.delete(item)

    def resetCustomer():
        txtphone.config(state=NORMAL)
        txtphone.delete(0, END)
        txtname['text']=""
        txtemail['text']=""
        txtname['bg']='#95a2aa'
        txtemail['bg']='#95a2aa'

    def resetBill():
        global total
        total = 0
        lbTotal['text']=total
        for item in billsTV.get_children():
            billsTV.delete(item)

    def printBill():
        totalBill = lbTotal['text']
        name = txtname.cget('text')
        customerPhoneNo = txtphone.get()
        date1 = date.today()
        d1 = date1.strftime("%d/%b/%Y")
        d = date1.strftime("%d%m%y")
        t = strftime("%H%M%S")
        billid = f"{d}_{t}_{customerPhoneNo}"
        if lbTotal['text']==0:
            messagebox.showinfo(title="Error", message="Add items to Bill")
        elif customerPhoneNo=="" or name=="":
            messagebox.showinfo(title="Error", message="Enter Customer Details")
        else:
            #  PRINT PDF
            pdf.cell(w=None, h=None,txt="******************************************************************************************", ln=1)
            pdf.set_font("helvetica", size = 30, style='B')
            pdf.cell(0, 20, txt = "Supermarket Bill", align = 'C', ln=1)
            pdf.set_font("helvetica", size = 15)
            pdf.cell(w=None, h=None,txt="============================================================", ln=1)
            pdf.cell(200, 10, txt = f"Bill ID : {billid}            ", align = 'R', ln=1)

            pdf.cell(0, 10, txt=f"Customer Phone Number : {customerPhoneNo}", ln=1)
            pdf.cell(0, 10, txt=f"Customer Name : {name}",ln=1)
            pdf.ln()

            headings=('ITEM',"RATE",'QUANTITY','COST')
            count=0
            for heading in headings:
                pdf.cell(45, 10, heading, ln=0, border=1)
            pdf.ln()

            for i in billsTV.get_children():
                values = billsTV.item(i, 'values')
                for j in values:
                    pdf.cell(45, 10, j, ln=0, border=1)
                pdf.ln()

            pdf.cell(135, 10, txt="")
            pdf.cell(45, 10, txt = f"TOTAL : Rs. {totalBill}            ", align = 'L', ln=1)
            pdf.ln()
            pdf.cell(w=None, h=None,txt="============================================================", ln=1)
            pdf.set_font("helvetica", size = 15, style='B')
            pdf.cell(0,20,txt="Thanks for shopping with us today!", align='C', ln=1)
            pdf.set_font("helvetica", size = 15)
            pdf.cell(w=None, h=None,txt="******************************************************************************************", ln=1)
            pdf.output(f"Bill_{billid}.pdf") 

            try:
                con = mysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
                cursor = con.cursor()
                cursor.execute("insert into billing(billno, cust_phno,date,totalbill) values(%s,%s,%s,%s)", (billid, customerPhoneNo, d1, totalBill))
                messagebox.showinfo(title='Status', message='Bill Printed successfully!')
                reset()
                con.commit()
                con.close()
                
            except IndexError:
                messagebox.showinfo(title="Error", message="Some Error Occured")
            except Exception as e:
                messagebox.showinfo(title="Error", message=e)


    root = Toplevel()

    root.title("Supermarket Billing System - Billing Page")
    root.geometry("1100x700+200+60")
    root.resizable(0, 0)
    root.config(bg='#002f42')

    homephoto = PhotoImage(file="images/home3.png")
    picsearch = PhotoImage(file="images/search1.png")
    picAdd = PhotoImage(file="images/Add.png")
    picPrint = PhotoImage(file="images/PrintBtn.png")
    picReset = PhotoImage(file="images/Reset.png")

    homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42', command=home).place(x=40, y=30)

    lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 50 bold',bg='#002f42', fg='white', pady=20).place(x=150, y=10)

    time_string = strftime('%H:%M %p')
    date_string = strftime('%d %b %y')
    lbDate1 = Label(root, text=date_string, font='Montserrat 25 bold',bg='#002f42', fg='white')
    lbDate1.place(x=900,y=12)
    lbTime1 = Label(root, text="", font='Montserrat 25 bold',bg='#002f42', fg='white')
    lbTime1.place(x=900,y=60)
    time()

    lbdate = Label(root, text='DATE :', font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5').place(x=810, y=12)
    lbdate = Label(root, text='TIME :', font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5').place(x=815, y=60)

    canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
    canvas.place(x=150,y=110)

    lbphone = Label(root, text='Phone Number :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=85, y=130)
    lbname = Label(root, text='Customer Name :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=70, y=170)
    lbemail = Label(root, text='Email ID :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=600, y=170)

    btn_customer_Search = Button(root, image=picsearch, width=30,height=30, highlightthickness=0, highlightbackground='#002f42', command = customer_search)
    btn_customer_Search.place(x=750, y=125)

    txtphone = Entry(root, width=30, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    txtphone.place(x=290, y=130)
    txtname = Label(root, width=20, font='Montserrat 20 bold', bg='#95a2aa', fg='black')
    txtname.place(x=292, y=175)
    txtemail = Label(root, width=21, font='Montserrat 20 bold', bg='#95a2aa', fg='black')
    txtemail.place(x=720, y=175)

    btnresetCustomer = Button(root, text = "RESET Customer Details", font='Montserrat 15 bold', highlightthickness=0, highlightbackground='#54bec7', fg='#002f42', command= resetCustomer)
    btnresetCustomer.place(x=800, y=130)

    canvas1=Canvas(root, width=980, highlightthickness=0, height=3, bg='#70d0e5')
    canvas1.place(x=60,y=220)

    lbproductID = Label(root, text='Enter Product ID :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=68, y=230)
    lbprodName = Label(root, text='Product Name :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=92, y=275)
    lbRate = Label(root, text='Rate :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=640, y=230)
    lbQuantity = Label(root,text='Quantity :', font='Montserrat 25 bold',bg='#002f42', fg='white').place(x=640, y=275)

    btn_product_Search = Button(root, image=picsearch, width=30,height=30, highlightthickness=0, highlightbackground='#002f42', command=product_search).place(x=490, y=230)

    txtProductID = Entry(root, width=12, font='Montserrat 20 bold', bg='white', fg='black', highlightthickness=0)
    txtProductID.place(x=290, y=235)
    txtProductName = Label(root, width=20, font='Montserrat 20 bold', bg='#95a2aa', fg='black')
    txtProductName.place(x=290, y=280)
    txtrate = Label(root, width=21, font='Montserrat 20 bold', bg='#95a2aa', fg='black')
    txtrate.place(x=720, y=230)
    txtquant =Spinbox(root, width=2, from_ = 1, to = 10,fg='black', bg='white', font="Montserrat 25 bold", state=DISABLED)
    txtquant.place(x=770,y=270)

    btnAdd = Button(root ,text="ADD", compound= LEFT, image=picAdd, highlightthickness=1, highlightbackground='#54bec7', fg='#002f42', font='Montserrat 25 bold', width=100, command=add)
    btnAdd.place(x=918, y=270)

    canvas1=Canvas(root, width=980, highlightthickness=0, height=3, bg='#70d0e5')
    canvas1.place(x=60,y=320)

    TableFrame = Frame(root,bg="#002f42",width=800,height=350)
    TableFrame.place(x=60,y=335)

    billLabel=Label(TableFrame, text="BILL", font="Arial 20", fg='white',bg='#002f42')
    billLabel.grid(row=4, column=2)

    billsTV = ttk.Treeview(TableFrame,height=13, columns=('Item','Rate','Quantity','Cost'))
    billsTV.grid(row=5, column=0, columnspan=5)

    scrollBar = Scrollbar(TableFrame, orient="vertical",command=billsTV.yview)
    scrollBar.grid(row=5, column=4, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.column('#0', width=0, stretch=NO)
    billsTV.column('#1', anchor=CENTER, minwidth=200)
    billsTV.column('#2', anchor=CENTER, minwidth=200)
    billsTV.column('#3', anchor=CENTER, minwidth=200)
    billsTV.column('#4', anchor=CENTER, minwidth=200)

    billsTV.heading('#0',text="")
    billsTV.heading('#1',text="ITEM")
    billsTV.heading('#2',text="RATE")
    billsTV.heading('#3',text="QUANTITY")
    billsTV.heading('#4',text="COST")

    btnDelete = Button(root, text="DELETE",font='Montserrat 20 bold', highlightthickness=0, highlightbackground='#54bec7', fg='#002f42', command=delete)
    btnDelete.place(x=300,y=650)

    btnResetBill = Button(root, text="RESET BILL",font='Montserrat 20 bold', highlightthickness=0, highlightbackground='#54bec7', fg='#002f42', command=resetBill)
    btnResetBill.place(x=500,y=650)

    lbTotalBill = Label(root, text='TOTAL BILL :', font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5').place(x=880, y=355)
    lbTotal = Label(root, width=11,text = total, font='Montserrat 25 bold',bg='white', fg='#002f42')
    lbTotal.place(x=880, y=390)

    btnPrint = Button(root, image=picPrint, width=190,height=40, bg='#002f42', command=printBill)
    btnPrint.place(x=880, y=480)
    btnReset = Button(root, image=picReset, width=190,height=35, bg='#002f42', command=reset)
    btnReset.place(x=880, y=580)

    root.mainloop()

def logout():
    msg = messagebox.askquestion(title="LOGOUT",message="Do you want to LOGOUT?", icon ='question')
    if msg=="yes":
        root.destroy()
    else:
        pass


root = Tk()

root.title("Supermarket Billing System - Home Page")
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

homeButton = Button(root, image=homephoto, width=70,height=70, bg='#002f42')
homeButton.place(x=40, y=30)

lbmain = Label(root, text='Supermarket Billing System', font='Montserrat 35 bold',bg='#002f42', fg='white', pady=20)
lbmain.place(x=220, y=10)
lbhome = Label(root, text='- HOME', font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5')
lbhome.place(x=860, y=42)

canvas=Canvas(root, width=900, highlightthickness=0, height=3, bg='white')
canvas.place(x=150,y=110)


cust = LabelFrame(root, text="Customer", width = 900, height = 220, borderwidth=2, font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5')
cust.place(x=100, y=130)

btnnewCust = Button(cust, image = picnewCust, width = 40, height = 40, highlightbackground='#002f42', command = newCust)
btnnewCust.place(x=60, y=25)
lbnewCust = Label(cust, text = "New Customer", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbnewCust.place(x=120, y=25)

btnupdateCust = Button(cust, image = picupdateCust, width = 40, height = 40, highlightbackground='#002f42', command = updateCust)
btnupdateCust.place(x=400, y=25)
lbupdateCust = Label(cust, text = "Update Customer Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbupdateCust.place(x=470, y=25)

btndeleteCust = Button(cust, image = picdeleteCust, width = 40, height = 40, highlightbackground='#002f42', command = deleteCust)
btndeleteCust.place(x=60, y=110)
lbdeleteCust = Label(cust, text = "Delete Customer", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbdeleteCust.place(x=120, y=110)

btnviewCust = Button(cust, image = picviewCust, width = 40, height = 40, highlightbackground='#002f42', command=viewCust)
btnviewCust.place(x=400, y=110)
lbviewCust = Label(cust, text = "View Customer Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbviewCust.place(x=470, y=110)


prod = LabelFrame(root, text="Product", width = 900, height = 220, borderwidth=2, font='Montserrat 25 bold',bg='#002f42', fg='#70d0e5')
prod.place(x=100, y=350)

btnnewProd = Button(prod, image = picnewProd, width = 40, height = 40, highlightbackground='#002f42', command=newProd)
btnnewProd.place(x=60, y=25)
lbnewProd = Label(prod, text = "New Product", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbnewProd.place(x=120, y=25)

btnupdateProd = Button(prod, image = picupdateProd, width = 40, height = 40, highlightbackground='#002f42', command=updateProd)
btnupdateProd.place(x=400, y=25)
lbupdateProd = Label(prod, text = "Update Product Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbupdateProd.place(x=470, y=25)

btndeleteProd = Button(prod, image = picdeleteProd, width = 40, height = 40, highlightbackground='#002f42', command=deleteProd)
btndeleteProd.place(x=60, y=110)
lbdeleteProd = Label(prod, text = "Delete Product", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbdeleteProd.place(x=120, y=110)

btnviewProd = Button(prod, image = picviewProd, width = 40, height = 40, highlightbackground='#002f42', command=viewProd)
btnviewProd.place(x=400, y=110)
lbviewProd = Label(prod, text = "View Product Details", bg='#002f42', font='Montserrat 25 bold', fg = 'white')
lbviewProd.place(x=470, y=110)


billing = Button(root, text='    Billing Page', image=picbill, compound= LEFT, fg='#002f42', highlightbackground='#70d0e5', borderwidth=2, font='Montserrat 25 bold', width=300, command = bill)
billing.place(x=375, y=580)

logout = Button(root, image=piclogout, highlightbackground='#002f42', width=200, height=40, command = logout)
logout.place(x=800, y=620)
lblogout = Label(root, text = 'Logout', font='Montserrat 25 bold', fg = 'white', bg = '#54bec7')
lblogout.place(x=870,y=620)


root.mainloop()