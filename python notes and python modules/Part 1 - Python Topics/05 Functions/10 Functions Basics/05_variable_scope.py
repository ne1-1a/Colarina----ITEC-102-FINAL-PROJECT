# Example 5 (Intermediate): Scope - where a variable can be seen

message = "I am GLOBAL (defined outside any function)"


def show_message():
    print(message)                 # a function CAN read a global variable


show_message()


def local_example():
    secret = "I am LOCAL (only exists inside this function)"
    print(secret)


local_example()
# print(secret)                    # NameError: secret does not exist out here


def shadow_example():
    message = "I am a NEW local variable with the same name"
    print(message)


shadow_example()
print("Global message is unchanged:", message)


# Parameters are local too: changing them does not change the caller's variable
def double(n):
    n = n * 2
    return n


number = 5
print("double(number) =", double(number), "| number is still", number)

# Changing a global from inside a function needs the global keyword ...
counter = 0


def bad_increment():
    global counter
    counter += 1


bad_increment()
print("counter after bad_increment():", counter)


# ... but a BETTER habit is: pass values in, return values out
def good_increment(value):
    return value + 1


counter = good_increment(counter)
print("counter after good_increment():", counter)
