from tkinter import *
from tkinter import messagebox
import sqlite3


def submit():
    name = f_name.get()
    surname = l_name.get()
    phone_number = number.get()
    if name == "" or surname == "" or phone_number == "":
        messagebox.showerror("Info", "You forget something")
    elif not phone_number.isdigit():
        messagebox.showerror("Info", "Number Should Contain Only Digits")
    else:
        conn = sqlite3.connect(dtbs)
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS people (
                        f_name text,
                        l_name text,
                        number text
                        )""")

        c.execute("INSERT INTO people VALUES (:f_name, :l_name, :number)",
                  {
                      "f_name": f_name.get(),
                      "l_name": l_name.get(),
                      "number": number.get()
                  })

        conn.commit()
        conn.close()
        txt = "You added:\n {} {} - {}".format(f_name.get(), l_name.get(), number.get())
        messagebox.showinfo("Info", txt)

        f_name.delete(0, END)
        l_name.delete(0, END)
        number.delete(0, END)


def delete():
    conn = sqlite3.connect(dtbs)
    c = conn.cursor()

    c.execute("DELETE from people WHERE oid = " + del_box.get())

    del_box.delete(0, END)

    conn.commit()
    conn.close()


def edit():
    global editor
    editor = Tk()
    editor.title("Numbers Notebooks")
    editor.configure(background="white")

    conn = sqlite3.connect(dtbs)
    c = conn.cursor()

    c.execute("SELECT * FROM people WHERE oid  = " + del_box.get())
    records = c.fetchall()

    f_name_lbl_editor = Label(editor, text="Name", bg="grey80").grid(row=0, column=0, padx=20, pady=5)
    l_name_lbl_editor = Label(editor, text="Surname", bg="grey80").grid(row=1, column=0, padx=20, pady=5)
    number_lbl_editor = Label(editor, text="Number", bg="grey80").grid(row=2, column=0, padx=20, pady=5)

    global f_name_editor, l_name_editor, number_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    number_editor = Entry(editor, width=30)
    number_editor.grid(row=2, column=1, padx=20)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        number_editor.insert(0, record[2])

    conn.commit()
    conn.close()

    save_btn_editor = Button(editor, bg="grey60", text="Save",
                             command=save).grid(row=3, column=0, columnspan=2, ipadx=50, pady=(5, 30))

    editor.mainloop()


def query():
    conn = sqlite3.connect(dtbs)
    c = conn.cursor()

    c.execute("SELECT *, oid FROM people")
    records = c.fetchall()
    if not records:
        messagebox.showinfo("Info", "You don't have any contact\n\nPlease add somebody")
    else:
        k = 1
        for item in range(len(records)):
            st = records[item]
            name = st[0]
            surname = st[1]
            num = st[2]
            el = st[3]
            Label(root, text=str(k) + ". " + name + " " + surname + " " + num + " #" + str(el),
                  bg="white").grid(row=k + 7, column=0, columnspan=2)
            k += 1

    conn.commit()
    conn.close()


def save():
    conn = sqlite3.connect(dtbs)
    c = conn.cursor()

    c.execute("""UPDATE people  SET
        f_name = :first,
        l_name = :last,
        number = :number

        WHERE oid = :oid""",

              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'number': number_editor.get(),
                  'oid': del_box.get()
              }

              )

    conn.commit()
    conn.close()
    editor.destroy()
    del_box.delete(0, END)


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