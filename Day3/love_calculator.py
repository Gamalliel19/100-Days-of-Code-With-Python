# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# MY SOLUTION
name_1 = name1.lower()
name_2 = name2.lower()

true_total = name_1.count('t') + name_1.count('r') + name_1.count('u') + name_1.count('e') + name_2.count('t') + name_2.count('r') + name_2.count('u') + name_2.count('e') 

love_total = name_1.count('l') + name_1.count('o') + name_1.count('v') + name_1.count('e') + name_2.count('l') + name_2.count('o') + name_2.count('v') + name_2.count('e')

result = f"{true_total}{love_total}"

result_int = int(result)

if result_int < 10 or result_int > 90:
  print(f"Your Score is {result_int}, You go together like coke and mentos.")
elif result_int >= 40 and result_int <= 50:
  print(f"Your Score is {result_int}, you are alright together.")
else:
  print(f"Your Score is {result_int}")



#   ANGELA YU SOLUTION
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")














