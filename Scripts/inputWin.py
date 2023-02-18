import tkinter as tk
import random
import SummarizeTesting
import translate

languages = [
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr',
    'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw',
    'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la',
    'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt',
    'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta',
    'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]

random_number = random.randint(0, len(languages) - 1)

def handle_input():
    input_str = input_entry.get()
    output_label.config(text="You entered: " + save_txt(input_str))

def write_to_file(string_to_write, file_path):
    with open(file_path, "w") as file:
        file.write(string_to_write)
        
def save_txt():
    input_str = input_entry.get()
    write_to_file(input_str,"document.txt")
    summary = SummarizeTesting.generate_summary("document.txt")
    translated_summary = []
    for sentence in summary:
        translated_sentence = translate.translateSentence(sentence, languages[random.randint(0, len(languages) - 1)])
        translated_summary.append(translated_sentence)
    summary_text = "\n".join(translated_summary)
    output_window = tk.Toplevel(window)
    output_label = tk.Label(output_window, text=summary_text)
    output_label.pack()

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
