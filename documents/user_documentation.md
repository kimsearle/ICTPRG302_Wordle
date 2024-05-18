# Guess-My-Word Game
Guess-My-Word is a fun and challenging game where you have to guess a hidden word within a limited number of attempts. Each guess provides feedback to help you guess the correct word.

## How to Play

#### Starting the Game: 
Run the script using Python 3.1x.

using bash, copy code:
```bash 
./wordle.py
```
#### Objective: 
Guess the target word within 6 attempts.

#### Input: 
Enter a 5-letter word as your guess.

#### Feedback:


MISS (⬜): The letter is not in the word  
MISPLACED (🟨): The letter is in the word but in the wrong position.  
EXACT (🟩): The letter is in the correct position.

#### Winning: 
Guess the word correctly to win the game.

#### Exiting: 
The game ends automatically when the word is guessed correctly or when you run out of attempts.  
You can also quit the game at any time by typing ```exit``` during the game 

### Example Gameplay

**Target word:** WORLD

**Guess:** hello

**Feedback:** H E L L O   
⬜ ⬜ ⬜ 🟩 🟨    
  
**Guess:** scold

**Feedback:** S C O L D
  
⬜ ⬜ 🟨 🟩 🟩  

**Guess:** world

**Feedback:** W O R L D
  
🟩 🟩 🟩 🟩 🟩  

**Winner!**
    
Continue guessing until you either guess the word correctly or use up all attempts.


### Help
For assistance, you can use the in-game help function by typing: 
```help``` during the game.

