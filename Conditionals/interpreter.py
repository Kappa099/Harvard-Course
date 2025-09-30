x = input("Enter the first number: ")
y = input("Enter an operator (+, -, *, /): ")
z = input("Enter the second number: ")

if not x.isdigit() or not z.isdigit():
    print("Error: Both values must be numbers.")
else:
    x = int(x)
    z = int(z)

    if y == "+":
        print(f"Result: {x + z}")
    elif y == "-":
        print(f"Result: {x - z}")
    elif y == "*":
        print(f"Result: {x * z}")
    elif y == "/":
        if z == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {x / z}")
    else:
        print("Error: Invalid operator. Use +, -, *, or /.")
