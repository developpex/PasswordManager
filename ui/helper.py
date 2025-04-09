from tkinter import *

def clear_entries(*entries):
    for entry in entries:
        entry.delete(0, END)

def insert_entries(*entries, input):
    for entry in entries:
        entry.insert(0, input)