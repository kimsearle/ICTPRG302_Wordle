# Guess-My-Word Game
Guess-My-Word is a fun game where you have to guess a hidden word within a limited number of attempts. Each guess provides feedback to help you guess the correct word.

## How to Download Game:

####Download the Game from GitHub:

Visit: [https://github.com/kimsearle/ICTPRG302_guess-my-word] 
Click on the green "Code" button and select "Download ZIP".
Extract the downloaded ZIP file to your desired location on your computer.  

Alternatively, if you have Git installed, you can clone the repository:
```bash
git clone https://github.com/your-username/your-repository.git
```  
Open your terminal and navigate to the directory where you extracted or cloned the repository: 
```bash
cd path/to/your-repository
```  
 #### Run the Game
Make sure you have Python installed on your system. If not, download and install it from python.org.

In the terminal, run the game script:
```bash
python gmw.py
```

## How to Play

#### Starting the Game: 

#### Objective: 
Guess the target word within 6 attempts.

#### Input: 
Enter a 5-letter word as your guess.

#### Special Commands:

Enter "E" or "exit" to quit the game.
Enter "H" or "help" to view the instructions again.  

#### Feedback:


MISS (⬜): The letter is not in the word  
MISPLACED (🟨): The letter is in the word but in the wrong position.  
EXACT (🟩): The letter is in the correct position.

#### Winning: 
Guess the word correctly to win the game.


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
You will have the option to play again after each game


### Help
For assistance, you can use the in-game help function by typing: 
```help``` during the game.

