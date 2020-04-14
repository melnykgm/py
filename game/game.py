import random

def main():
  print(get_info())
  make_decision(get_user_choice(),get_comp_choice(1,3))
  

def get_info():
  info="""Make your choice:
1 - scissors
2 - rock
3 - paper"""
  return info

def get_user_choice():
  user_choice = int(raw_input())
  return user_choice

def get_comp_choice(x,y):
  comp_choice = random.randint(x,y)
  return comp_choice

def make_decision(user_choice,comp_choice):
  if user_choice == comp_choice:
    print("draw")
  if user_choice == 1 and comp_choice==2:
    print("you win")
  if user_choice == 1 and comp_choice==3:
    print("You lose")

  if user_choice==2 and comp_choice==3:
    print("you win")
  if user_choice==2 and comp_choice==1:
    print("You lose")

  if user_choice==3 and comp_choice==2:
    print("you lose")
  if user_choice==3 and comp_choice==1:
    print("You win")


main()
