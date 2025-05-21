
fahrenheit_values = [32, 70, 80, 72, 68, 75, 82, 65, 77, 78, 73, 79, 71, 74, 76]
celsius_values = [25, 18, 15, 28, 20, 23, 30, 22, 26, 24, 21, 27, 19, 17, 29]
tot_temperature_in_fahrenheit = sum(fahrenheit_values)
tot_temperature_in_celsius = sum(celsius_values)
avg_temperature_in_fahrenheit = tot_temperature_in_fahrenheit / len(fahrenheit_values)
avg_temperature_in_celsius = tot_temperature_in_celsius / len(celsius_values)
print(f"Total Temperature in Fahrenheit: {tot_temperature_in_fahrenheit}°F")
print(f"Total Temperature in Celsius: {tot_temperature_in_celsius}°C")
print(f"Average Temperature in Fahrenheit: {avg_temperature_in_fahrenheit:.2f}°F")
print(f"Average Temperature in Celsius: {avg_temperature_in_celsius:.2f}°C")
