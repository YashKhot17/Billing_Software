from tkinter import *
from tkinter import messagebox
import pymysql


# --------------------------------------- Signup Method ---------------------------- #


def signup():
    email = email_input.get()
    username = username_input.get()
    password = password_input.get()
    retype = password1_input.get()

    if email == "" or username == "" or password == "":
        messagebox.showerror('Error','All fields are required!!')

    elif retype != password:
        messagebox.showerror('Password Error', "Password doesn't match")

    else:
        con=pymysql.connect(host='localhost',user='root',password='SAMSEVEN',database='billing_user')
        cur=con.cursor()
        cur.execute('select * from users where email=%s',email)
        row=cur.fetchone()
        if row!=None:
            messagebox.showerror('Error','User with given email already exists')
        else:
            cur.execute('insert into users(email,username,password) values(%s,%s,%s)',(email,username,password))
            con.commit()
            con.close()

            messagebox.showinfo('Signed Up','You have been signed up successfully')
            window.destroy()
            import login


#  --------------------------------------------- GUI ---------------------------------- #
window = Tk()
window.title("Stock Manager")
window.geometry("1100x700")
window.config(bg="#002f42")
window.resizable(False, False)

frame = Frame(window, width=550, height=700)
frame.grid(row=0, column=0, rowspan=10)

email_label = Label(text="Enter Email Id", bg="#002f42", fg="white", font=("Ariel", 20))
email_input = Entry(bg="#54bec7", width=40, fg="white", font=("Ariel", 15))

email_label.grid(column=1, row=1)
email_input.grid(column=1, row=2, sticky="we", padx=40)

username_label = Label(text="Enter Username", bg="#002f42", fg="white", font=("Ariel", 20))
username_input = Entry(bg="#54bec7", width=40, fg="white", font=("Ariel", 15))

username_label.grid(column=1, row=3)
username_input.grid(column=1, row=4, sticky="we", padx=40)

password_label = Label(text="Enter Password", bg="#002f42", fg="white", font=("Ariel", 20))
password_input = Entry(bg="#54bec7", show="*", width=40, fg="white", font=("Ariel", 15))

password_label.grid(column=1, row=5)
password_input.grid(column=1, row=6, sticky="we", padx=40)

password1_label = Label(text="Retype Password", bg="#002f42", fg="white", font=("Ariel", 20))
password1_input = Entry(bg="#54bec7", width=40, fg="white", font=("Ariel", 15))

password1_label.grid(column=1, row=7)
password1_input.grid(column=1, row=8, sticky="we", padx=40)

submit = Button(text="Signup", font=("Ariel", 20), command=signup)
submit.config(bg="#54bec7", fg="white")
submit.grid(column=1, row=9)
window.mainloop()