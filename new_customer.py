from tkinter import *
from tkinter import messagebox
import pymysql as pymysql


def confirm():
    email = email_entry.get()
    name = name_entry.get()
    phone_no = phne_entry.get()

    if email == "" or name == "" or phone_no == "":
        messagebox.showerror('Error','All fields are required!!')

    else:
        con=pymysql.connect(host='localhost',user='root',password='SAMSEVEN',database='billing_user')
        cur=con.cursor()
        cur.execute('select * from customer where phone_no=%s',phone_no)
        row=cur.fetchone()
        if row!=None:
            messagebox.showerror('Error','Customer with given phone number already exists')
        else:
            cur.execute('insert into customer(email,name,phone_no) values(%s,%s,%s)',(email,name,phone_no))
            con.commit()
            con.close()
            messagebox.showinfo('Confirm','Customer has been added successfully!')


def home():
    root.destroy()
    import home


def reset():
    phne_entry.delete(0,"end")
    name_entry.delete(0,"end")
    email_entry.delete(0,"end")

root = Tk()

root.title("Billing Software")
root.geometry("1100x700")
root.resizable(0, 0)
root.config(bg='#002f42')

photo = PhotoImage(file="images/home0.png")
label = Button(root, image=photo, bg='#002f42', command=home).place(x=40, y=30)

lbmain = Label(root, text='Supermarket Billing System', font='arial 35 bold',bg='#002f42', fg='white', pady=20).place(x=270, y=20)
lbsub = Label(root, text='New Customer', font='arial 25 bold', bg='#002f42', fg='#54bec7').place(x=450, y=150)

canvas=Canvas(root, width=900, height=1)
canvas.place(x=150,y=110)

name = Label(root, text='Customer Name:', fg='white', bg='#002f42', font='arial 18 bold').place(x=250, y=280)
name_entry = Entry(root, width=30, font='arial 16')
name_entry.place(x=460, y=285)
phne = Label(root, text='Phone Number:', fg='white', bg='#002f42', font='arial 18 bold').place(x=260, y=340)
phne_entry = Entry(root, width=30, font='arial 16')
phne_entry.place(x=460, y=345)
email = Label(root, text='Email ID:', fg='white', bg='#002f42', font='arial 18 bold').place(x=335, y=400)
email_entry = Entry(root, width=30, font='arial 16')
email_entry.place(x=460, y=400)

confirm = Button(root, text='Confirm Details', command=confirm, bg='#54bec7', font='arial 20', width=15).place(x=250, y=530)
reset = Button(root, text='Reset', command=reset, bg='#54bec7', font='arial 20', width=15).place(x=650, y=530)

root.mainloop()