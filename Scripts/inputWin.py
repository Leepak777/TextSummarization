import tkinter as tk
import random
import SummarizeTesting
import translate_Sentences

languages = [
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr',
    'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw',
    'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la',
    'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt',
    'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta',
    'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]


def handle_input():
    input_str = input_entry.get()
    output_label.config(text="You entered: " + input_str)

def write_to_file(string_to_write, file_path):
    with open(file_path, mode="w", encoding="utf-8") as file:
        file.write(string_to_write)
        
def save_txt():
    input_str = input_entry.get("1.0","end")
    write_to_file(input_str,"document.txt")
    summary = SummarizeTesting.generate_summary("document.txt")
    ans = []
    for i in range(len(summary)):
        # Translate to a random language initially
        translated_summary = translate_Sentences.translateSentence(summary[i], languages[random.randint(0, len(languages) - 1)])
        ans.append(translated_summary)
        print(translated_summary)
    output_label.config(text="\n".join(ans))
    return ans

# create a new window
window = tk.Tk()
window.title("My App")
window.geometry("690x690")

# create an input field
input_entry = tk.Text(window, width = 69, height = 42)
input_entry.pack()

# create a button to handle the input
button = tk.Button(window, text="Submit", command=save_txt)
button.pack()

# create a frame for output
output_frame = tk.Frame(window)
output_frame.pack(fill=tk.BOTH, expand=True)
output_frame.pack_propagate(False) # stop frame from resizing based on contents

# create a label for output
output_label = tk.Label(output_frame, text="")
output_label.pack(fill=tk.BOTH, expand=True)

# run the main loop


# run the main loop
window.mainloop()
