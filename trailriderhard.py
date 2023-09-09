"""
Survival Game - A simple text-based survival game.

The Goal is to Travel 1000 Miles
Keep track of your health and food. If either of these reach zero then GAME OVER. 
    You can hunt, just... beware of bears!
    You can rest to gain heath!
Keep Track of the weather!
    If its snowy you are more likely to get sick!
    If it stormy then your shelter can be detroyed!
Be mindful of your shelter!
    If your shelter is destroyed then you are more likley to get sick.
If you are sick or if your shelter is destory no worries!
    There is a 20% chance of finding a village!
        In the village you have the option to trade food for cures and a restored shelter! 

Good Luck!

Author: BluHerron
Date: September 8, 2023
"""

#Initialize Game
while True:
    import random
    # Initialize game variables
    PLAYER_NAME = input("Welcome to the Survival Game! Enter your name: ")
    PLAYER_HEALTH = 100
    FOOD_SUPPLY = 50
    MILEAGE = 0
    SHELTER_QUALITY = 50
    WEATHER = "Sunny"
    SICKNESS_COUNT = 0

    print(f"Welcome, {PLAYER_NAME}! Your journey begins.")

    # Main game loop
    while PLAYER_HEALTH > 0:
        print("\nOptions:")
        print("1. Continue on the trail")
        print("2. Hunt for food")
        print("3. Rest")
        print("4. Check shelter quality")
        print("5. Check weather")
        print("6. Quit the Game")

        # Check if the "Visit the village" option should appear
        if random.random() < 0.2:  # 20% chance of displaying "Visit Village"
            print("7. Visit the village")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            # Continue on the trail
            distance = random.randint(10, 20)
            MILEAGE += distance
            FOOD_SUPPLY -= random.randint(5, 10)

            # Adjust health loss based on weather
            if WEATHER == "Snowy":
                PLAYER_HEALTH -= random.randint(3, 6)
                if SHELTER_QUALITY == 0:
                    # Higher chance of illness in stormy or snowy weather when shelter quality is 0
                    if random.random() < 0.6:  # 60% chance of getting sick
                        print(
                            "Your shelter quality is 0, and you got sick in the stormy weather!")
                        SICKNESS_COUNT += 1
            else:
                PLAYER_HEALTH -= random.randint(2, 5)
                if SHELTER_QUALITY == 0:
                    # Higher chance of illness in stormy or snowy weather when shelter quality is 0
                    if random.random() < 0.4:  # 40% chance of getting sick
                        print(
                            "Your shelter quality is 0, and you got sick in the rainy weather!")
                        SICKNESS_COUNT += 1

            # Display current status
            print(f"Food supply: {FOOD_SUPPLY}, Health: {PLAYER_HEALTH}")
            print(f"Distance traveled: {MILEAGE} miles")

            # Check for game over conditions
            if FOOD_SUPPLY <= 0:
                print(f"Game over, {PLAYER_NAME}! You ran out of food.")
                break
            elif PLAYER_HEALTH <= 0:
                print(f"Game over, {PLAYER_NAME}! Your health reached zero.")
                break
            elif MILEAGE >= 1000:
                print(
                    f"Congratulations, {PLAYER_NAME}! You completed the journey.")
                break

        if choice == '2':
            # Hunt for food
            FOOD_FOUND = random.randint(5, 15)
            FOOD_SUPPLY += FOOD_FOUND
            PLAYER_HEALTH -= random.randint(2, 5)

            # Random occurrence: Chance of being mauled by a bear
            if random.random() < 0.05:  # 5% chance of bear attack
                print("While hunting, you were mauled by a bear!")
                BEAR_DAMAGE = random.randint(25,50)
                PLAYER_HEALTH -= BEAR_DAMAGE
                print(f"Health reduced to {PLAYER_HEALTH}")

            # Check for sickness
            if SICKNESS_COUNT > 0:
                # Extra health loss when sick
                PLAYER_HEALTH -= random.randint(5, 10)
                SICKNESS_COUNT += 1
                if SICKNESS_COUNT >= 3:
                    print("You got sick for the third time and couldn't continue. Game over.")
                    break
            else:
                # Random occurrence: Get sick when health is below 50
                if PLAYER_HEALTH < 50 and random.random() < 0.2:  # 20% chance of getting sick
                    print("You got sick while hunting!")
                    SICKNESS_COUNT += 1

            print(f"You found: {FOOD_FOUND} pounds of food.")
            print(f"Food supply: {FOOD_SUPPLY}, Health: {PLAYER_HEALTH}")

        if choice == '3':
            # Rest
            PLAYER_HEALTH += random.randint(5, 10)
            FOOD_SUPPLY -= random.randint(2, 5)

            # Check for sickness
            if SICKNESS_COUNT > 0:
                # Extra health loss when sick
                PLAYER_HEALTH -= random.randint(5, 10)
                SICKNESS_COUNT += 1
                if SICKNESS_COUNT >= 3:
                    print(
                        "You got sick for the third time and couldn't continue. Game over.")
                    break
            else:
                # Random occurrence: Get sick when health is below 50
                if PLAYER_HEALTH < 50 and random.random() < 0.2:  # 25% chance of getting sick
                    print("You got sick while resting!")
                    SICKNESS_COUNT += 1

            print("You rested and regained some health.")
            print(f"Food supply: {FOOD_SUPPLY}, Health: {PLAYER_HEALTH}")

        if choice == '4':
            # Check shelter quality
            SHELTER_QUALITY -= random.randint(2, 5)

            # Adjust shelter damage based on weather
            if WEATHER == "Stormy":
                SHELTER_QUALITY -= random.randint(3, 6)
                print("The shelter took extra damage due to the storm!")
            else:
                print("You checked the shelter quality.")

            print(f"The shelter quality is now {SHELTER_QUALITY}.")

        if choice == '5':
            # Check weather
            possible_weather = ["Sunny", "Rainy", "Snowy", "Stormy"]
            WEATHER = random.choice(possible_weather)
            print(f"The weather is {WEATHER}.")

        if choice == '7' and random.random() < 0.2:  # 20% chance of displaying "Visit Village"
            # Visit the village
            print("You arrived at a village.")
            print("Options:")
            print("1. Trade 20 food to remove sickness")
            print("2. Trade 15 food to restore shelter quality")
            print("3. Leave the village")

            village_choice = input("Enter your choice (1/2/3): ")

            if village_choice == '1':
                # Trade 20 food to remove sickness
                if FOOD_SUPPLY >= 20 and SICKNESS_COUNT > 0:
                    FOOD_SUPPLY -= 20
                    SICKNESS_COUNT = 0
                    print("You traded 20 food to remove sickness.")
                elif SICKNESS_COUNT == 0:
                    print("You are not sick.")
                else:
                    print("You don't have enough food to trade for the remedy.")

            elif village_choice == '2':
                # Trade 15 food to restore shelter quality
                if FOOD_SUPPLY >= 15:
                    FOOD_SUPPLY -= 15
                    SHELTER_QUALITY = 100
                    print("You traded 15 food to restore shelter quality.")
                else:
                    print("You don't have enough food to trade for shelter repair.")

            elif village_choice == '3':
                print("You left the village.")


        elif choice == '6':
            # Quit the game
            print(
                f"Thanks for playing, {PLAYER_NAME}! You traveled a total of {MILEAGE} miles.")
            break

        # Add a line to separate turns
        print("-" * 40)  # Prints 40 dashes as a separator

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

    # End of game loop

    # Add a line to separate turns
    print("-" * 40)  # Prints 40 dashes as a separator

    # Game has ended (win or lose)
print("Game over!")
