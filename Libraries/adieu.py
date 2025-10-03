import inflect

def main():
    p = inflect.engine()
    names = []

    print("Enter names, one per line (Ctrl+Z+Enter to end):")
    try:
        while True:
            name = input()
            if name.strip():
                names.append(name.strip())
    except EOFError:
        pass  

    joined_names = p.join(names)

    print(f"Adieu, adieu, to {joined_names}")

if __name__ == "__main__":
    main()
