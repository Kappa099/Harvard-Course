def to_percent(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0 or x > y:
            raise ValueError

        return round((x / y) * 100)

    except (ValueError, ZeroDivisionError):
        raise

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

        except Exception:
            print("Invalid input. Please enter a valid fraction like '3/4', where X and Y are integers, X ≤ Y, and Y ≠ 0.")

if __name__ == "__main__":
    main()
