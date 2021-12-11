num_char = len(input("What is your name? "))

#type
print(type(num_char))

#type conversion

#to string
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

#to Float
a = float(123)
print(70 + float("100.5"))


#Data types - Coding Exercise
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

sum = int(two_digit_number[0]) + int(two_digit_number[1])

print(sum)