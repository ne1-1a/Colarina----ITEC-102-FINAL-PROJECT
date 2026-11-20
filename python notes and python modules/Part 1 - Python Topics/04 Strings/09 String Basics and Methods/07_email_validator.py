# Example 7 (Hard) MINI PROJECT 2: Email validator that explains WHAT is wrong
email = input("Enter an email address: ").strip()
problems = 0

if email == "":
    print("- The email is empty")
    problems += 1
else:
    if " " in email:
        print("- It must not contain spaces")
        problems += 1

    if ".." in email:
        print("- It must not contain two dots in a row")
        problems += 1

    if email.count("@") != 1:
        print("- It must contain exactly one @")
        problems += 1
    else:
        at = email.find("@")
        local_part = email[:at]                 # before the @
        domain = email[at + 1:]                 # after the @

        if local_part == "":
            print("- There must be something before the @")
            problems += 1

        if "." not in domain:
            print("- The domain needs a dot (like example.com)")
            problems += 1
        elif domain.startswith(".") or domain.endswith("."):
            print("- The domain must not start or end with a dot")
            problems += 1
        else:
            extension = domain[domain.rfind(".") + 1:]      # text after the LAST dot
            if len(extension) < 2 or not extension.isalpha():
                print("- The ending (like .com) needs 2 or more letters")
                problems += 1

print()
if problems == 0:
    print("VALID email:", email)
else:
    print(f"INVALID email ({problems} problem(s) found)")
