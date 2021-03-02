import random 

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

love_score = random.randint(0, 100)
print(f"Your love score is {love_score}")

# EXERCISE Challenge number 1
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
# import random

random_number = random.randint(0, 1)

if random_number == 1:
  print('Heads')
else:
  print('Tails')

# List
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america.append('GAMALAND')
states_of_america.pop()

print(states_of_america)


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# EXERCISE CHALLENGE NUMBER 2
# import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len_name = len(names)
random_name = random.randint(0, len_name - 1)
print(f"{names[random_name]} is going to buy a meal today")


# NESTED LIST
dirty_fruits = ["Strawberries", "Apples", "Grapes", "Pears", "Cherries", "Peaches"]
dirty_vegetables = ["Spinach", "Kale", "Nectarines", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [dirty_fruits, dirty_vegetables]

print(dirty_dozen[1][2])

# EXERCISE CHALLENGE NUMBER 3 : NESTED LIST
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

map[horizontal - 1][vertical - 1] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

