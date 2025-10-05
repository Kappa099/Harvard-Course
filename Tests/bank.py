def main():
    s = input("Greeting: ")
    print(value(s))


def value(greeting):
    greeting_lower = greeting.lower()
    if greeting_lower.startswith("hello"):
        return 0
    if greeting_lower.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()