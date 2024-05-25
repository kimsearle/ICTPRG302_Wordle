"""Guess-My-Word is a game where the player has to guess a word. A terminal version of wordle
Author: Kim
Company: NM TAFE
Copyright: 2024

"""

import random
import datetime

# Load the word lists
with open('documents/target_words.txt', 'r') as target_all:
    target_list = target_all.read().splitlines()
with open('documents/all_words.txt', 'r') as valid_all:
    all_words_list = valid_all.read().splitlines()

# Constants
GUESS_COUNT = 6
WORD_LENGTH = 5

# Select a random target word
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
    username = input("Enter name: ").lower()
    guesses_left = GUESS_COUNT
    global total_guess_count
    total_guess_count = 0  # Reset for each game
    guess_log = []
    won = False

    while guesses_left > 0:
        guess_word = input("Enter a guess: ").lower()
        if guess_word in ("exit", "e"):
            print("Thanks for playing!")
            return
        if guess_word in ("h", "help"):
            help_info()
            continue
        if guess_word in all_words_list and len(guess_word) == WORD_LENGTH:
            char_guess = list(guess_word.lower())
            total_guess_count += 1
            formatted_score = score_guess(char_guess)
            guess_log.append((guess_word, formatted_score))
            if formatted_score == "🟩 🟩 🟩 🟩 🟩":
                won = True
                break
            guesses_left -= 1
        else:
            print("Sorry, please enter a valid guess.")

    if not won:
        print("Sorry, you lost 😭")
        print(f'The target word was: {target_word}')

    append_guess_log(username, target_word, guess_log, won)
    if won:
        record_score_win(username)
        print("Congratulations! 🎉🎉🎉🎉")
    else:
        record_score_loss(username)


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
    formatted_score = " ".join(format_score(score))
    print("  ".join(char_guess).upper())
    print(formatted_score)
    return formatted_score


def format_score(score):
    score_tiles = {
        0: "⬜",
        1: "🟨",
        2: "🟩"
    }
    return [score_tiles[val] for val in score]


def record_score_win(username):
    global total_guess_count
    with open("scores.txt", "a") as scores_file:
        scores_file.write(f'{username} guessed the word in {total_guess_count} on {datetime.date.today()}.\n')


def record_score_loss(username):
    global total_guess_count
    with open("scores.txt", "a") as scores_file:
        scores_file.write(f'{username} lost and did not guess the word on {datetime.date.today()}.\n')


def calculate_score_average():
    with open('scores.txt', 'r') as file:
        lines = file.readlines()
    user_scores = {}
    user_stats = {}

    for line in lines:
        parts = line.split()
        user_name = parts[0]
        if "guessed" in parts:
            score_index = parts.index("in") + 1
            score = int(parts[score_index])
            if user_name in user_scores:
                user_scores[user_name].append(score)
            else:
                user_scores[user_name] = [score]
            # Increment win count for the user
            user_stats[user_name] = user_stats.get(user_name, {"wins": 0, "losses": 0, "total": 0})
            user_stats[user_name]["wins"] += 1
            user_stats[user_name]["total"] += 1
        elif "lost" in parts:
            # Increment loss count for the user
            user_stats[user_name] = user_stats.get(user_name, {"wins": 0, "losses": 0, "total": 0})
            user_stats[user_name]["losses"] += 1
            user_stats[user_name]["total"] += 1

    with open('average_score_report.txt', 'w') as report_file:
        for user, scores in user_scores.items():
            average_score = sum(scores) / len(scores) if scores else 0
            win_percentage = (user_stats[user]["wins"] / user_stats[user]["total"]) * 100
            total_plays = user_stats[user]["total"]
            report_file.write(
                f"{user} has an average score of {average_score:.2f}, a win percentage of {win_percentage:.2f}"
                f"%, and a total of {total_plays} plays.\n")


def append_guess_log(username, target_word, guess_log, won):
    with open('guess_log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(f"Username: {username}\n")
        log_file.write(f"Target Word: {target_word}\n")
        log_file.write("Guesses:\n")
        for guess, formatted_score in guess_log:
            log_file.write(f"{guess}, Score: {formatted_score}\n")
        if won:
            log_file.write(f"Correct in {total_guess_count} guesses\n")
        else:
            log_file.write("Game lost\n")
        log_file.write(f"Date: {datetime.date.today().strftime('%d/%m/%Y')}\n")
        log_file.write("\n")


# Uncomment to print the target word for testing
# print(target_word)

game_instructions()
guess_prompt()
calculate_score_average()
