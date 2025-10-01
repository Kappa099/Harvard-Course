def main():
    camel = input("camelCase: ")
    print(snake_case(camel))


def snake_case(word):
    snake = ""
    first = True
    for character in word:
        if character.isupper():
            if not first:  
                snake += "_"
            snake += character.lower()
        else:
            snake += character
        first = False
    return snake

if __name__ == "__main__":
    main()