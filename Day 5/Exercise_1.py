# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
print(student_heights)

lenght = 0
sum = 0

# len(student_heights)
# sum(student_heights)
for i in student_heights:
  sum += i
  lenght += 1

average = round(sum/lenght)
# average = round( sum(student_heights) / len(student_heights) )
print(f"The average height of all students are{average}")