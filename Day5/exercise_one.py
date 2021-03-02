# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# SUM sum() function Logic
jumlah = 0
for i in student_heights:
  jumlah += i
# total = jumlah / 7
# print(int(round(total, 0)))


# len() function logic
length = 0
for j in student_heights:
  length += 1
print(f"Length of this input is {length}")

average = round(jumlah / length)
print(average)

print(f"Total penjumlahan inputan kamu = {jumlah} dibagi dengan jumlah panjangnya dan dibulatkan = {average}")