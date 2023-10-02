import random

choices = ["Rock", "Paper", "Scissors"]
player_score = 0
cpu_score = 0

while True:
  computer = random.choice(choices)
  player = input("Rock, Paper, or Scissors? ").capitalize()

  if player == "End":
    print("Final Scores:")
    print(f"CPU: {cpu_score}")
    print(f"Player: {player_score}")
    break

  if player not in choices:
    print("Invalid input. Please choose Rock, Paper, or Scissors.")
    continue

  print(f"Computer chose: {computer}")

  if player == computer:
    print("Tie!")
  elif (player == "Rock" and computer == "Scissors") or (
      player == "Paper" and computer == "Rock") or (player == "Scissors"
                                                    and computer == "Paper"):
    print(f"You win! {player} beats {computer}")
    player_score += 1
  else:
    print(f"You lose! {computer} beats {player}")
    cpu_score += 1
