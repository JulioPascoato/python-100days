import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# 0 - Rock
# 1 - Paper
# 2 - Scissors

game_images = [rock, paper, scissors]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# print player chose
print(game_images[choose])

computer_chose = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer_chose])

if choose == 0 and computer_chose == 2:
    print("You win")
elif choose == 2 and computer_chose == 1:
    print("You win")
elif choose == 1 and computer_chose == 0:
    print("You win")
elif choose == computer_chose:
    print("It's a draw")
else:
    print("You lose")
