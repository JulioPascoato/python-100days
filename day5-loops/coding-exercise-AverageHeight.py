# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_height = 0
counter = 0

for height in student_heights:
    sum_height += height
    counter += 1

print (student_heights)
print (counter)

average = round(sum_height  / counter)
print(f"Input a list of student heights {average}")