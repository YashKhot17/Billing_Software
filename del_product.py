from tkinter import *
from tkinter import messagebox
import pymysql as pymysql

def home():
    root.destroy()
    import home

def delete():
    product_name = name_entry.get()

    con = pymysql.connect(host='localhost', user='root', password='SAMSEVEN', database='billing_user')
    cur = con.cursor()
    cur.execute('select * from product_data where product_name=%s', product_name)
    row = cur.fetchone()
    if row == None:
        messagebox.showerror('Error', 'Product does not exist')
    else:
        cur.execute('DELETE FROM product_data WHERE product_name=%s;', product_name)
        con.commit()
        con.close()
        messagebox.showinfo('Delete','Product has been deleted successfully!')


def search():
    product_name = name_entry.get()
    try:
        con = pymysql.connect(host="localhost", user="root", password="SAMSEVEN", database="billing_user")
        cursor = con.cursor()

        cursor.execute(f"Select product_id from product_data where product_name='{product_name}'")


        data = cursor.fetchall()
        product_entry = Label(root, text=f"{str(data)[2]}",  width=30, font='arial 16', bg='white')
        product_entry.place(x=460, y=345)
        cursor.execute(f"Select product_price from product_data where product_name='{product_name}'")
        prices = cursor.fetchall()
        price_entry = Label(root, text=prices[0],  width=30, font='arial 16', bg='white')
        price_entry.place(x=460, y=400)
        con.close()
    except IndexError:
        messagebox.showinfo(title="Error", message="No product found")


def confirm():
    messagebox.showinfo('Delete','Customer has been deleted successfully!')


def reset():
    name_entry.delete(0,"end")
    email_entry = Label(root, text="", width=30, font='arial 16', bg='#95A2AA')
    email_entry.place(x=460, y=400)
    phne_entry = Label(root, text="",width=30, font='arial 16', bg='#95A2AA')
    phne_entry.place(x=460, y=345)


root = Tk()

root.title("Billing Software")
root.geometry("1100x700")
root.resizable(0, 0)
root.config(bg='#002f42')

photo = PhotoImage(file="images/home0.png")
home = Button(root, image=photo, bg='#002f42', command=home).place(x=40, y=30)

lbmain = Label(root, text='Supermarket Billing System', font='arial 35 bold',bg='#002f42', fg='white', pady=20).place(x=270, y=20)
canvas=Canvas(root, width=900, height=1).place(x=150,y=110)
lbsub = Label(root, text='Delete Product', font='arial 25 bold', bg='#002f42', fg='#54bec7').place(x=450, y=150)


name = Label(root, text='Product Name:', fg='white', bg='#002f42', font='arial 18 bold').place(x=260, y=240)
name_entry = Entry(root, width=30, font='arial 16')
name_entry.place(x=460, y=245)

canvas2=Canvas(root, width=700, height=1, bg='#54bec7').place(x=220, y=290)

phne = Label(root, text='Product ID:', fg='white', bg='#002f42', font='arial 18 bold').place(x=300, y=340)
phne_entry = Label(root, width=30, font='arial 16', bg='#95A2AA')
phne_entry.place(x=460, y=345)
email = Label(root, text='Price:', fg='white', bg='#002f42', font='arial 18 bold').place(x=365, y=400)
email_entry = Label(root, width=30, font='arial 16', bg='#95A2AA')
email_entry.place(x=460, y=400)

photo2 = PhotoImage(file="images/search0.png")
search = Button(root, command=search, image=photo2, bg='#002f42').place(x=850, y=237)
delete = Button(root, command=delete, text='Delete', bg='#54bec7', font='arial 20', width=15).place(x=250, y=530)
reset = Button(root, command=reset, text='Reset', bg='#54bec7', font='arial 20', width=15).place(x=650, y=530)

root.mainloop()