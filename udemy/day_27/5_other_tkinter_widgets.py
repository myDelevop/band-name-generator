from tkinter import *


def action():
    print("Do something")


def spinbox_used():
    print(spinbox.get())


def scale_used(value):
    print(value)


def check_button_used():
    # Prints 1 if On button checked, 0 otherwise
    print(checked_state.get())


def radio_used():
    print(radio_state.get())


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

# Buttons
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with")
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()


# Spinbox
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CheckButton
checked_state = IntVar()  # 0 if off, 1 if on
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=check_button_used)
checked_state.get()
checkbutton.pack()


# Radio Button
radio_state = IntVar()
radiobutton_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton_1.pack()
radiobutton_2.pack()


# Listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
