import tkinter as tk

def handle_input():
    input_str = input_entry.get()
    output_label.config(text="You entered: " + save_txt(input_str))

def write_to_file(string_to_write, file_path):
    with open(file_path, "w") as file:
        file.write(string_to_write)
        
def save_txt():
    input_str = input_entry.get()
    write_to_file(input_str,"document.txt")
    
# create a new window
window = tk.Tk()
window.title("My App")
window.geometry("400x300")

# create an input field
input_entry = tk.Entry(window)
input_entry.pack()

# create a button to handle the input
button = tk.Button(window, text="Submit", command=save_txt)
button.pack()

# create a label for output
output_label = tk.Label(window, text="")
output_label.pack()

# run the main loop
window.mainloop()
