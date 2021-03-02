# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# highest score
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"Nilai Maksimum = {highest_score}")

# lowest score
lowest_score = highest_score
for lowest in student_scores:
  if lowest < lowest_score:
    lowest_score = lowest
print(f"Nilai Minimum = {lowest_score}")

# SUM score
total_score = 0
for scores in student_scores:
  total_score += scores
print(f"Nilai Total semuanya = {total_score}")

# Length score
length_score = 0
for length in student_scores:
  length_score += 1
print(f"Nilai Panjang Inputan = {length_score}")

# Nilai Rata - Rata atau Average
average = round(total_score / length_score)
print(f"Nilai Rata Rata = {average}")
