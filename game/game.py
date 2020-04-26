import random
import sys
from typing import List


def main():
    """Runs the whole program."""
    score = [0, 0]
    choices = {'1': 'scissors',
               '2': 'rock',
               '3': 'paper'}
    print(get_info())
    while True:
        user_choice = get_user_choice()
        comp_choice = get_comp_choice(1, 3)
        check_for_exit_program(user_choice)
        if check_for_help(user_choice):
            continue
        winner = get_winner(user_choice, comp_choice)
        score = update_score(score, winner)
        user_choice, comp_choice = get_made_choices(user_choice,
                                                    str(comp_choice),
                                                    choices)
        print_report(winner, score, user_choice, comp_choice)


def get_made_choices(user_choice, comp_choice, choices):
    """Returning user's and computer's choices."""
    return choices[user_choice], choices[comp_choice]


def get_info():
    """Provides user with info what one should print to play this game."""
    info = """Make your choice:
1 - scissors
2 - rock
3 - paper
help - prints help info
exit - exit from game
"""
    return info


def get_user_choice():
    """Receives input from user and assigns it to variable user_choice, returns it."""
    user_choice = input("Type in your choice: ")
    return user_choice


def get_comp_choice(x, y):
    """Gets a random value in range from x to y and assigns it to variable comp_choice, returns it."""
    comp_choice = random.randint(x, y)
    return comp_choice


def check_for_exit_program(user_choice: str) -> None:
    """Check for exit and exits program."""
    if user_choice == 'exit':
        sys.exit()


def check_for_help(user_choice: str) -> bool:
    """Check for help and prints info."""
    if user_choice == 'help':
        print(get_info())
        return True
    else:
        return False


def update_score(score, winner):
    """Returns score with arguments score and winner."""
    if winner == 'user':
        score[0] += 1
    elif winner == 'computer':
        score[1] += 1
    return score


def get_winner(user_choice, comp_choice):
    """Makes decision about winner and returns it."""
    winner = ""
    user_choice = int(user_choice)

    if user_choice == comp_choice:
        winner = 'draw'

    elif user_choice == 1 and comp_choice == 2 or \
            user_choice == 2 and comp_choice == 3 or \
            user_choice == 3 and comp_choice == 1:
        winner = 'user'

    elif user_choice == 1 and comp_choice == 3 or \
            user_choice == 2 and comp_choice == 1 or \
            user_choice == 3 and comp_choice == 2:
        winner = 'computer'

    return winner


def print_report(winner: str, score: List, user_choice: str, comp_choice: str) -> None:
    """Prints winner, score, choices made by user and computer, and message if draw."""
    if winner != 'draw':
        print("""Your choice was: {0}
Computer choice was: {1}
Winner: {2}
####Score#### 
User: {3}
Computer: {4}
""".format(user_choice, comp_choice, winner, *score))
    else:
        print("""Your choice was: {0}
There is no winner: it's a Draw!""".format(user_choice))


main()
