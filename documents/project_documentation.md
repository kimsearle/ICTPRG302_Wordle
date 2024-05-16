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
├── guess_my_word.py           # Main game script  
├── words.txt                  # File containing all valid words  
├── target_words.txt           # File containing target words  
├── README.md                  # Project documentation  
├── LICENSE                    # License file  
└── tests/                     # Directory containing test files  
     └── test_guess_my_word.py # Unit tests for the game  
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
**play():** Controls the game loop.   
**is_correct(score):** Checks if the guess is correct.   
**get_valid_words(file_path=ALL_WORDS):** Returns a list of valid words.   
**get_target_word(file_path=TARGET_WORDS, seed=None):** Returns a random target word.  
**ask_for_guess(valid_words):** Prompts the user for a guess.  
**score_guess(guess, target_word):** Scores the guess against the target word.  
**format_score(guess, score):** Formats the guess and its score for display.  


### Testing
To run the included doctests and ensure all functions behave as expected, execute the script with the test=True argument:

```bash
./guess_my_word.py
```
This will run all doctests embedded in the function docstrings.

### License
This project is licensed under the MIT License. See the LICENSE file for details.