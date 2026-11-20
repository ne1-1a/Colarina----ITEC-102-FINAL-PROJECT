# Example 8 (Hard) MINI PROJECT 3: Text adventure - match inside match inside a loop
location = "village"
print("=== THE LOST TREASURE ===")

while True:
    match location:
        case "village":
            print("\nYou are in a quiet village. Paths lead NORTH (forest) and EAST (river).")
            choice = input("Where to? (north / east / quit): ").strip().lower()
            match choice:
                case "north":
                    location = "forest"
                case "east":
                    location = "river"
                case "quit":
                    print("You went home. The end.")
                    break
                case _:
                    print("You cannot go that way.")

        case "forest":
            print("\nThe forest is dark. A cave entrance is NORTH. The village is SOUTH.")
            choice = input("Where to? (north / south): ").strip().lower()
            match choice:
                case "north":
                    location = "cave"
                case "south":
                    location = "village"
                case _:
                    print("You walk in circles.")

        case "river":
            print("\nA wide river blocks the way. You can go WEST (village) or SWIM.")
            choice = input("What now? (west / swim): ").strip().lower()
            match choice:
                case "west":
                    location = "village"
                case "swim":
                    print("The current is too strong. You are swept away. GAME OVER.")
                    break
                case _:
                    print("You stare at the water.")

        case "cave":
            print("\nA chest glows in the cave. You can TAKE it or LEAVE.")
            choice = input("What now? (take / leave): ").strip().lower()
            match choice:
                case "take":
                    print("You found the lost treasure! YOU WIN!")
                    break
                case "leave":
                    location = "forest"
                case _:
                    print("The chest waits.")
