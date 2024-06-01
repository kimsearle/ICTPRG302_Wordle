# Project Documentation
## Guess-My-Word Game
Guess-My-Word is a Python-based word guessing game where players attempt to guess a hidden 5-letter word within 6 attempts, receiving feedback on each guess to help them guess the correct word. This document provides an overview of the project, including setup, structure, and development guidelines.

### Requirements
Python 3.1x
external libraries required:

### Installation
Clone the repository:

```bash
git clone <repository_url>
cd guess-my-word
```
Ensure you have Python 3.1x installed:

```bash
python3 --version
```
### Project Structure
The project has the following structure:
```bash
guess-my-word/  
│  
├── guess_my_word_main.py          # Main game script  
├── README.md                      # Project documentation  
├── average_score_report.txt       # stats for all users
├── guess_log.txt                  # log of all games
├── scores.txt                     # list of usernames, score and timestamp
└── docments/                      # Directory containing project files  
     └── psudeocode.py             # psudocode for the game  
     └── all_words.txt                 # File containing all valid words 
     └── target_words.txt              # File containing target words 
     └── developer_documentation.md    # File containing developer documentation
     └── user_documentation.md         # File containing user documentation
     └── project_documentation.md      # File containing project documentation  
     └── flowchart.pdf                 # File containing flowchart of code algorithms           
 ```

### Usage
To start the game, run the guess_my_word.py script from the command line:

```bash
./guess_my_word.py
```
The game will prompt you to enter your guesses and will provide feedback after each guess.

### Development
**Code Style**  
Follow PEP8 for Python code style guidelines.   
Ensure that your code is compatible with Python 3.1x.  


### Key Functions
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


### Testing
To run the included doctests and ensure all functions behave as expected, execute the script with the test=True argument:

```bash
./guess_my_word.py
```
This will run all doctests embedded in the function docstrings.

### License
This project is licensed under the MIT License. See the LICENSE file for details.