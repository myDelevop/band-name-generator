import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a label", font=("Arial", 24, "italic"))
my_label.pack(side="bottom")


window.mainloop()
