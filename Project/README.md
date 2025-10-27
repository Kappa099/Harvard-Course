# Hangman Game

#### Video Demo: (https://youtu.be/VWbF6OkFp2M)

### Description

This is my final project for CS50P. I decided to build a version of Hangman because it’s a simple game that almost everyone knows, but it gave me room to combine different parts of Python into one project. Instead of keeping it text‑only, I used the `turtle` module to draw the gallows and the hangman figure as the game progresses. That way, each wrong guess doesn’t just reduce a counter — you actually see the figure being drawn step by step.

At the start of the game, the player chooses a difficulty: **easy**, **hard**, or **expert**. Each difficulty has its own word list (`words_easy.txt`, `words_hard.txt`, `words_expert.txt`). A random word is picked from the chosen list, and the player guesses letters one at a time. Correct guesses reveal letters in the word, while wrong guesses cost a life and add another piece to the hangman drawing. The game ends when the word is guessed or the player runs out of lives. After each round, the player can choose to play again.

---

### Files

- **project.py**
  Main game file. Includes:
  - `main()` – runs the game loop
  - `choose_difficulty()` – loads the right word list
  - `encrypt()` – hides the word as underscores
  - `guesser()` – checks guesses and updates lives
  - Drawing functions (`setup_turtle`, `draw_gallows`, `draw_hangman`, `show_message`)

- **test_project.py**
  Contains `pytest` tests for the core logic:
  - Tests for `encrypt()` - verifies hidden word initialization
  - Tests for `guesser()` - validates correct guesses, incorrect guesses, and repeated letters
  - Tests for `correct_answer()` - ensures random word selection works
  - Tests for `load_words()` - verifies word file loading
  - Uses `monkeypatch` to mock `draw_hangman()` and prevent turtle graphics from interfering with tests

- **words_easy.txt**, **words_hard.txt**, **words_expert.txt**
  Word lists for each difficulty.

- **requirements.txt**
  Only includes `pytest`.

---

### Design

I wanted the game to be structured in a way that separates logic from graphics. The drawing functions handle visuals, while functions like `encrypt`, `guesser`, and `load_words` return values that can be tested. This made it possible to write automated tests without needing to simulate the whole game loop.

The difficulty system was added to make the game more replayable. Easy mode has shorter and simpler words, while expert mode includes longer or trickier words. This gives players a reason to come back and try again at a higher level.

I also tried to keep the code modular. Each function does one thing: loading words, checking guesses, or drawing a specific part of the hangman. That made it easier to debug and also easier to test.

---

### Challenges and Lessons Learned

One challenge was handling repeated letters correctly. For example, in the word *letter*, guessing “t” should reveal both positions at once. I had to make sure the loop that checks guesses updated every matching index, not just the first one.

Another challenge was balancing interactivity with testability. Games are usually hard to test because they rely on user input, but by splitting the logic into small functions, I could test the important parts in isolation. For example, `guesser()` can be tested with a fake word and hidden list without running the whole game.

I also learned to keep `requirements.txt` minimal. At first I included too many packages, but in the end the only extra tool needed was `pytest`.

---

### How to Run

Clone the repo and run the game:

```bash
git clone https://github.com/Kappa099/Harvard-Course.git
cd Project
python project.py
