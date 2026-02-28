# Defining global variables/constants for conversion factors.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Defining functions for temperature conversion.

def  convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:

    temperature = input("Enter the temperature to convert: ")

    try:
        temperature = float(temperature)
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.\n")

# Using a loop to ensure accurate input.

while True:
    
    conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if conversion_type == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}\u00B0C is {fahrenheit}\u00B0F")
        break
    elif conversion_type =='F':
        celsius = convert_to_celsius(temperature)
        print(F"{temperature}\u00B0F is {celsius}\u00B0C")
        break
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.\n")



