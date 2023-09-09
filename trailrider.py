"""
Teaching myself to code, while relying heavily on ChatGPT.
This is the base game that ChatGPT provided me.

Author: BluHerron
Date: September 8, 2023
"""

import random

# Initialize game variables
PLAYER_NAME = input("Welcome to the Survival Game! Enter your name: ")
PLAYER_HEALTH = 100
FOOD_SUPPLY = 50
MILEAGE = 0

print(f"Welcome, {PLAYER_NAME}! Your journey begins.")

# Main game loop
while PLAYER_HEALTH > 0:
    print("\nOptions:")
    print("1. Continue on the trail")
    print("2. Hunt for food")
    print("3. Rest")
    print("4. Quit the game")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # Continue on the trail
        DISTANCE = random.randint(10, 20)
        MILEAGE += DISTANCE
        FOOD_SUPPLY -= random.randint(5, 10)
        PLAYER_HEALTH -= random.randint(2, 5)

        print(f"You traveled {DISTANCE} miles. Food supply: {FOOD_SUPPLY}, Health: {PLAYER_HEALTH}")

    elif choice == '2':
        # Hunt for food
        FOOD_FOUND = random.randint(5, 15)
        FOOD_SUPPLY += FOOD_FOUND
        PLAYER_HEALTH -= random.randint(2, 5)

        print(f"You found {FOOD_FOUND} pounds of food.")
        print(f"Food supply: {FOOD_SUPPLY}, Health: {PLAYER_HEALTH}")

    elif choice == '3':
        # Rest
        PLAYER_HEALTH += random.randint(5, 10)
        FOOD_SUPPLY -= random.randint(2, 5)

        print("You rested and regained some health.")
        print(f"Food supply: {FOOD_SUPPLY}, Health: {PLAYER_HEALTH}")

    elif choice == '4':
        # Quit the game
        print(f"Thanks for playing, {PLAYER_NAME}! You traveled a total of {MILEAGE} miles.")
        break

    # Check for game over conditions
    if FOOD_SUPPLY <= 0:
        print(f"Game over, {PLAYER_NAME}! You ran out of food.")
        break
    elif PLAYER_HEALTH <= 0:
        print(f"Game over, {PLAYER_NAME}! Your health reached zero.")
        break
    elif MILEAGE >= 200:
        print(f"Congratulations, {PLAYER_NAME}! You completed the journey.")
        break
