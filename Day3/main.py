print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
  print('You can ride rollercoaster')
  age = int(input("What is your age? "))
  if age > 12 and age < 18:
    print("Cost $7")
  elif age >= 18:
    print("Cost $12")
  elif age <= 12:
    print("Cost $5")
  else:
    print("Your height is enough but your age isn't enough")
else:
  print("You can't ride the rollercoaster")


# number 2

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if number % 2 == 0:
  print('even Number')
else:
  print('odd number')

# Exercise

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi = weight / (height * height)
bmi_to_int = round(weight / height ** 2)

if bmi_to_int <18.5:
  print(f"Your bmi is {bmi_to_int} that is UNDERWEIGHT")
elif bmi_to_int > 18.5 and bmi_to_int <= 25:
  print(f"Your bmi is {bmi_to_int} that is NORMAL WEIGHT")
elif bmi_to_int > 25 and bmi_to_int <= 30:
  print(f"Your bmi is {bmi_to_int} that is OVER WEIGHT")
elif bmi_to_int > 30 and bmi_to_int <= 35:
  print(f"Your bmi is {bmi_to_int} that is OBESE")
else:
  print(f"Your bmi is {bmi_to_int} that are CLINICALLY OBESE")

# ================================================

  print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")



# LOGICAL OPERATOR
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
