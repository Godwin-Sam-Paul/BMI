from bmiCalc import calculate_bmi
import customtkinter as ct
from db import insert_measurement
from plot import plot_bmi
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def bmi(weight,height):
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    
    # Check if weight and height are within human range
    if weight <= 0 or weight > 200:
        result_label.configure(text="Invalid weight",text_color="red")
        return
    if height <= 0 or height > 3:
        result_label.configure(text="Invalid height",text_color="red")
        return
    
    # bmi = weight / (height ** 2)
    bmi,category = calculate_bmi(weight, height)
    plotBMI()
    # insert_measurement(weight, height,bmi)
    result_label.configure(text=f"Your BMI: {bmi:.2f}\n You are: {category}")

def plotBMI():
    fig = plot_bmi()
    fig.patch.set_alpha(0)  # Set the figure background to transparent
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.get_tk_widget().configure(background="#212121")  # Set the canvas background to transparent
    canvas.get_tk_widget().pack(fill="both", expand=True)

def units():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    metric=unit_metric.get()

    bmi(weight, height)
    
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")
# Create the main window
window = ct.CTk()

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0 ,weight=0)
window.grid_columnconfigure(1 ,weight=1)
window.title("BMI Calculator")

# Set the height and width of the window
window.geometry("1200x700")

frame = ct.CTkFrame(window,width=500,height=500)
frame.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure((0,1,2), weight=1)

bmiframe= ct.CTkFrame(frame,fg_color="transparent")
bmiframe.grid(row=0, column=1, padx=10, pady=10,sticky="ew")

weight_unit_label = ct.CTkLabel(bmiframe, text="Units:", font=("Helvetica", 16))
weight_unit_label.pack(padx=30, pady=2, anchor="center",fill="x")

unit_metric = ct.CTkComboBox(bmiframe,values=["kg,m","lb,cm","kg,cm"] , font=("Helvetica", 16))
unit_metric.pack(padx=30,pady=2, anchor="center",fill="x")

weight_label = ct.CTkLabel(bmiframe, text="Weight (kg):",font=("Helvetica", 16))
weight_label.pack(padx=30, pady=5, anchor="center",fill="x")

weight_entry = ct.CTkEntry(bmiframe,placeholder_text="Enter your weight",corner_radius=10,font=("Helvetica", 16))
weight_entry.pack(padx=30, pady=5, anchor="center",fill="x")

height_label = ct.CTkLabel(bmiframe, text="Height (m):",font=("Helvetica", 16))
height_label.pack(padx=30, pady=5, anchor="center",fill="x")

height_entry = ct.CTkEntry(bmiframe,placeholder_text="Enter your height",corner_radius=10,font=("Helvetica", 16))
height_entry.pack(padx=30, pady=5, anchor="center",fill="x")

calculate_button = ct.CTkButton(bmiframe,text="Calculate",corner_radius=10,font=("Helvetica", 16),command=units)
calculate_button.pack(padx=30, pady=5, anchor="center",fill="x")

result_label = ct.CTkLabel(bmiframe, text="",font=("Helvetica", 16))
result_label.pack(padx=30, pady=5, anchor="center",fill="x")

frame2 = ct.CTkFrame(window,fg_color="#212121")
frame2.grid(row=0, column=1, padx=10, pady=10,sticky="nsew")

# Start the main loop
window.mainloop()
