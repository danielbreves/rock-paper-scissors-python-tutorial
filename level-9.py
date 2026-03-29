"""
The final level! You've come a long way!

But our code is getting long! Let's clean it up by putting the winner check
into its own function. A function is a reusable block of code that you
can call by name.
"""

import random

# Step 1: Let's create a function called "check_winner" that takes two inputs and returns a result.
# Write the following below this line:
# def check_winner(player_hand, computer_hand):
#     if player_hand == computer_hand:
#         return "It's a tie!"
#     elif (player_hand == "rock" and computer_hand == "scissors") or \
#          (player_hand == "paper" and computer_hand == "rock") or \
#          (player_hand == "scissors" and computer_hand == "paper"):
#         return "You win!"
#     else:
#         return "You lose!"








life = 3

while life > 0:
    options = ["rock", "paper", "scissors"]
    player_hand = input("Enter your choice " + str(options) + ": ")

    if player_hand not in options:
        print("Oops! That's not a valid choice. Try again!")
        continue

    computer_hand = random.choice(options)

    print("Computer chose " + computer_hand + "!")

    # Step 2: Now instead of all those if/elif/else lines, we can call our function!
    # Write "result = check_winner(player_hand, computer_hand)" below this line:


    # Step 3: Print the result below this line:


    # Step 4: Check if the player lost. Write the following below this line:
    # if result == "You lose!":
    #     life -= 1
    #     print("You have " + str(life) + " lives remaining.")




# Run the code with "python level-9.py" to make sure everything works!

# When you're done, open level-10.py for some bonus ideas!
