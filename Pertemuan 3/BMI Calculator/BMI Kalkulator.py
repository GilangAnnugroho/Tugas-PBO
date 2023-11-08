import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = float(age_entry.get())

    unit = unit_var.get()
    if unit == "Metric":
        bmi = weight / ((height / 100) ** 2)
    else:
        bmi = (weight / (height ** 2)) * 703

    if age <= 20:
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal Weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
    else:
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal Weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    result_label.config(text=f"BMI: {bmi:.2f} ({category})")

    # Update the BMI graph
    update_bmi_graph(bmi)

def update_bmi_graph(bmi):
    age = float(age_entry.get())

    if age <= 20:
        categories = ["Underweight", "Normal Weight", "Overweight", "Obese"]
        bmi_values = [18.5, 24.9, 29.9, 100]
    else:
        categories = ["Underweight", "Normal Weight", "Overweight", "Obese"]
        bmi_values = [18.5, 24.9, 29.9, 100]

    plt.clf()
    plt.bar(categories, bmi_values, color=['lightblue', 'lightgreen', 'orange', 'red'])
    plt.ylim(0, 40)
    plt.title("BMI Categories")
    plt.xlabel("Category")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.axhline(y=bmi, color='r', linestyle='--', label="Your BMI")
    plt.legend()

    canvas.draw()

def update_height_entry(event):
    unit = unit_var.get()
    if unit == "Metric":
        height_label.config(text="Height (cm):")
    else:
        height_label.config(text="Height (inch):")

app = tk.Tk()
app.title("BMI Calculator")

# Create and configure the unit dropdown
unit_label = ttk.Label(app, text="Unit:")
unit_label.grid(row=0, column=0, padx=10, pady=10)
unit_var = tk.StringVar()
unit_dropdown = ttk.Combobox(app, textvariable=unit_var, values=["Metric", "US"])
unit_dropdown.grid(row=0, column=1, padx=10, pady=10)
unit_dropdown.set("Metric")
unit_dropdown.bind("<<ComboboxSelected>>", update_height_entry)

# Create and configure weight entry
weight_label = ttk.Label(app, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry = ttk.Entry(app)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and configure height entry
height_label = ttk.Label(app, text="Height (cm):")
height_label.grid(row=2, column=0, padx=10, pady=10)
height_entry = ttk.Entry(app)
height_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and configure age entry
age_label = ttk.Label(app, text="Age:")
age_label.grid(row=3, column=0, padx=10, pady=10)
age_entry = ttk.Entry(app)
age_entry.grid(row=3, column=1, padx=10, pady=10)

# Create and configure the calculate button
calculate_button = ttk.Button(app, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Create and configure the result label
result_label = ttk.Label(app, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create the BMI graph
figure = plt.figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()