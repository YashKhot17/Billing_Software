from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql as mysql
from time import strftime
from fpdf import FPDF

cost=0
total=0

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size = 15)

def home():
    root.destroy()
    import home

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
            cursor.execute(f"select name,email from customer where phone_no='{cust_phone}'")
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
            con = mysql.connect(host="localhost", user="root", password="12345678", database="billing_user")
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
            con = mysql.connect(host="localhost", user="root", password="12345678", database="billing_user")
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


root = Tk()

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
