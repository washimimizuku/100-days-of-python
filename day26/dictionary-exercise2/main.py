weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def celsius_to_fahrenheit(temperature_celsius):
    return (temperature_celsius * 9 / 5) + 32

weather_f = {day: celsius_to_fahrenheit(temperature) for (day, temperature) in weather_c.items()}

print(weather_f)
