import random
import sys


def main():
    score = [0, 0]
    choices = {'1': 'scissors',
               '2': 'rock',
               '3': 'paper'}
    while True:
        print(get_info())
        user_choice = get_user_choice()
        comp_choice = get_comp_choice(1, 3)
        print_made_choices(user_choice, str(comp_choice), choices)
        winner = make_decision(user_choice, comp_choice)
        score = update_score(score, winner)
        if winner != 'draw':
            print("Winner: {0}".format(winner))
        print('####Score####', '\nUser: {0}\nComputer: {1}'.format(*score))
        exit_program()
        print('\n')


def print_made_choices(user_choice, comp_choice, choices):
    print("Your choice was: \"{0}\", computer choice was: \"{1}\"".format(choices[user_choice], choices[comp_choice]))


def get_info():
    info = """Make your choice:
1 - scissors
2 - rock
3 - paper
exit - exit from game"""
    return info


def get_user_choice():
    user_choice = input()
    return user_choice


def get_comp_choice(x, y):
    comp_choice = random.randint(x, y)
    return comp_choice


def exit_program():
    bye = "Thanks for the game, bye"
    return bye


def update_score(score, winner):
    if winner == 'user':
        score[0] += 1
    elif winner == 'computer':
        score[1] += 1
    return score


def make_decision(user_choice, comp_choice):
    winner = ""
    if user_choice == 'exit':
        print(exit_program())
        sys.exit()
    user_choice = int(user_choice)

    if user_choice == comp_choice:
        print("There is no winner: it's a draw")
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


main()
