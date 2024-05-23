# Developer Documentation
### Overview
The Guess-My-Word game is implemented in Python 3.1x and adheres to PEP8 standards. It is a command-line game where players guess a 5-letter word within 6 attempts. The game provides feedback on the accuracy of each guess, guiding the player towards the correct word.

### Constants

GUESS_COUNT = 6: Maximum number of attempts allowed.
WORD_LENGTH = 5: The length of the target word.

##Global Variables
target_word: The word the player needs to guess.
char_target: List of characters in the target word.
total_guess_count: Counts the number of guesses made by the player.


### Functions

```game_instructions()```
Displays the game instructions to the player.

```help_info()```
Displays help information when the player asks for help.

```guess_prompt()```
Prompts the player for guesses and processes the input. Checks for special commands (exit, help) and validates the guesses.

```score_guess(char_guess)```
Scores the player's guess against the target word. Returns False if the word is guessed correctly, otherwise returns True.

```format_score(score)```
Formats the score feedback (miss, misplaced, exact) for display.

```record_score_win()```
Records the player's win in the scores.md file with the number of attempts taken.

```record_score_loss()```
Records the player's loss in the scores.md file.


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


