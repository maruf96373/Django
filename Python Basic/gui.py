import tkinter as tk
from tkinter import ttk

def convert_temperature():
    """Convert temperature based on the selected option."""
    try:
        temp = float(entry_temperature.get())
        if conversion_option.get() == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            label_result.config(text=f"{result:.2f} °F")
        elif conversion_option.get() == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            label_result.config(text=f"{result:.2f} °C")
        else:
            label_result.config(text="Please select a conversion type.")
    except ValueError:
        label_result.config(text="Invalid input! Enter a numeric value.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.resizable(False, False)

# Input field for temperature
label_temperature = ttk.Label(root, text="Enter Temperature:")
label_temperature.pack(pady=5)
entry_temperature = ttk.Entry(root, width=15)
entry_temperature.pack(pady=5)

# Dropdown menu for conversion options
conversion_option = tk.StringVar(value="Celsius to Fahrenheit")
conversion_menu = ttk.Combobox(
    root, textvariable=conversion_option, state="readonly", width=25
)
conversion_menu['values'] = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
conversion_menu.pack(pady=5)

# Convert button
button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Label to display the result
label_result = ttk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
