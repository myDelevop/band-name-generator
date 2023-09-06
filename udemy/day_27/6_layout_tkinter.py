from tkinter import *


def button_clicked():
    print("I got clicked")
    input_text = user_input.get()
    my_label.config(text=input_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=120, pady=120)  # This method adds padding to ALL components

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=50, pady=50)  # modifies padding only to this component
# my_label.pack()
# my_label.place(x=0, y=0) place the label in the top left corner
# my_label.place(x=100, y=200) place the label to specific position
my_label.grid(column=0, row=0)  # place the label in the top left corner


# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=3, row=2)


window.mainloop()
