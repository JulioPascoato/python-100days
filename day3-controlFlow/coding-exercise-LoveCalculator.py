# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
scoreTrue = 0
scoreLove = 0

scoreTrue += name1.lower().count("t")
scoreTrue += name1.lower().count("r")
scoreTrue += name1.lower().count("u")
scoreTrue += name1.lower().count("e")

scoreTrue += name2.lower().count("t")
scoreTrue += name2.lower().count("r")
scoreTrue += name2.lower().count("u")
scoreTrue += name2.lower().count("e")

scoreLove += name1.lower().count("l")
scoreLove += name1.lower().count("o")
scoreLove += name1.lower().count("v")
scoreLove += name1.lower().count("e")

scoreLove += name2.lower().count("l")
scoreLove += name2.lower().count("o")
scoreLove += name2.lower().count("v")
scoreLove += name2.lower().count("e")

score = int(str(scoreTrue) + str(scoreLove))


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")