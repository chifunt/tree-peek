import os
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

def print_dir_structure(path='.', level=0):
    """Recursively print the structure of the directory in Markdown format."""
    output = '    ' * level + '* ' + os.path.basename(path) + '\n'
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
    txt_display.config(state=tk.NORMAL)
    txt_display.delete(1.0, tk.END)
    txt_display.insert(tk.END, structure)
    txt_display.config(state=tk.DISABLED)
    btn_copy.configure(state=tk.NORMAL)

def copy_to_clipboard():
    content = txt_display.get(1.0, tk.END)
    app.clipboard_clear()
    app.clipboard_append(content)

def setup_buttons(frame):
    btn_select_dir = ctk.CTkButton(
        frame, text="Select Directory", command=show_structure, 
        fg_color=color_primary, hover_color=color_secondary, 
        text_color=color_text, font=font_tuple
    )
    btn_select_dir.grid(row=0, column=0, padx=(0,50))

    btn_copy = ctk.CTkButton(
        frame, text="Copy", command=copy_to_clipboard, state=tk.DISABLED, 
        fg_color=color_primary, hover_color=color_secondary, 
        text_color=color_text, text_color_disabled=color_disabled, font=font_tuple
    )
    btn_copy.grid(row=0, column=1)
    return btn_copy

def setup_text_display(frame):
    txt_display = tk.Text(frame, wrap=tk.WORD, width=80, height=20)
    txt_display.insert(tk.END, "Please select a directory to view its structure.")
    txt_display.config(state=tk.DISABLED)
    txt_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, command=txt_display.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    txt_display.configure(yscrollcommand=scrollbar.set)
    return txt_display

if __name__ == "__main__":
    app = tk.Tk()
    app.title("TreePeek")

    # Constants
    color_primary = "#519872"
    color_secondary = "#3B5249"
    color_text = "#F0F4EF"
    color_disabled = "#34252F"
    font_tuple = ("Roboto", 25)

    frame_buttons = tk.Frame(app)
    frame_buttons.pack(pady=(20, 0))
    btn_copy = setup_buttons(frame_buttons)

    frame_txt_display = tk.Frame(app)
    frame_txt_display.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    txt_display = setup_text_display(frame_txt_display)

    app.mainloop()
