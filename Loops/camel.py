camel = input("camelCase: ")
snake = ""

first = True
for character in camel:
    if character.isupper():
        if not first:  
            snake += "_"
        snake += character.lower()
    else:
        snake += character
    first = False
print(f"snake_case: {snake}")