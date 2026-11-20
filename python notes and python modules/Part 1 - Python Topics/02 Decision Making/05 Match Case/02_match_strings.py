# Example 2 (Easy): match / case with text
command = input("Type a command (start / stop / pause): ").strip().lower()

match command:
    case "start":
        print("Engine started.")
    case "stop":
        print("Engine stopped.")
    case "pause":
        print("Engine paused.")
    case _:
        print(f"Unknown command: {command}")
