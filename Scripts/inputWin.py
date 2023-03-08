from tkinter import *
import tkinter as tk
from tkinter import ttk
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
        
def lost_in_translate():
    input_str = input_entry.get("1.0","end")
    write_to_file(input_str,"document.txt")
    summary = SummarizeTesting.generate_summary("document.txt")
    ans = []
    eng = []
    for i in range(len(summary)):
        # Translate to a random language initially
        translated_summary = translate_Sentences.translateSentence(summary[i], languages[random.randint(0, len(languages) - 1)])
        ans.append(translated_summary)
        eng.append(translate_Sentences.translateEnglish(translated_summary))
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(ans))
    eng_text.delete("1.0", tk.END)
    eng_text.insert(tk.END, "\n".join(eng))
        
def save_txt():
    input_str = input_entry.get("1.0","end")
    write_to_file(input_str,"document.txt")
    summary = SummarizeTesting.generate_summary("document.txt")
    ans = []
    eng = []
    for i in range(len(summary)):
        # Translate to a random language initially
        translated_summary = translate_Sentences.translateSentence(summary[i], languages[random.randint(0, len(languages) - 1)])
        ans.append(translated_summary)
        eng.append(translate_Sentences.translateEnglish(translated_summary))
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(ans))
    eng_text.delete("1.0", tk.END)
    eng_text.insert(tk.END, "\n".join(eng))
    if(len(eng) > 1):
        summarizesummary(eng)
    else:
        return
      
def summarizesummary(summary_str):
      for i in range(len(summary_str)):
          write_to_file(summary_str[i],"document.txt")
      summary = SummarizeTesting.generate_summary("document.txt")
      ans = []
      eng = []
      for i in range(len(summary)):
          # Translate to a random language initially
          translated_summary = translate_Sentences.translateSentence(summary[i], languages[random.randint(0, len(languages) - 1)])
          ans.append(translated_summary)
          eng.append(translate_Sentences.translateEnglish(translated_summary))
      output_text.delete("1.0", tk.END)
      output_text.insert(tk.END, "\n".join(ans))
      eng_text.delete("1.0", tk.END)
      eng_text.insert(tk.END, "\n".join(eng))
      if(len(eng) > 1):
          summary_str = eng
          summarizesummary(summary_str)
      else:
          return

# create a new window
window = tk.Tk()
window.title("Lost in Translation")
window.geometry("690x690")

# main
main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)

# canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar
my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
scrollable_frame = ttk.Frame(my_canvas)
scrollable_frame.pack(fill=BOTH, expand=1)
scrollable_frame.bind(
    "<Configure>",
    lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")
    )
)
my_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
my_canvas.configure(yscrollcommand=my_scrollbar.set)
# create an input field
input_entry = tk.Text(scrollable_frame, width=69, height=20)
input_entry.pack()

# create a button to handle the input
button = tk.Button(scrollable_frame, text="Paragraph Summarize", command=lost_in_translate)
button.pack()

button2 = tk.Button(scrollable_frame, text="Summarize the summarize", command = save_txt)
button2.pack()

# create a frame for output
output_frame = tk.Frame(scrollable_frame, width=69, height=20)
output_frame.pack()
output_frame.pack_propagate(True) # stop frame from resizing based on contents

# create a label for output
output_text = tk.Text(output_frame)
output_text.pack(fill=tk.BOTH, expand=True)

# create a frame for output
eng_frame = tk.Frame(scrollable_frame, width=69, height=20)
eng_frame.pack()
eng_frame.pack_propagate(True) # stop frame from resizing based on contents

# create a label for output
eng_text = tk.Text(eng_frame)
eng_text.pack(fill=tk.BOTH, expand=True)

# run the main loop
window.mainloop()
