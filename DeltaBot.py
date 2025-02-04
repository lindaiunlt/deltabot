import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def merge_files(file_paths):
    content = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content.append(file.read())
    return content

def save_merged_file(merged_text):
    save_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if save_path:
        try:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(merged_text)
            messagebox.showinfo("Success", "Merged file saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def select_files():
    file_paths = filedialog.askopenfilenames(title="Select Text Files",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_paths:
        content = merge_files(file_paths)
        merged_text = "\n\n".join(content)
        display_comparison(content)
        save_merged_file(merged_text)

def display_comparison(content):
    comparison_window = tk.Toplevel(root)
    comparison_window.title("DeltaBot - Comparison Interface")

    text_widgets = []
    for idx, text in enumerate(content):
        text_widget = scrolledtext.ScrolledText(comparison_window, wrap=tk.WORD, width=50, height=20)
        text_widget.insert(tk.END, text)
        text_widget.configure(state='disabled')
        text_widget.grid(row=0, column=idx, padx=5, pady=5)
        text_widgets.append(text_widget)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("DeltaBot - File Merger and Comparator")

    select_button = tk.Button(root, text="Select Text Files", command=select_files)
    select_button.pack(pady=20)

    root.mainloop()