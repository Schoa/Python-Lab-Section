import tkinter as tk

def click_button(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        clear_display()
        display.insert(0, "Error")

# Window initialization
# Your code is here
    # The window name is root

# Display block initialization
# Your code is here
    # The display Entry widget's name is display


# Buttons initialization
# Your code is here
    # The button list's name is buttons

for (text, row, col) in buttons:
    if text == "Clear":
        tk.Button(root, text=text, width=9, height=2, command=lambda: clear_display()).grid(row=row, column=col)
    elif text == "=":
        tk.Button(root, text=text, width=9, height=2, command=lambda: calculate()).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=9, height=2, command=lambda text=text: click_button(text)).grid(row=row, column=col)

root.mainloop()