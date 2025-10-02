def get_menu():
    return {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

def process(item, menu):
    item = item.strip().title()
    return menu.get(item, None)

def order():
    foods = get_menu()
    total = 0.0

    try:
        while True:
            item_input = input("Item: ")
            price = process(item_input, foods)
            if price is not None:
                total += price
                print(f"Total: ${total:.2f}")
    except EOFError:
        print() 

    print(f"Final total: ${total:.2f}")

if __name__ == "__main__":
    order()