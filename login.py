from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

def toggle_password():
    if checkbutton.var.get():
        txtPassword['show'] = ""
    else:
        txtPassword['show'] = "*"

def login():
    uname = txtUsername.get()
    pwd = txtPassword.get()
    if uname=="" or pwd=="":
        messagebox.showerror("Error","Enter User Name And Password")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="12345678", database="billing_user")
            cursor = con.cursor()
            cursor.execute("select * from login where username=%s and password = %s", (uname,pwd))
            row = cursor.fetchone()
            if row==None:
                messagebox.showerror(title="Error", message="Invalid Username or Password")
            else:
                messagebox.showinfo(title="Status", message="Login Successful")
                root.destroy()
                import SupermarketBilling
            con.commit()
            con.close()
        except Exception as es:
            messagebox.showinfo(title="Error", message=f"Error : {str(es)}")

root = Tk()

root.title("Supermarket Billing System - Login Page")
root.geometry("1100x700+200+60")
root.resizable(0, 0)
root.config(bg='#002f42')

frame = Frame(root, bg="#ECECEC",width=550,height=700)
frame.place(x=0,y=0)

picSupermarket = PhotoImage(file="images/Supermarket.png")
lbpic = Label(frame, image=picSupermarket)
lbpic.place(x=25,y=20)

lbSupermarket = Label(frame, text="Supermarket\nBilling\nSystem", font='Montserrat 50 bold', fg='#002f42')
lbSupermarket.place(x=130,y=400)

lbLogin = Label(root, text="Login Page", font='Montserrat 30 bold', fg='white', bg='#002f42')
lbLogin.place(x=740, y=100)

lbUsername = Label(root, text="Enter Username", font='Montserrat 30 bold', fg='#82DEE4', bg='#002f42')
lbUsername.place(x=600, y=200)
lbPassword = Label(root, text="Enter Password", font='Montserrat 30 bold', fg='#82DEE4', bg='#002f42')
lbPassword.place(x=600, y=350)

txtUsername = Entry(root, bg='#002f42', borderwidth=0, highlightthickness=0, font='Montserrat 30', fg='white')
txtUsername.place(x=600, y=250)

line1 = Canvas(root, width=400, highlightthickness=0, height=2, bg='white')
line1.place(x=600,y=300)

txtPassword = Entry(root, bg='#002f42', borderwidth=0, highlightthickness=0, font='Montserrat 30', fg='white', show="*")
txtPassword.place(x=600, y=400)

line2 = Canvas(root, width=400, highlightthickness=0, height=2, bg='white')
line2.place(x=600,y=450)

btnlogin = Button(root, text="Login", fg='#002f42', highlightbackground='#82DEE4', font='Montserrat 30 bold', borderwidth=2, command=login)
btnlogin.place(x=760, y=520)

checkbutton = Checkbutton(root, text="Show password", font='Montserrat 15', fg='white', bg='#002f42', onvalue=True, offvalue=False, command=toggle_password)
checkbutton.var = BooleanVar(value=False)
checkbutton['variable'] = checkbutton.var
checkbutton.place(x=600, y=460)

root.mainloop()