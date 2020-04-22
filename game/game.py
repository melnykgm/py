import random
import sys


def main():
    """Runs the whole program."""
    while True:
        print(get_info())
        print_report()


def get_made_choices(user_choice, comp_choice, choices):
    """Printing user's and computer's choices."""
    return "Your choice was: \"{0}\", computer choice was: \"{1}\"".format(choices[user_choice], choices[comp_choice])


def get_info():
    """Provides user with info what one should print to play this game."""
    info = """Make your choice:
1 - scissors
2 - rock
3 - paper
exit - exit from game"""
    return info


def get_user_choice():
    """Receives input from user and assigns it to variable user_choice, returns it."""
    user_choice = input()
    return user_choice


def get_comp_choice(x, y):
    """Gets a random value in range from x to y and assigns it to variable comp_choice, returns it."""
    comp_choice = random.randint(x, y)
    return comp_choice


def exit_program():
    """Writes text we assign in variable bye."""
    return "Thanks for the game, bye"


def update_score(score, winner):
    """Returns score with arguments score and winner."""
    if winner == 'user':
        score[0] += 1
    elif winner == 'computer':
        score[1] += 1
    return score


def get_decision(user_choice, comp_choice):
    """Returns the result of user's decision compared with computer's decision, exits the program if user prints
    exit."""
    winner = ""

    if user_choice == 'exit':
        return exit_program()

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


def print_report():
    score = [0, 0]
    choices = {'1': 'scissors',
               '2': 'rock',
               '3': 'paper'}
    user_choice = get_user_choice()
    comp_choice = get_comp_choice(1, 3)
    winner = get_decision(user_choice, comp_choice)
    if winner == 'exit':
        print(exit_program())
        quit()
    if winner != 'draw':
        print("Winner: {0}".format(winner))
    if winner == 'draw':
        print("There is no winner: it's a Draw")
    score = update_score(score, winner)
    print(get_made_choices(user_choice, str(comp_choice), choices))
    print('####Score####', '\nUser: {0}\nComputer: {1}'.format(*score))
    print('\n')


main()

# не працює правильно вихід і не плюсується рахунок score

