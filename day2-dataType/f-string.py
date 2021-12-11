print(int(8 / 3 ))

#round
print(round(8 / 3, 2))

# // division to int
print( 8 // 3) 

score = 0
# User scores a point
score += 1

print(score)

height = 1.80
isWinning = True

# F-String

print(f"Your score is {score}, your height is {height}m, you are winning is {isWinning}")


# Life in weeks - Coding Exercise
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year_left = 90 - int(age)

month = year_left * 12
week = year_left * 52
day = year_left * 365

print (f"You have {day} days, {week} weeks, and {month} months left.")


