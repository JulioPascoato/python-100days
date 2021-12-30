from tkinter import *


window = Tk()
window.title(string="Mile to Km Converter")
# window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

mile_input = Entry()
mile_input.config(width=7)
mile_input.grid(column=1, row=0)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

equal_label = Label()
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=5, pady=5)

result_label = Label()
result_label.config(text="0")
result_label.grid(column=1, row=1)

km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)


def converter():
    mile = float(mile_input.get())
    km = round(1.60934 * mile)
    result_label.config(text=km)


button = Button(text="Calculate", command=converter)

button.grid(column=1, row=2)

window.mainloop()
