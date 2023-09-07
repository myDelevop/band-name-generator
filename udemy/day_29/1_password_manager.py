import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_psw():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    psw_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_psw():
    website_string = website_entry.get().strip()
    user_string = user_entry.get().strip()
    psw_string = psw_entry.get().strip()

    # if website_string == "" or psw_string == "" or user_string == "":
    #     messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")

    if website_string == "":
        messagebox.showinfo(title="Empty field", message="You must insert a website")
    elif user_string == "":
        messagebox.showinfo(title="Empty field", message="You must insert a user")
    elif psw_string == "":
        messagebox.showinfo(title="Empty field", message="You must insert a password")
    else:
        is_ok = messagebox.askokcancel("Insert Values",
                                       "These are the details entered: \n"
                                       f"website: {website_string}\n"
                                       f"user: {user_string}\n"
                                       f"password: {psw_string}\n"
                                       "Is it ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website_string} | {user_string} | {psw_string}\n")
            f.close()
            messagebox.showinfo(title="Success", message="Your record has been inserted successfully")
            website_entry.delete(0, END)
            psw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="#D3D3D3", padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="#D3D3D3", highlightthickness=0, )
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
