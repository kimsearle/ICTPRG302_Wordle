"""Guess-My-Word is a game where the player has to guess a word a terminal version of wordle
Author: Kim
Company: NM Tafe
Copyright: 2024

"""

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
total_guess_count = 0


def game_instructions():
    welcome = "Welcome to the Wordle Game!"
    aim = "Guess the target word within 6 attempts."
    instructions = """ 
Enter a valid 5-letter word as your guess.
Type a 5-letter word and press “enter” to see if any letters in it are also in word. Green tiles (🟩) mean you’ve
guessed the correct letter in the correct place in the word. A yellow tile (🟨) means you guessed a letter that’s
in the word but isn’t in the right spot. A white tile (⬜) means the letter is not in the word.
Enter "E" or "exit" to exit the game
Enter "H" or "help" to see the instructions again
"""
    print(welcome, aim, instructions)


def help_info():
    game_help = """
Enter a valid 5-letter word as your guess.
Your guess will receive the following feedback:
MISS (⬜): The letter is not in the word  
MISPLACED (🟨): The letter is in the word but in the wrong position.  
EXACT (🟩): The letter is in the correct position.

Enter "E" or "exit" to exit the game
    """
    print(game_help)


def guess_prompt():
    guesses_left = GUESS_COUNT
    global total_guess_count
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
            total_guess_count += 1
            if score_guess(char_guess):
                guesses_left -= 1
            else:
                return
        else:
            print("Sorry, please enter a valid guess.")
    print("You lost")
    print(f'The target word was: {target_word}')
    record_score_loss()


def score_guess(char_guess):
    score = [0] * WORD_LENGTH
    used_char = set()
    for i, char in enumerate(char_guess):
        if char == char_target[i]:
            score[i] = 2
            used_char.add(i)
    for i, char in enumerate(char_guess):
        if score[i] == 0:
            for j, target_char in enumerate(char_target):
                if target_char == char and j not in used_char:
                    score[i] = 1
                    used_char.add(j)
                    break
    print(" ".join(format_score(score)))
    if all(val == 2 for val in score):
        print("Congratulations!")
        record_score_win()
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


def record_score_win():
    global total_guess_count
    username = input("Enter name: ")
    scores_file = open("scores.md", "a")
    scores_file.write(f'{username} guessed the word in {total_guess_count} on {datetime.date.today()}.\n')


def record_score_loss():
    global total_guess_count
    username = input("Enter name: ")
    scores_file = open("scores.md", "a")
    scores_file.write(f'{username} lost and did not the word on {datetime.date.today()}.\n')


# print(target_word)
game_instructions()
guess_prompt()
