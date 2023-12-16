import tkinter as tk
import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    
    # Check if weight and height are within human range
    if weight <= 0 or weight > 200:
        result_label.config(text="Invalid weight")
        return
    if height <= 0 or height > 3:
        result_label.config(text="Invalid height")
        return
    
    bmi = weight / (height ** 2)
    result_label.config(text=f"Your BMI: {bmi:.2f}")


# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Set the height and width of the window
window.geometry("400x300")

# Create labels and entries for weight and height
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.place(relx=0.5, rely=0.4, anchor="center")
weight_entry = tk.Entry(window, justify="center")
weight_entry.place(relx=0.5, rely=0.5, anchor="center")

height_label = tk.Label(window, text="Height (m):")
height_label.pack(anchor="center")
height_entry = tk.Entry(window, justify="center")
height_entry.pack(anchor="center")

# Create a button to calculate BMI
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(anchor="center")

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack(anchor="center")

# Start the main loop
window.mainloop()
