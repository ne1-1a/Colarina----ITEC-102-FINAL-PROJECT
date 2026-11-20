# Example 7 (Hard) MINI PROJECT 2: Number toolkit - one small function per tool


def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def digit_sum(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total


def reverse_number(n):
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n


def is_palindrome(n):
    return n == reverse_number(n)


def main():
    while True:
        print("\n=== NUMBER TOOLKIT ===")
        print("1. Even or odd")
        print("2. Prime?")
        print("3. Factorial")
        print("4. Sum of digits")
        print("5. Palindrome?")
        print("6. Reverse")
        print("7. Exit")
        choice = input("Choose (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 6:
            print("Please choose 1 to 7.")
            continue

        n = int(input("Enter a whole number (0 or more): "))
        if n < 0:
            print("Negative numbers are not supported here.")
        elif choice == "1":
            print(n, "is", "even" if is_even(n) else "odd")
        elif choice == "2":
            print(n, "is prime" if is_prime(n) else "is NOT prime")
        elif choice == "3":
            if n > 20:
                print("Please use 20 or less.")
            else:
                print(f"{n}! = {factorial(n):,}")
        elif choice == "4":
            print("Sum of digits:", digit_sum(n))
        elif choice == "5":
            print(n, "is a palindrome" if is_palindrome(n) else "is NOT a palindrome")
        elif choice == "6":
            print("Reversed:", reverse_number(n))


main()
