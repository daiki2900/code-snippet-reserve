import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def combobox_selected(event, label):
    label.config(text=f"({combobox_var.get()}) is selected")


# Initialize the main window
window = tk.Tk()
window.title("Combobox & Spinbox")
window.geometry("600x400")

# create combobox
fruits_list = ["Banana", "Orange", "Apple"]
combobox_var = tk.StringVar(value=fruits_list[0])
combobox_fruits = ttk.Combobox(window, textvariable=combobox_var)
combobox_fruits["values"] = fruits_list
combobox_fruits.pack(pady=(15, 0))

# create label that holds selected fruit
label = ttk.Label(window, text="Select a fruit")
label.pack(pady=(15, 0))

# bind events to combobox
combobox_fruits.bind("<<ComboboxSelected>>",
                     lambda event: label.config(text=f"{combobox_var.get()} is selected."))


# creat Spinbox
spinbox_var = tk.IntVar(value=2)
spinbox = ttk.Spinbox(window, from_=2, to=10,
                      increment=2, textvariable=spinbox_var)
spinbox.pack(pady=(15, 0))
spinbox.bind("<<Increment>>",
             lambda event: print(f"Spinbox is Incremented to: {spinbox_var.get()}"))
spinbox.bind("<<Decrement>>",
             lambda event: print(f"Spinbox is Decremented to: {spinbox_var.get()}"))


# create Spinbox with (A, B, C, D, E)
spinbox2_var = tk.StringVar(value="A")
spinbox2 = ttk.Spinbox(window, textvariable=spinbox2_var)
spinbox2["values"] = ("A", "B", "C", "D", "E")
spinbox2.pack(pady=(15, 0))

spinbox2.bind("<<Increment>>", lambda event: print(
    f"Spinbox2 value is Incremented to {spinbox2_var.get()}"))
spinbox2.bind("<<Decrement>>", lambda event: print(
    f"Spinbox2 value is Decremented to {spinbox2_var.get()}"))
# Start the Tkinter event loop
window.mainloop()
