from tkinter import *
from tkinter import messagebox
import sqlite3

def submit():
    pass

def delete():
    pass

def edit():
    pass

def query():
    pass

root = Tk()
root.title("Numbers Notebooks")
root.iconbitmap("Photo\\Contacts.ico")
root.configure(background="white")
dtbs = "contact_list.db"

f_name_lbl = Label(root, text="Name", bg="grey80").grid(row=0, column=0, padx=20, pady=5)
l_name_lbl = Label(root, text="Surname", bg="grey80").grid(row=1, column=0, padx=20, pady=5)
number_lbl = Label(root, text="Number", bg="grey80").grid(row=2, column=0, padx=20, pady=5)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
number = Entry(root, width=30)
number.grid(row=2, column=1, padx=20)

submit_btn = Button(root, bg="grey60", text="Add to Contact",
                    command=submit).grid(row=3, column=0, columnspan=2, ipadx=50, pady=(5, 30))

del_btn = Button(root, bg="grey60", text="Delete ID",
                 command=delete).grid(row=4, column=0, columnspan=2, ipadx=10, pady=0)
del_box_lbl = Label(root, text="ID", bg="grey80").grid(row=5, column=0, padx=20, pady=0)
del_box = Entry(root, width=30)
del_box.grid(row=5, column=1, padx=20, pady=5)
upd_btn = Button(root, bg="grey60", text="Update ID",
                 command=edit).grid(row=6, column=0, columnspan=2, ipadx=10, pady=0)

query_btn = Button(root, bg="grey60", text="Show All My Contacts",
                   command=query).grid(row=7, column=0, columnspan=2, ipadx=40, pady=(30, 5))

root.mainloop()