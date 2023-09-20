import os
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

def print_dir_structure(path='.', level=0):
    """Recursively print the structure of the directory."""
    output = ''
    output += '  ' * level + '|-- ' + os.path.basename(path) + '\n'
    
    if os.path.isdir(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            output += print_dir_structure(child_path, level + 1)
    return output

def show_structure():
    dir_path = filedialog.askdirectory(title="Select Directory")
    if not dir_path:
        return
    structure = print_dir_structure(dir_path)
    txt_display.delete(1.0, tk.END)
    txt_display.insert(tk.END, structure)

app = tk.Tk()
app.title("Directory Structure Viewer")

btn_select_dir = ctk.CTkButton(app, text="Select Directory", command=show_structure)
btn_select_dir.pack(pady=20)

txt_display = tk.Text(app, wrap=tk.WORD, width=80, height=20)
txt_display.pack(padx=20, pady=20)

app.mainloop()
