import tkinter as tk
from tkinter import ttk
import random

first_names = ["Alice", "Bob", "Charlie", "Diana",
               "Ethan", "Fiona", "George", "Hannah", "Ivy", "Jack"]
last_names = ["Smith", "Johnson", "Williams", "Brown",
              "Jones", "Garcia", "Miller", "Davis", "Martinez", "Wilson"]


def select_item(_):
    # print selected item
    for i in treeview.selection():
        print(treeview.item(i)["values"])


def delete_item(_):
    # delete item
    treeview.delete(treeview.selection())


# Initialize the main window
window = tk.Tk()
window.title("Combobox & Spinbox")
window.geometry("700x400")

# create Treeview
treeview = ttk.Treeview(window,
                        columns=("firstname", "lastname", "email"),
                        show="headings")
treeview.pack(pady=(15, 0))

# create Treeview heading
treeview.heading("firstname", text="Firstname")
treeview.heading("lastname", text="Lasttname")
treeview.heading("email", text="email")

# insert data into Treeview
for i in range(100):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    email = f"{fname}-{lname}@email.com"
    treeview.insert(parent="", index=0, values=(fname, lname, email))


# add events
treeview.bind("<<TreeviewSelect>>", select_item)  # item selection event
treeview.bind("<Delete>", delete_item)  # pressing delete button

window.mainloop()
