import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

#
print("running......")

# ------- Generate test data -------


def generate():
    range_x = int(x_range_entry.get().strip())
    range_y = int(y_range_entry.get().strip())
    # generate random x and y values within range_x and range_y
    x = np.random.randint(-range_x, range_x, size=10)
    y = np.random.randint(-range_y, range_y, size=10)
    data = {'x': x, 'y': y}
    df_data = DataFrame(data, columns=data.keys())
    # print(df_data)
    # plot the data
    fig = plt.Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    ax.set_title('Scatter Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    scatter = FigureCanvasTkAgg(fig, window)
    scatter.get_tk_widget().grid(row=1, column=0, columnspan=5, rowspan=5)

    # return data


# ------- Save data to (kml) file -------

# ------- GUI setup -------
window = tk.Tk()
window.title('Sample Plotter')
# window.geometry('800x600')

# labels, entry boxes, buttons
x_range_label = tk.Label(text="x range:")
x_range_entry = tk.Entry(width=5)
x_range_entry.insert(0, '10')
y_range_label = tk.Label(text="y range:")
y_range_entry = tk.Entry(width=5)
y_range_entry.insert(0, '10')
generate_btn = tk.Button(text='Generate', command=generate)

# positions
x_range_label.grid(row=0, column=0)
x_range_entry.grid(row=0, column=1)
y_range_label.grid(row=0, column=2)
y_range_entry.grid(row=0, column=3)
generate_btn.grid(row=0, column=4)

window.mainloop()

# ------- test -------

# generate(10, 10)
