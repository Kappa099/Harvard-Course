import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        tries = 0
        while tries < 3:
            try:
                answer = input(f"{x} + {y} = ")
                guess = int(answer)
                if guess == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:

                print("EEE")
                tries += 1

        else:  
            print(f"{x} + {y} = {correct}")

    print(f"Score: {score}/10")

def get_level():
    while True:
        level_str = input("Level: ").strip()
        if level_str in ("1", "2", "3"):
            return int(level_str)

def generate_integer(level):
    if level not in (1, 2, 3):
        raise ValueError("Level must be 1, 2, or 3")
    start = 10**(level - 1) if level > 1 else 0
    end = 10**level - 1
    return random.randint(start, end)

if __name__ == "__main__":
    main()
