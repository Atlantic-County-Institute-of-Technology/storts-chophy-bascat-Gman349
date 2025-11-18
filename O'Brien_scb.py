# variables and imports
import random
import inquirer3
import pyfiglet

word_list = []
max_tries = 5
word_length = 5


# welcome sign
def fancy_ascii_welcome():
    welcome_text = f"Welcome!"
    ascii_art = pyfiglet.figlet_format(welcome_text, font="epic")
    print(ascii_art)
    print("to Storts, Chophy, Bascat")

fancy_ascii_welcome()


def change_word_length():
    letter_len = [  # prompts user to change number of letters
        inquirer3.Text("num", message="how many letters?"),
    ]
    answers = inquirer3.prompt(letter_len)
    try:  # if number less then 10, change word length
        global word_length
        word_length = int(answers["num"])
        if 1 <= word_length <= 10:
            print(f"word length is now {word_length} letters long")
            return word_length
    except ValueError:  # else retry
        print("Please enter a valid number")
    else:
        print("Please try again")


def change_tries_length():
    letter_len = [
        inquirer3.Text("num", message="How many tries?"),
    ]
    answers = inquirer3.prompt(letter_len)
    try:
        global max_tries
        max_tries = int(answers["num"])
        if 1 <= max_tries <= 100:  # if number less than 100, change max tries
            print(f"You now have {max_tries} tries per game")
            return max_tries
    except ValueError:  # else retry
        print("Please enter a valid number")
    else:
        print("Please try again")


def extract_words():  # gets all words with the same length as word length
    global word_list
    word_list = []
    with open("assets/words_alpha.txt", "r") as dictionary:
        for word in dictionary.readlines():
            if len(word.strip()) == word_length:
                word_list.append(word.strip())


def word_check(guess_word_l, answer_word_l, guesses_l, prnt_statement=""):
    p = 0
    for x in answer_word_l:  # for each letter, check if its in the answer, and in the right spot
        if x == guess_word_l[p]:
            prnt_statement = f"{prnt_statement} {guess_word_l[p]}: Chophy"
        elif guess_word_l[p] in answer_word_l:
            prnt_statement = f"{prnt_statement} {guess_word_l[p]}: Storts"
        else:
            prnt_statement = f"{prnt_statement} {guess_word_l[p]}: Bascat"
        p += 1
    print(prnt_statement, f" You have {guesses_l} guesses left")


def game_round():
    # variables
    alive = True
    wrong = True
    play = True

    # create answer word
    extract_words()
    guesses_left = max_tries
    answer_word = f"{word_list[random.randint(0, len(word_list))]}"
    answer_word_list = list(answer_word)
    while play:
        while alive and wrong:
            questions = [  # prompt user for a guess
                inquirer3.Text("guess", message="What's your guess?"),
            ]
            answers = inquirer3.prompt(questions)
            guess_word = answers["guess"]
            if guess_word == "Gman349!":  # ultimate hacker code
                print(answer_word)
            else:
                if guess_word in word_list:  # checks if word is valid
                    guess_word_list = list(guess_word)
                    if guess_word_list == answer_word_list:  # checks if guess is correct before checking each letter
                        # ends game if correct
                        print("Congrats! you got it!")
                        wrong = False
                        play = False
                    guesses_left = guesses_left - 1
                    if alive and wrong:  # if guess wasn't correct, check each letter
                        word_check(guess_word_list, answer_word_list, guesses_left)
                    if guesses_left == 0 and wrong:  # if out of guesses, end game
                        alive = False
                        play = False
                        print(f"You lost! the word was {answer_word}")

                else:  # if not valid word
                    if len(guess_word) == word_length:
                        print("That is not a valid word")
                    else:
                        print(f"That is not {word_length} characters long")
    another = [  # prompt user to play again with same settings
        inquirer3.Confirm("stop", message="Play another?", default=False),
    ]

    answers = inquirer3.prompt(another)
    if answers["stop"]:  # if yes, run game round again, otherwise continue to main menu
        game_round()
    else:
        print("Returning to main menu!")


def main():
    questions = [  # creates menu for user
        inquirer3.List(
            "menu",
            message="What would you like to do?",
            choices=["Exit", "Change word length", "Change tries", "Play game"],
        ),
    ]
    answers = inquirer3.prompt(questions)
    match answers["menu"]:  # runs appropriate function to menu selection
        case "Exit":
            exit()
        case "Change word length":
            change_word_length()

        case "Change tries":
            change_tries_length()

        case "Play game":
            game_round()


while __name__ == "__main__":
    main()
