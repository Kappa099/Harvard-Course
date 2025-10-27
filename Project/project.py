import random
import turtle

# turtle model
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

# turtle model
def setup_turtle():
    turtle.bgcolor("white")
    drawer.clear()
    drawer.pensize(5)
    draw_gallows()

# turtle model
def draw_gallows():
    # Base
    drawer.penup()
    drawer.goto(-100, -150)
    drawer.setheading(0)
    drawer.pendown()
    drawer.forward(200)

    # Pole
    drawer.penup()
    drawer.goto(-50, -150)
    drawer.setheading(90)
    drawer.pendown()
    drawer.forward(250)

    # Top bar
    drawer.right(90)
    drawer.forward(100)

    # Rope
    drawer.right(90)
    drawer.forward(30)

# turtle model
def draw_hangman(lives_left):
    if lives_left == 5:
        drawer.penup()
        drawer.goto(50, 70)
        drawer.setheading(0)
        drawer.pendown()
        drawer.circle(20)
    elif lives_left == 4:
        drawer.penup()
        drawer.goto(50, 70)
        drawer.setheading(-90)
        drawer.pendown()
        drawer.forward(50)
    elif lives_left == 3:
        drawer.penup()
        drawer.goto(50, 50)
        drawer.setheading(-45)
        drawer.pendown()
        drawer.forward(30)
    elif lives_left == 2:
        drawer.penup()
        drawer.goto(50, 50)
        drawer.setheading(-135)
        drawer.pendown()
        drawer.forward(30)
    elif lives_left == 1:
        drawer.penup()
        drawer.goto(50, 20)
        drawer.setheading(-45)
        drawer.pendown()
        drawer.forward(30)
    elif lives_left == 0:
        drawer.penup()
        drawer.goto(50, 20)
        drawer.setheading(-135)
        drawer.pendown()
        drawer.forward(30)

# turtle model
def show_message(text, color):
    drawer.penup()
    drawer.goto(0, 120)
    drawer.color(color)
    drawer.write(text, align="center", font=("Arial", 50, "bold"))
    drawer.color("black")

def load_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def choose_difficulty():
    while True:
        choice = input("Choose difficulty (easy, hard, expert): ").lower()
        if choice == "easy":
            return load_words("words_easy.txt")
        elif choice == "hard":
            return load_words("words_hard.txt")
        elif choice == "expert":
            return load_words("words_expert.txt")
        else:
            print("Invalid choice. Please type easy, hard, or expert.")

def correct_answer(word_list):
    return random.choice(word_list)

def encrypt(word):
    hidden = ["_"] * len(word)
    print(f"Your guessing word is: {hidden}")
    return hidden

def guesser(char, chosen, hidden, lives):
    found = False
    for i in range(len(chosen)):
        if char == chosen[i]:
            hidden[i] = char
            found = True
    if found:
        print(f"{char} is in the word! {hidden}")
    else:
        lives -= 1
        draw_hangman(lives)  # turtle model
        print(f"{char} is not in the word! You have {lives} lives left.")
    return lives

def play_again():
    again = input("Play again? (y/n): ").lower()
    return again == "y"

def main():
    while True:
        setup_turtle()

        word_list = choose_difficulty()
        phrase = correct_answer(word_list)
        hidden = encrypt(phrase)
        lives = 6
        guessed_letters = []


        while lives > 0 and "_" in hidden:
            game = input("Please enter a letter: ").lower()

            if not game.isalpha() or len(game) != 1:
                print("Invalid input. Enter a single letter (a-z).")
                continue

            if game in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(game)
            lives = guesser(game, phrase, hidden, lives)

            if "_" not in hidden:
                print("You won!")
                show_message("You won!", "green")  # turtle model
                break

            if lives == 0:
                print(f"Game Over! The word was: '{phrase}'.")
                show_message("You lost! Try again!", "red")
                break

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

