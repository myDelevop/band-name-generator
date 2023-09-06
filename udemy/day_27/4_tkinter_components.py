from tkinter import *


def button_clicked():
    print("I got clicked")
    input_text = user_input.get()
    my_label.config(text=input_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")

my_label.pack()


# Button
button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
user_input = Entry(width=10)
user_input.pack()


window.mainloop()
