# Example 4 (Intermediate): Why `case _` matters


def traffic_light(color):
    print(f"Light is {color}:", end=" ")
    match color:
        case "red":
            print("STOP")
        case "yellow":
            print("SLOW DOWN")
        case "green":
            print("GO")
        case _:
            print("Broken light! Treat it like a stop sign.")


traffic_light("red")
traffic_light("green")
traffic_light("blue")          # caught by case _


# Without case _ , an unmatched value is silently ignored (no error, no output)
def silent(color):
    match color:
        case "red":
            print("STOP")


print("Calling silent('blue') prints nothing:")
silent("blue")
print("(nothing printed above, which can hide bugs)")
