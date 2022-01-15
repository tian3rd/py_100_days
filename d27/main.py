from curses import window
import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)


def calculate(mile=0):
    km = mile * 1.60934
    km_label.config(text=f'{km:.2f}')


mile_entry = tk.Entry(width=10)
mile_entry.grid(row=0, column=1)

mile_label = tk.Label(text="Miles")
mile_label.config(width=10)
mile_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="=")
is_equal_label.config(width=10)
is_equal_label.grid(row=1, column=0)

km_label = tk.Label(text="")
km_label.config(text="0")
km_label.grid(row=1, column=1)

km_unit_lable = tk.Label(text="Km(s)")
km_unit_lable.grid(row=1, column=2)

calc_btn = tk.Button(
    text="Calculate", command=lambda: calculate(float(mile_entry.get())))
calc_btn.grid(row=2, column=2)


window.mainloop()
