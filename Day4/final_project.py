import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_choice = [rock, paper, scissors]

player = int(input("What your choice? 0 for rock, 1 for paper, 2 for scissors "))


player_choice = list_choice[player]
print(player_choice)


computer = random.randint(0, len(list_choice))
computer_choice = list_choice[computer]
print('Computer Choice: \n')
print(computer_choice)

if player >= 3 or player < 0:
  print('Out of range')
elif player == 0 and computer == 2:
  print('Player win')
elif player == 2 and computer == 0:
  print('Computer win')
elif computer > player:
  print('computer win')
elif computer < player:
  print('player win')
elif computer == player:
  print('Game Tight!!!')

# SOLUTION NUMBER 2
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_choice = [rock, paper, scissors]
# Player Choice
player_choice = int(input("Choice 0 for rock, 1 for paper, 2 for scissors "))
print(list_choice[player_choice])

# Computer Random Choice
computer_choice = random.randint(0, 2)
print(list_choice[computer_choice])

# If statement for result
if player_choice >= 3 or player_choice < 0:
  print('Out of range')
elif player_choice == 0 and computer_choice == 2:
  print('Player win')
elif player_choice == 2 and computer_choice == 0:
  print('Computer win')
elif player_choice == 1 and computer_choice == 2:
  print('Computer win')
elif player_choice == 2 and computer_choice == 1:
  print('Player win')
elif player_choice == 0 and computer_choice == 1:
  print('Player Lose')
elif player_choice == 1 and computer_choice == 0:
  print('Computer lose')
elif player_choice == computer_choice:
  print('Game Tight')