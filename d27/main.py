from tkinter import *

def miles_to_km():
    try:
        calc_num = float(num_miles.get()) * 1.609
        answer_label.config(text=round(calc_num, 2))
    except ValueError:
        popup = Tk()
        popup.title("Error")
        popup.config(padx=10, pady=10)
        error_label = Label(popup, text="Please enter a number", font="Arial")
        error_label.grid(column=0, row=0)
        error_label.config(padx=10, pady=10)
        close_button = Button(popup, text="Close", command=popup.destroy)
        close_button.grid(column=0, row=1)
        popup.mainloop()

window = Tk()
window.title("Miles to KM")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles", font="Arial")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="KM", font="Arial")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

equal_label = Label(text="Equals", font="Arial")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

answer_label = Label(text="0", font="Arial")
answer_label.grid(column=1, row=1)
answer_label.config(padx=10, pady=10)

num_miles = Entry(width=10)
num_miles.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()