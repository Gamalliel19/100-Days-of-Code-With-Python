#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print('welcome to the tip calculator!')
total_bill = input('What was the total bill? $')
total_bill_as_float = float(total_bill)

percentage = input('What percentage tip would you like to give? 10, 12, or 15? ')
percentage_as_float = float(percentage)


potongan = (percentage_as_float / 100) + 1

a = total_bill_as_float * potongan


split_people = input('How many people to split the bill? ')

split_people_as_float = float(split_people)

total = a / split_people_as_float
totals = float(round(total, 2))

# total_round_by_2 = str(round(total, 3))
result = f"Each person should pay: ${totals}"

print(result)

