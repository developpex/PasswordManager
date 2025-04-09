from tkinter import Label, Entry, Button

def create_label(text, row, column, **kwargs):
    label = Label(text=text)
    label.grid(row=row, column=column, **kwargs)
    return label

def create_entry(width, row, column, columnspan=1, default="", **kwargs):
    entry = Entry(width=width)
    entry.grid(row=row, column=column, columnspan=columnspan, **kwargs)
    entry.insert(0, default)
    return entry

def create_button(text, command, row, column, columnspan=1, width=None, **kwargs):
    button = Button(text=text, command=command, width=width)
    button.grid(row=row, column=column, columnspan=columnspan, **kwargs)
    return button