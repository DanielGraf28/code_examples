import random
def player1(prev_play, player2_history=[]):
  player1_choice = ""
  player2_history.append(prev_play)
  player1_choice = ""
  player1_choice = random.choice(["R", "P", "S"])
  if len(player2_history) > 4:
    player1_choice = player2_history[-3]
    return player1_choice
  if len(player2_history) > 30:
    player1_choice = player2_history[-2]
    return player1_choice
  if len(player2_history) > 60:
    player1_choice = player2_history[-1]
    return player1_choice
  if len(player2_history) > 100:
    player1_choice = player2_history[-4]
    return player1_choice
def play(player1, player2, num_games, verbose=False):
  player_choice = ""
  player1_wins = 0
  player2_wins = 0
  for _ in range(num_games):
    player1_choice = choice(["R", "P", "S"])
    player2_choice = choice(["R", "P", "S"])
    if player1_choice == "R" and player2_choice == "S":
      player1_wins += 1
    elif player1_choice == "P" and player2_choice == "R":
      player1_wins += 1
    elif player1_choice == "S" and player2_choice == "P":
      player1_wins += 1
    elif player1_choice == player2_choice:
      player1_wins += 0
    else:
      player2_wins += 1
    if verbose:
      print("Player 1 wins: ", player1_wins)
      print("Player 2 wins: ", player2_wins)
    if player1_wins > player2_wins:
      print("Player 1 wins!")
    elif player2_wins > player1_wins:
      print("Player 2 wins!")
    else:
      print("It's a tie!")
