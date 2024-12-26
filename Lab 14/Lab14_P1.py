import tkinter as tk

def display_text():
    # Get the text from entry_widget and set it as the label's text
    label.config(text   = entry_widget.get())

# Create the main window
root = tk.Tk()
root.title("Simple GUI Application") # Add your title here
root.geometry("300x200") # Add your size here
root.resizable(False, False) # This is for a fixed window size

# Create an Entry widget
entry_widget = tk.Entry(root, width=20)
entry_widget.grid(row=0, column=0)

# Create a Button
button = tk.Button(master=root, text="Click me", command=display_text) # Add label and the function event for the button here
button.grid(row=1, column=0)

# Create a Label
label = tk.Label()
label.grid(row=1, column=1)

# Create a Checkbutton
check_button = tk.Checkbutton(master=root, text="I agree")
check_button.grid(row=2, column=0)

# Create Radiobuttons
radio_value = tk.IntVar()
radio_button1 = tk.Radiobutton(master=root, text="Option 1", variable=radio_value, value=1)
radio_button1.grid(row=3, column=0)
radio_button2 = tk.Radiobutton(master=root, text="Option 2", variable=radio_value, value=2)
radio_button2.grid(row=3, column=1)

# Start the application
root.mainloop()