def main():
    while True:
        fraction = input("Fraction: ")

        try:
            percent = to_percent(fraction)

            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
            break

        except (ValueError, ZeroDivisionError):
            continue

def to_percent(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0 or x > y:
        raise ValueError

    return round((x / y) * 100)

if __name__ == "__main__":
    main()
