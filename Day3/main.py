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



  