sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
sentence_split = sentence.split(" ")
# print(sentence_split)

result = {key: len(key) for key in sentence_split}
print(result)
