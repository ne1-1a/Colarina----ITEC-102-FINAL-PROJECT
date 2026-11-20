# Example 4 (Intermediate): Small functions working together
PI = 3.14159


def area_circle(radius):
    return PI * radius ** 2


def circumference_circle(radius):
    return 2 * PI * radius


def describe_circle(radius):
    area = area_circle(radius)                 # one function uses another
    circumference = circumference_circle(radius)
    print(f"Radius {radius}: area = {area:.2f}, circumference = {circumference:.2f}")


describe_circle(5)
describe_circle(10)


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def describe_weather(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    if celsius >= 32:
        mood = "hot"
    elif celsius >= 24:
        mood = "warm"
    else:
        mood = "cool"
    print(f"{celsius} C = {fahrenheit:.1f} F ({mood})")


describe_weather(35)
describe_weather(26)
describe_weather(18)


# Break a big problem into small, named steps
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


print("Feb 2024 has", days_in_month(2, 2024), "days")
print("Feb 2026 has", days_in_month(2, 2026), "days")
print("Nov 2026 has", days_in_month(11, 2026), "days")
