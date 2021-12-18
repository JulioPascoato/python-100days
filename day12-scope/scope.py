################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

#Global Scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# There is no block scope


# Modyfying Global Scope

enemies = 1

def increase_enemies():
    #Avoid, just to know
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants
PI = 3.14159
URL = "https://wwww.google.com"



