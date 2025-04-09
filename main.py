from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from logic.generator import Password
from logic.storage import load_data, save_data, find_website_data
from ui.components import create_entry, create_label, create_button
from ui.helper import clear_entries, insert_entries
from config import DATA_FILE
import pyperclip

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        result = find_website_data(DATA_FILE, website)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="The data file does not exist.")
    except JSONDecodeError:
        messagebox.showerror(title="File Corrupted", message="Couldn't read the data file.")
    else:
        if result:
            email = result["email"]
            password = result["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showwarning(title="Website not found", message="No website found in storage.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = Password().generate()
    if len(password_entry.get()) == 0:
        insert_entries(password_entry, input=password)
    else:
        clear_entries(password_entry)
        insert_entries(password_entry, input=password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password":password
        }
    }

    if len(website) == 0:
        messagebox.showwarning(title="No website", message="Please enter a website")
        return

    elif len(password) == 0:
        messagebox.showwarning(title="No Password", message="Please enter a password")
        return

    else:
        is_ok = messagebox.askokcancel(
            title="Save Password",
            message=(
                f"Details:\n"
                f"Website: {website}\n"
                f"Email: {email}\n"
                f"Password: {password}\n\n"
                f"Is it okay to save?"
            )
        )

        if is_ok:
            data = {}
            try:
                data = load_data(DATA_FILE)
            except (FileNotFoundError, JSONDecodeError):
                pass

            data.update(new_data)
            save_data(DATA_FILE, data)

            clear_entries(password_entry, website_entry)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="assets/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)

# Labels
create_label("Website:", row=1, column=0, sticky="e", pady=(10, 0))
create_label("Email/Username:", row=2, column=0, sticky="e", pady=(10, 0))
create_label("Password:", row=3, column=0, sticky="e", pady=(10, 0))

# Entries
website_entry = create_entry(22, row=1, column=1, pady=(10, 0), sticky="w")
email_entry = create_entry(42, row=2, column=1, columnspan=2, default="patrick@email.com", pady=(10, 0), sticky="w")
password_entry = create_entry(22, row=3, column=1, pady=(10, 0), sticky="w")

# Buttons
create_button("Search", command=search, row=1, column=2, width=15, sticky="w", pady=(10, 0))
create_button("Generate Password", command=generate_password, row=3, column=2, width=15, sticky="w", pady=(10, 0))
create_button("Add", command=save_password, row=4, column=1, columnspan=2, width=35, pady=(10, 0))

window.mainloop()