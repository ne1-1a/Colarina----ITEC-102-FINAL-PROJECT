# Example 6 (Intermediate-Hard) MINI PROJECT 1: Diary app that remembers between runs
import os

FILENAME = "diary.txt"


def add_entry():
    text = input("Write your entry: ").strip()
    if text == "":
        print("Nothing to save.")
        return
    with open(FILENAME, "a", encoding="utf-8") as file:     # append = never lose old entries
        file.write(text + "\n")
    print("Entry saved!")


def read_entries():
    if not os.path.exists(FILENAME):
        print("No entries yet. Write one first!")
        return
    number = 0
    with open(FILENAME, encoding="utf-8") as file:
        for line in file:                                    # streaming
            number += 1
            print(f"{number}. {line.strip()}")
    if number == 0:
        print("The diary is empty.")


def search_entries():
    if not os.path.exists(FILENAME):
        print("No entries yet.")
        return
    word = input("Search for: ").strip().lower()
    found = 0
    with open(FILENAME, encoding="utf-8") as file:
        for line in file:
            if word in line.lower():
                found += 1
                print(" -", line.strip())
    print(f"{found} entr{'y' if found == 1 else 'ies'} found.")


def main():
    while True:
        print("\n=== MY DIARY ===")
        print("1. Add entry")
        print("2. Read all entries")
        print("3. Search entries")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1 to 4.")


main()
