import tkinter as tk
from tkinter import ttk,Tk
from bmiCalc import calculate_bmi
import customtkinter as ct

def bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    
    # Check if weight and height are within human range
    if weight <= 0 or weight > 200:
        result_label.configure(text="Invalid weight")
        return
    if height <= 0 or height > 3:
        result_label.configure(text="Invalid height")
        return
    
    # bmi = weight / (height ** 2)
    bmi,category = calculate_bmi(weight, height)
    result_label.configure(text=f"Your BMI: {bmi:.2f}\n You are: {category}")


# Create the main window
window = ct.CTk()
window.title("BMI Calculator")

# Set the height and width of the window
window.geometry("400x300")

weight_label = ct.CTkLabel(window, text="Weight (kg):",font=("Helvetica", 16))
weight_label.place(relx=0.5, rely=0.3, anchor="center")

weight_entry = ct.CTkEntry(window,placeholder_text="Enter your weight",corner_radius=10,font=("Helvetica", 16))
weight_entry.place(relx=0.5, rely=0.4, anchor="center")

height_label = ct.CTkLabel(window, text="Height (m):",font=("Helvetica", 16))
height_label.place(relx=0.5, rely=0.5, anchor="center")

height_entry = ct.CTkEntry(window,placeholder_text="Enter your height",corner_radius=10,font=("Helvetica", 16))
height_entry.place(relx=0.5, rely=0.6, anchor="center")

calculate_button = ct.CTkButton(window,text="Calculate",corner_radius=10,font=("Helvetica", 16),command=bmi)
calculate_button.place(relx=0.5, rely=0.7, anchor="center")

result_label = ct.CTkLabel(window, text="",font=("Helvetica", 16))
result_label.place(relx=0.5, rely=0.85, anchor="center")
# Start the main loop
window.mainloop()
