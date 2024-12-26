import tkinter as tk 
import ttkbootstrap as ttk

# window 
window = ttk.Window(themename = 'darkly')
# Your code is here

# title 
# Your code is here

# input field 
# Your code is here
# The entry name should be entry_int

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

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