# MY SOLUTION
for i in range(1, 101):
  
  if i % 5 == 0 and i % 3 == 0:
    i = "FIZZBUZZ"
  elif i % 5 == 0:
    i = "BUZZ"
  elif i % 3 == 0:
    i = "FIZZ"
  print(i)

#   INSTRUCTOR SOLUTION
#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

#For Loop with Range

for number in range(1, 100):
  print(number)

for number in range(1, 101):
  print(number)

for number in range(1, 11, 3):
  print(number)

#Calculating the sum of all the numbers from 1 to 100.
total = 0
for number in range(1, 101):
  total += number
print(total)