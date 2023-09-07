import time
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_psw():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_psw():
    global empty_field
    website_string = website_entry.get().strip()
    user_string = user_entry.get().strip()
    psw_string = psw_entry.get().strip()

    empty_field.config(fg="red")
    if website_string == "":
        empty_field.config(text="Insert the website")
    elif user_string == "":
        empty_field.config(text="Insert a username")
    elif psw_string == "":
        empty_field.config(text="Insert the password")
    else:
        f = open("data.txt", "a")
        f.write(f"{website_string} | {user_string} | {psw_string}\n")
        f.close()
        empty_field.config(fg="green", text="Password Added Successfully")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="#D3D3D3", padx=50, pady=50)

empty_field = Label(text="", bg="#D3D3D3", fg="red")
empty_field.grid(row=5, column=1)


canvas = Canvas(width=200, height=200, bg="#D3D3D3", highlightthickness=0,)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="#D3D3D3")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

user_label = Label(text="Email/Username:", bg="#D3D3D3")
user_label.grid(row=2, column=0)

user_entry = Entry(width=35)
user_entry.focus()
user_entry.insert(0, "angela@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

psw_label = Label(text="Password:", bg="#D3D3D3")
psw_label.grid(row=3, column=0)

psw_entry = Entry(width=32)
psw_entry.focus()
psw_entry.grid(row=3, column=1, sticky="W")

generate_psw_button = Button(text="Generate Password", command=generate_psw)
generate_psw_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save_psw, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
