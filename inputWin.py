import tkinter as tk

def handle_input():
    input_str = input_entry.get()
    output_label.config(text="You entered: " + input_str)

# create a new window
window = tk.Tk()
window.title("My App")
window.geometry("400x300")

# create an input field
input_entry = tk.Entry(window)
input_entry.pack()

# create a button to handle the input
button = tk.Button(window, text="Submit", command=handle_input)
button.pack()

# create a label for output
output_label = tk.Label(window, text="")
output_label.pack()

# run the main loop
window.mainloop()