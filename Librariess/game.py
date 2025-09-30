import random

def get_positive_integer(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)

def main():
    level = get_positive_integer("Level: ")
    target = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
