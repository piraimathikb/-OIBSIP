import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Similar characters to exclude
similar_chars = "il1Lo0O"

# Function to calculate strength
def calculate_strength(password):
    length = len(password)
    if length < 8:
        return "Weak"
    elif any(c in string.punctuation for c in password) and any(c.isdigit() for c in password):
        return "Strong"
    return "Moderate"

# Function to generate password
def generate_password():
    length = length_var.get()
    include_letters = letters_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    exclude_similar = exclude_similar_var.get()
    avoid_repeat = avoid_repeat_var.get()

    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if exclude_similar:
        characters = ''.join([c for c in characters if c not in similar_chars])

    if not characters:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    try:
        length = int(length)
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")
        return

    if avoid_repeat and length > len(characters):
        messagebox.showerror("Error", "Length too long for unique characters selected.")
        return

    password = ''.join(random.sample(characters, length)) if avoid_repeat else ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
    strength_var.set(f"Strength: {calculate_strength(password)}")

# Copy to clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# Clear password field
def clear_fields():
    password_var.set("")
    strength_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("420x450")
root.resizable(False, False)

# Variables
length_var = tk.IntVar(value=12)
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
exclude_similar_var = tk.BooleanVar()
avoid_repeat_var = tk.BooleanVar()
password_var = tk.StringVar()
strength_var = tk.StringVar()

# UI Layout
tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var).pack()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)

tk.Checkbutton(root, text="Avoid Similar Characters (e.g. 0, O, l)", variable=exclude_similar_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Avoid Repeating Characters", variable=avoid_repeat_var).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

tk.Entry(root, textvariable=password_var, width=34, font=("Courier", 12)).pack(pady=5)

tk.Label(root, textvariable=strength_var, fg="blue").pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields, bg="gray", fg="white").pack(pady=5)


root.mainloop()
