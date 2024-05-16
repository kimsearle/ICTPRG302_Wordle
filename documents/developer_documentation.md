# Developer Documentation
### Overview
The Guess-My-Word game is implemented in Python 3.1x and adheres to PEP8 standards. It is a command-line game where players guess a 5-letter word within 6 attempts. The game provides feedback on the accuracy of each guess, guiding the player towards the correct word.

### Constants
MISS = 0: Letter not in word(⬜)  
MISPLACED = 1: Letter in wrong place (🟨)  
EXACT = 2: Right letter, right place (🟩)  
MAX_ATTEMPTS = 6: Maximum number of attempts allowed.  
WORD_LENGTH = 5: Length of the word to be guessed.  
ALL_WORDS = 'file/path/of/words.txt': Path to the file containing all valid words.  
TARGET_WORDS = 'file/path/of/target_words.txt': Path to the file containing target words.   
  
### Functions

```play()```

Controls the game loop.
Selects the word of the day using get_target_word().
Fetches the list of valid words using get_valid_words().
Repeats asking for guesses and scoring them until the game ends.

```is_correct(score)```

Checks if the score indicates the word has been guessed correctly.
Returns True if all letters are EXACT.

```get_valid_words(file_path=ALL_WORDS)```

Reads and returns a list of valid words from the specified file.

```get_target_word(file_path=TARGET_WORDS, seed=None)```

Picks and returns a random target word from the specified file.

```ask_for_guess(valid_words)```

Prompts the user for a guess.
Ensures the guess is valid and of correct length.

```score_guess(guess, target_word)```

Scores the guess against the target word.
Returns a tuple representing the score for each letter.

```help()```

Provides help and instructions for the game.

```format_score(guess, score)```

Formats and displays the guess and its corresponding score.

```main(test=False)```

Entry point of the game.
Runs doctests if test is True.
Initiates the game by calling play().

### Testing
Doctests are included in the function docstrings to validate their behavior.
Run the script with test=True to execute the doctests:
```bash 
./guess_my_word.py
```
Example Doctest
```python 
>>> score_guess('hello', 'hello')
(2, 2, 2, 2, 2)
>>> score_guess('drain', 'float')
(0, 0, 1, 0, 0)
>>> score_guess('gauge', 'range')
(0, 2, 0, 2, 2)
```


