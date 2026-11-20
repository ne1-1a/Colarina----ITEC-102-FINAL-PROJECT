# Example 6 (Intermediate-Hard) MINI PROJECT 1: Temperature converter with a menu


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    return c + 273.15


def show_menu():
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        if choice == "1":
            c = float(input("Celsius: "))
            print(f"{c} C = {celsius_to_fahrenheit(c):.2f} F")
        elif choice == "2":
            f = float(input("Fahrenheit: "))
            print(f"{f} F = {fahrenheit_to_celsius(f):.2f} C")
        elif choice == "3":
            c = float(input("Celsius: "))
            print(f"{c} C = {celsius_to_kelvin(c):.2f} K")
        else:
            print("Please choose 1 to 4.")


main()
