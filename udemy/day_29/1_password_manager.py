from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_psw():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_psw():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passw ord Manager")
window.config(bg="#D3D3D3", padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="#D3D3D3", highlightthickness=0,)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="#D3D3D3")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

user_label = Label(text="Email/Username:", bg="#D3D3D3")
user_label.grid(row=2, column=0)

user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

psw_label = Label(text="Password:", bg="#D3D3D3")
psw_label.grid(row=3, column=0)

psw_entry = Entry(width=32)
psw_entry.grid(row=3, column=1, sticky="W")

generate_psw_button = Button(text="Generate Password", command=generate_psw)
generate_psw_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save_psw, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
