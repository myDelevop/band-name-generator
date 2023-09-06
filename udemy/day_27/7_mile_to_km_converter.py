from tkinter import *


def convert_miles_to_km():
    user_input = float(miles_entry.get())
    km = user_input * 1.6
    km_num_label.config(text=str(int(km)))
    print(km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)
# window.minsize(width=500, height=300)

miles_entry = Entry(width=10, takefocus=True)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles", padx=10, font=("Arial", 10, "bold"))
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", pady=10, padx=5, font=("Arial", 11, "normal"))
equal_label.grid(row=1, column=0)


km_num_label = Label(text="0", pady=10, padx=5, font=("Arial", 11, "normal"))
km_num_label.grid(row=1, column=1)


km_label = Label(text="Km", pady=10, padx=5, font=("Arial", 11, "normal"))
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
