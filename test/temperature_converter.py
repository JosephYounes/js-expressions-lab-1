def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def main():
    # Predefined list of temperatures in Fahrenheit
    fahrenheit_values = [32, 70, 80, 72, 68, 75, 82, 65, 77, 78, 73, 79, 71, 74, 76]
    # Predefined list of temperatures in Celsius
    celsius_values = [25, 18, 15, 28, 20, 23, 30, 22, 26, 24, 21, 27, 19, 17, 29]

    print("Fahrenheit to Celsius conversions:")
    for f in fahrenheit_values:
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c:.2f}°C")

    print("\nCelsius to Fahrenheit conversions:")
    for c in celsius_values:
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f:.2f}°F")

if __name__ == "__main__":
    main()
