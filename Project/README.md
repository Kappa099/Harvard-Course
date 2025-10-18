# Hangman Game

#### Video Demo: <URL HERE>
#### Description:

This project is my final submission for Harvard’s CS50P course. It is a Python implementation of the classic Hangman game, enhanced with Turtle graphics for visual feedback. The program randomly selects a word from a predefined list, and the player attempts to guess the word one letter at a time. Each incorrect guess reduces the number of lives and draws another part of the hangman figure. The game ends when the player either guesses the word correctly or runs out of lives.

The project demonstrates my ability to combine Python’s standard library modules (`random` and `turtle`) with structured program design and automated testing using `pytest`. It goes beyond a simple console game by integrating graphics, modular functions, and a test suite to ensure correctness.

---

### Overview

The game begins by selecting a random word from a predefined list. The word is displayed as underscores, and the player guesses one letter at a time. Correct guesses reveal letters in their positions, while incorrect guesses reduce the number of lives and trigger Turtle graphics to draw parts of the hangman. The player wins if they reveal the entire word before running out of lives, and loses otherwise. After each round, the player is prompted to play again.

---

### Project Structure

- **`project.py`**  
  Contains the main game logic and all supporting functions.  
  - `main()` — orchestrates the game loop, handles user input, and manages win/lose conditions.  
  - `setup_turtle()` — initializes the Turtle graphics window and prepares the gallows.  
  - `draw_gallows()` — draws the base structure of the gallows.  
  - `draw_hangman(lives_left)` — draws the hangman figure step by step as lives decrease.  
  - `show_message(text, color)` — displays win/lose messages on the screen.  
  - `correct_answer()` — randomly selects a word from a predefined list.  
  - `encrypt(word)` — converts the chosen word into a hidden list of underscores.  
  - `guesser(char, chosen, hidden, lives)` — updates the hidden word if the guess is correct, or decreases lives if incorrect.  
  - `play_again()` — prompts the user to play another round.

- **`test_project.py`**  
  Contains automated tests written with `pytest`. These tests verify the correctness of the core logic functions:
  - `test_encrypt_*` — ensures words are properly hidden as underscores.  
  - `test_guesser_*` — checks correct guesses, incorrect guesses, and repeated letters.  
  - `test_correct_answer()` — ensures the chosen word is always from the allowed list (using `monkeypatch` for determinism).

- **`requirements.txt`**  
  Lists external dependencies. For this project, only `pytest` is required, since all other modules come from Python’s standard library.

---

### Design Choices

I chose to use Turtle graphics to make the game more engaging and visually appealing. While a text‑only version of Hangman would have been simpler, adding graphics demonstrates my ability to integrate multiple parts of Python’s ecosystem. The game logic is separated into small, testable functions, which makes the code easier to maintain and extend.

For testing, I focused on the functions that return values (`encrypt`, `guesser`, `correct_answer`). Functions that only draw graphics (`draw_gallows`, `draw_hangman`, `show_message`) are not unit‑tested, since they do not return values and are primarily visual. This separation of logic and graphics was an intentional design decision.

---

### Challenges and Lessons Learned

One challenge was ensuring that repeated letters in a word (such as the two “t”s in “letter”) were revealed correctly when guessed. Another was balancing the interactive nature of the game with the need for automated testing. By isolating the logic into pure functions, I was able to write meaningful tests without needing to simulate the entire game loop.

I also learned the importance of keeping `requirements.txt` minimal. At first, I generated a full environment freeze, which included many unrelated packages. I refined it to include only `pytest`, which is all that is needed to run the tests.

---

### Future Improvements

If I were to extend this project, I would consider:
- Adding difficulty levels with different word lists.  
- Implementing a scoring system that tracks wins and losses across sessions.  
- Allowing players to provide their own custom word lists.  
- Saving results to a file or database for persistence.  

---

### How to Run

```bash
python project.py