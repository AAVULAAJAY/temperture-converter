import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature():
    try:
        input_temperature = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        result = 0

        if from_unit == to_unit:
            result = input_temperature
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(input_temperature)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = fahrenheit_to_celsius(input_temperature)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = celsius_to_kelvin(input_temperature)
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = kelvin_to_celsius(input_temperature)
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = fahrenheit_to_kelvin(input_temperature)
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = kelvin_to_fahrenheit(input_temperature)

        result_label.config(text=f"Result: {result:.2f} {to_unit}")

    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create input field
entry_label = tk.Label(root, text="Enter Temperature:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create "From" unit selection
from_unit_var = tk.StringVar()
from_unit_var.set("Celsius")
from_unit_label = tk.Label(root, text="From:")
from_unit_label.pack()
from_unit_menu = tk.OptionMenu(root, from_unit_var, "Celsius", "Fahrenheit", "Kelvin")
from_unit_menu.pack()

# Create "To" unit selection
to_unit_var = tk.StringVar()
to_unit_var.set("Fahrenheit")
to_unit_label = tk.Label(root, text="To:")
to_unit_label.pack()
to_unit_menu = tk.OptionMenu(root, to_unit_var, "Celsius", "Fahrenheit", "Kelvin")
to_unit_menu.pack()

# Create conversion button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create result label
result_label = tk.Label(root, text="Result:")
result_label.pack()

# Start the GUI main loop
root.mainloop()
