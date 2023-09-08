from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

screen = Tk()
screen.title("Flashy")
# screen.minsize(width=900, height=600)
screen.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)


screen.mainloop()
