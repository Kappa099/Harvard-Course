expr = input("Expression: ").strip()

if "+" in expr:
    expr = expr.replace("+", " + ")
elif "-" in expr:
    expr = expr.replace("-", " - ")
elif "*" in expr:
    expr = expr.replace("*", " * ")
elif "/" in expr:
    expr = expr.replace("/", " / ")

x, operator, z = expr.split()

x = int(x)
z = int(z)

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z

print(f"{result:.1f}")