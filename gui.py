import tkinter as tk
from tkinter import ttk, messagebox
from file_handling import save_text_to_docx

def show_loading_window():
    root = tk.Tk()
    root.title("Loading...")

    root.geometry("400x150")
    root.config(bg="#2e3b4e")
    root.resizable(False, False)

    label = tk.Label(root, text="Extracting Text from the Image...", font=("Arial", 14, "bold"), fg="white", bg="#2e3b4e")
    label.pack(pady=20)

    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
    progress.pack(pady=10)

    progress.start()
    root.after(6000, root.destroy)
    root.mainloop()

def display_text_in_gui(text):
    def save_and_exit():
        success, message = save_text_to_docx(text_widget.get("1.0", tk.END))
        if success:
            messagebox.showinfo("Success", "File saved successfully!")
        else:
            messagebox.showerror("Error", message)
        root.quit()

    root = tk.Tk()
    root.title("Text Display and Save")

    text_widget = tk.Text(root, height=10, width=50)
    text_widget.pack(pady=10)
    text_widget.insert(tk.END, text)

    save_button = tk.Button(root, text="Save to DOCX", command=save_and_exit)
    save_button.pack(side=tk.LEFT, padx=10, pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()
