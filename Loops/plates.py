def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    i = 0
    number_started = False

    while i < len(s):
        if s[i].isdigit():
            if not number_started:
                if s[i] == '0':
                    return False  
                number_started = True
        elif number_started:
            return False  
        i += 1

    return True

main()