from tkinter import *

admin = Tk()
admin.title("Billing Software")
admin.geometry("1100x700")
admin.resizable(0,0)

lbmain = Label(admin, text='Admin', font='arial 18 bold', bg='#002f42', fg='#54bec7', pady=20).pack(fill='x')

frame1 = LabelFrame(admin, text='Add Product', font='arial 16', bg='#54bec7', bd=12, width=750, height=310).pack()
frame2 = LabelFrame(admin, text='Update Product', font='arial 16', bg='#54bec7', bd=12, width=750, height=310).pack()

lb1 = Label(frame1, text='Enter Product Name:', font='arial 12', padx=10, pady=5, bg='#54bec7').place(x=250, y=150)
e1 = Entry(frame1, font='arial 12', width=30).place(x=450, y=155)
lb2 = Label(frame1, text='Enter Product Price:\n (per unit)', font='arial 12', padx=10, pady=5, bg='#54bec7').place(x=250, y=200)
e2 = Entry(frame1, font='arial 12', width=30).place(x=450, y=205)
btn1 = Button(frame1, text='Clear', font='arial 12', padx=10).place(x=520, y=280)
btn1 = Button(frame1, text='Add Product', font='arial 12', padx=10).place(x=600, y=280)


admin.mainloop()