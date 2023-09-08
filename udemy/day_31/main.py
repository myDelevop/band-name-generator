import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (pandas.errors.EmptyDataError, FileNotFoundError):
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_tile, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = screen.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)

    data_csv = pandas.DataFrame(to_learn)
    data_csv.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def flip_card():
    canvas.itemconfig(card_tile, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


screen = Tk()
screen.title("Flashy")
# screen.minsize(width=900, height=600)
screen.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = screen.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_tile = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

screen.mainloop()
