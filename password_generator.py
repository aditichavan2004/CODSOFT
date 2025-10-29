import tkinter as tk
from tkinter import messagebox
import random
import string

# ----------------- Functions ----------------- #
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
        result_entry.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number!")

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ----------------- GUI Setup ----------------- #
root = tk.Tk()
root.title("🔐 Password Generator 🔐")
root.geometry("480x360")
root.resizable(False, False)
root.configure(bg="#f5f5f5")  # light neutral background

# ----------------- Heading ----------------- #
heading = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
heading.pack(pady=15)

# ----------------- Length Frame ----------------- #
length_frame = tk.Frame(root, bg="#ffffff", relief="ridge", bd=2)
length_frame.pack(pady=10, padx=20, fill="x")

length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#ffffff", fg="#333")
length_label.pack(side=tk.LEFT, padx=10, pady=10)
length_entry = tk.Entry(length_frame, width=5, font=("Arial", 12))
length_entry.pack(side=tk.LEFT, padx=5, pady=10)

# ----------------- Options Frame ----------------- #
options_frame = tk.Frame(root, bg="#ffffff", relief="ridge", bd=2)
options_frame.pack(pady=10, padx=20, fill="x")

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var, bg="#ffffff", font=("Arial", 11)).pack(side=tk.LEFT, padx=10, pady=10)
tk.Checkbutton(options_frame, text="Lowercase", variable=lowercase_var, bg="#ffffff", font=("Arial", 11)).pack(side=tk.LEFT, padx=10, pady=10)
tk.Checkbutton(options_frame, text="Numbers", variable=numbers_var, bg="#ffffff", font=("Arial", 11)).pack(side=tk.LEFT, padx=10, pady=10)
tk.Checkbutton(options_frame, text="Symbols", variable=symbols_var, bg="#ffffff", font=("Arial", 11)).pack(side=tk.LEFT, padx=10, pady=10)

# ----------------- Buttons ----------------- #
def on_enter(e):
    e.widget['background'] = '#4CAF50'

def on_leave(e):
    e.widget['background'] = '#1f7a1f'

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"),
                            bg="#1f7a1f", fg="white", activebackground="#4CAF50", activeforeground="white",
                            bd=0, padx=15, pady=8, cursor="hand2", relief="flat", command=generate_password)
generate_button.pack(pady=10)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Result Entry
result_entry = tk.Entry(root, width=40, font=("Arial", 12), state="readonly", justify="center", relief="solid", bd=2)
result_entry.pack(pady=10, padx=20)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"),
                        bg="#d32f2f", fg="white", activebackground="#f44336", activeforeground="white",
                        bd=0, padx=15, pady=8, cursor="hand2", relief="flat", command=copy_to_clipboard)
copy_button.pack(pady=5)
copy_button.bind("<Enter>", lambda e: e.widget.config(bg="#f44336"))
copy_button.bind("<Leave>", lambda e: e.widget.config(bg="#d32f2f"))

root.mainloop()
