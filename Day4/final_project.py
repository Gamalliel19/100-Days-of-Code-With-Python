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