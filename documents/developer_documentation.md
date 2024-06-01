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

```select_random_word()```
Randomly chooses the target word at the start of each game

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

```record_score_win(username)```
Records the player's win in the scores.txt file with the number of attempts taken.

```record_score_loss(username)```
Records the player's loss in the scores.txt file.

```calculate_score_average()```
Records the total plays, average score and win percentage of each user in the average_score_report.txt file.

```append_guess_log(username, target_word, guess_log, won)```
Records the username and guess log (with a timestamp) of game in the guess_log.txt file.




