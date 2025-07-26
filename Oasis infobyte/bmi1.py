import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

# File to store data
DATA_FILE = "bmi_data.json"

# --- BMI and Advice Functions ---

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "Consider eating a balanced diet and consult a doctor if needed."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Great job! Maintain your healthy lifestyle."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Incorporate regular exercise and watch your diet."
    else:
        return "Obese", "Seek medical guidance to create a healthy weight loss plan."

def save_data(name, age, gender, bmi):
    entry = {
        "name": name,
        "age": age,
        "gender": gender,
        "bmi": bmi,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data = []

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

    data.append(entry)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# --- BMI Trend Chart ---

def show_trend():
    if not os.path.exists(DATA_FILE):
        messagebox.showinfo("No Data", "No historical data available.")
        return

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    # Sort by date
    data = sorted(data, key=lambda x: x['date'])

    labels = [f"{entry['name']} ({entry['date'].split()[0]})" for entry in data]
    bmis = [entry['bmi'] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.plot(labels, bmis, marker='o', color='teal')
    plt.xlabel("Entries")
    plt.ylabel("BMI")
    plt.title("BMI Trend Over Time")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

# --- Main Calculation Handler ---

def calculate_and_show():
    try:
        name = name_entry.get().strip()
        age = int(age_entry.get())
        gender = gender_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            raise ValueError("Name cannot be empty.")
        if age <= 0 or weight <= 0 or height <= 0:
            raise ValueError("Age, weight, and height must be positive.")

        bmi = calculate_bmi(weight, height)
        category, advice = categorize_bmi(bmi)

        result_label.config(text=f"{name}, your BMI is {bmi} ({category})")
        advice_label.config(text=f"Advice: {advice}")
        save_data(name, age, gender, bmi)

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Select")
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    advice_label.config(text="")

def toggle_dark_mode():
    theme = dark_mode_var.get()
    color = "#333" if theme else "white"
    fg_color = "white" if theme else "black"

    root.configure(bg=color)
    for widget in root.winfo_children():
        widget.configure(bg=color, fg=fg_color)

# --- GUI Setup ---

root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("450x500")

# Theme Control
dark_mode_var = tk.BooleanVar()
tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode).pack(anchor='ne', padx=10, pady=5)

# User Inputs
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar(value="Select")
tk.OptionMenu(root, gender_var, "Male", "Female", "Other").pack()

tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Buttons
tk.Button(root, text="Calculate BMI", command=calculate_and_show).pack(pady=10)
tk.Button(root, text="Show BMI Trend", command=show_trend).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_fields).pack(pady=5)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

advice_label = tk.Label(root, text="", font=("Arial", 10), wraplength=400, justify="center")
advice_label.pack(pady=5)

root.mainloop()
