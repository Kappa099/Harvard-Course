def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    try:
        x_str, y_str = fraction.split("/")
    except ValueError:
        raise ValueError

    try:
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    percent = round((x / y) * 100)
    if percent < 0:
        percent = 0
    if percent > 100:
        percent = 100
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()