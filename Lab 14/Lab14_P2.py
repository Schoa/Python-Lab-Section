import tkinter as tk 
import ttkbootstrap as ttk

# window 
window = ttk.Window(themename = 'darkly')
window.title("Length converter")
window.geometry("300x150")

def convert():
    mile_input = int(entry_widget.get())
    km_output = mile_input * 1.61
    output_string.set(km_output)

# Label
label = tk.Label(
    window,
    text = "Miles to Kilometer",
    font = ("Calibri", 24, "bold")
)
label.grid(column = 0, row = 0)

# Entry widget
entry_widget = tk.Entry(window)
entry_widget.grid(column = 0, row = 1)

# Button
button = tk.Button(master = window, text="Convert", command=convert)
button.grid(row = 2, column = 0)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = 'Output', 
    font = 'Calibri 24',
    textvariable = output_string)
output_label.grid(column = 0, row = 3)

# run 
window.mainloop()