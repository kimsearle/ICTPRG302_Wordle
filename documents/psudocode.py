# Guess-My-Word Game

# Read target words and valid words from files
target_list = read_lines_from_file("target_words.txt")
all_words_list = read_lines_from_file("all_words.txt")

# Constants
GUESS_COUNT = 6
WORD_LENGTH = 5

# Select a random target word
target_word = select_random_word(target_list)
char_target = convert_word_to_characters(target_word)

total_guess_count = 0

# Display game instructions
display_game_instructions()

# Start the game loop
while true:
    guesses_left = GUESS_COUNT

    # Prompt the user for a guess
    while guesses_left > 0:
        guess_word = get_user_input("Enter a guess: ")

        # Check if user wants to exit or get help
        if guess_word == "exit" or guess_word == "e":
            display_message("Thanks for playing!")
            return
        if guess_word == "help" or guess_word == "h":
            display_help_info()
            continue

        # Validate the guess
        if is_valid_guess(guess_word):
            char_guess = convert_word_to_characters(guess_word)
            total_guess_count += 1

            # Score the guess
            if score_guess(char_guess):
                guesses_left -= 1
            else:
                return
        else:
            display_message("Sorry, please enter a valid guess.")

    # Player ran out of guesses
    display_message("You lost")
    display_message("The target word was: " + target_word)
    record_score_loss()

# Function to score the guess
function
score_guess(char_guess):
score = initialize_score_list(WORD_LENGTH)
used_char = create_empty_set()

# First pass: Find exact matches
for each character in guess_word:
    if character matches character in the same position in target_word:
        score[position] = 2
        add_position_to_used_chars(position)

# Second pass: Find wrong position matches
for each character in guess_word:
    if character does not match character in the same position in target_word:
        for each character in target_word:
            if character matches guessed character and position not in used_chars:
                score[position] = 1
                add_position_to_used_chars(position)
                break

display_score(score)

if all_elements_are_2(score):
    display_message("Congratulations!")
    record_score_win()
    return false

return true
