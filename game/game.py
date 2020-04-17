import random
import sys


def main():
    score = [0, 0]
    while True:
        print(get_info())
        winner = make_decision(get_user_choice(), get_comp_choice(1, 3))
        score = update_score(score, winner)
        print(winner)
        print(score)
        exit_program()


def get_info():
    info = """Make your choice:
1 - scissors
2 - rock
3 - paper
4 - exit"""
    return info


def get_user_choice():
    user_choice = int(raw_input())
    return user_choice


def get_comp_choice(x, y):
    comp_choice = random.randint(x, y)
    return comp_choice


def exit_program():
    bye = "Thanks for the game, bye"
    return bye


def update_score(score, winner):
    if winner == 'user':
        score[0] = + 1
    elif winner == 'pc':
        score[1] = + 1
    return score


def make_decision(user_choice, comp_choice):
    if user_choice == comp_choice:
        print("draw")
        winner = 'draw'

    elif user_choice == 1 and comp_choice == 2 or user_choice == 2 and comp_choice == 3 or user_choice == 3 and comp_choice == 1:
        winner = 'user'


    elif user_choice == 1 and comp_choice == 3 or user_choice == 2 and comp_choice == 1 or user_choice == 3 and comp_choice == 2:
        winner = 'pc'


    elif user_choice == 4:
        print exit_program()
        sys.exit()

    return winner

    print winner()
    update_score(winner_name, score)


main()
