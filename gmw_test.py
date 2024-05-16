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

print(target_word)



def guess_prompt():
    guesses_left = GUESS_COUNT
    while guesses_left > 0:
        guess_word = input("Enter a guess: ").lower()
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
    print(score)
    if all(val == 2 for val in score):
        print("Congratulations!")
        return False
    return True


guess_prompt()









