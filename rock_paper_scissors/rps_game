import random

def main():
  print("Welcome to the game of Rock, Paper, Scissors!")
  print("You will be playing against the computer.")
  print("The first player to win three rounds wins the game.")
  print("Good luck!")
  print()
  player_score = 0
  computer_score = 0
  while player_score < 3 and computer_score < 3:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print("You chose:", player_choice)
    print("The computer chose:", computer_choice)
    result = get_result(player_choice, computer_choice)
    print(result)
    if result == "You win!":
      player_score += 1
    elif result == "The computer wins!":
      computer_score += 1
    print("Your score:", player_score)
    print("Computer score:", computer_score)
    print()
  if player_score == 3:
    print("Congratulations, you win!")
  else:
    print("Sorry, the computer wins.")
def get_player_choice():
  choice = input("Enter your choice (rock, paper, or scissors):")
  while choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please try again.")
    choice = input("Enter your choice (rock, paper, or scissors):")
  return choice
def get_computer_choice():
  return random.choice(["rock", "paper", "scissors"])
def get_result(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "It's a tie!"
  elif player_choice == "rock" and computer_choice == "scissors":
    return "You win!"
  elif player_choice == "paper" and computer_choice == "rock":
    return "You win!"
  elif player_choice == "scissors" and computer_choice == "paper":
    return "You win!"
  else:
    return "The computer wins!"
main()
