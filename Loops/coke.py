
def main():
    print(machine())

def machine():
    due = 50

    while due > 0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if coin not in [25, 10, 5]:
            print("Machine only allows 25, 10 and 5 cents")
            continue
        else:
            due -= coin

    if due < 0:
        return f"Change Owed: {-due}"
    else:
        return "Change Owed: 0"

if __name__ == "__main__":
    main()