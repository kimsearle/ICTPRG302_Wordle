import random
import datetime

with open('documents/target_words.txt', 'r') as target_all:
    target_list = target_all.read().splitlines()
with open('documents/all_words.txt', 'r') as valid_all:
    all_words_list = valid_all.read().splitlines()

GUESS_COUNT = 6
WORD_LENGTH = 5

target_word = random.choice(target_list)
char_target = list(target_word.lower())


def game_instructions():
    welcome = "Welcome to the Wordle Game!"
    aim = "Guess the target word within 6 attempts."
    instructions = """ 
Enter a valid 5-letter word as your guess.
Type a 5-letter word and press “enter” to see if any letters in it are also in word. Green tiles (🟩) mean you’ve
guessed the correct letter in the correct place in the word. A yellow tile (🟨) means you guessed a letter that’s
in the word but isn’t in the right spot. A white tile (⬜) means the letter is not in the word.
"""
    print(welcome, aim, instructions)


def help_info():
    help = """
MISS (⬜): The letter is not in the word  
MISPLACED (🟨): The letter is in the word but in the wrong position.  
EXACT (🟩): The letter is in the correct position.
    """
    print(help)


def guess_prompt():
    guesses_left = GUESS_COUNT
    while guesses_left > 0:
        guess_word = input("Enter a guess: ").lower()
        if guess_word in ("exit", "e"):
            print("thanks for playing!")
            return
        if guess_word in ("h", "help"):
            help_info()
            continue
        if guess_word in all_words_list and len(guess_word) == WORD_LENGTH:
            char_guess = list(guess_word.lower())
            if score_guess(char_guess):
                guesses_left -= 1
            else:
                return
        else:
            print("Sorry")


def score_guess(char_guess):
    score = []
    used_char = set()
    for i, char in enumerate(char_guess):
        if char == char_target[i]:
            score.append(2)
            used_char.add(i)
        elif char in char_target and char_target.index(char) not in used_char:
            score.append(1)
            used_char.add(char_target.index(char))
        else:
            score.append(0)
    print(" ".join(format_score(score)))
    if all(val == 2 for val in score):
        print("Congratulations!")
        return False
    return True


def format_score(score):
    score_tiles = {
        0: "⬜",
        1: "🟨",
        2: "🟩"
    }
    round_score = tuple(score)
    results = []
    for value in round_score:
        if value in round_score:
            results.append(score_tiles[value])
    return results

print(target_word)
game_instructions()
guess_prompt()

