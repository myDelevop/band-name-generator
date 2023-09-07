from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="#D3D3D3", padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg="#D3D3D3", highlightthickness=0,)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()  # for now
# canvas.grid(column=0, row=0, padx=20, pady=20)


window.mainloop()
