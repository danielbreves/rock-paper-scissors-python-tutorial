"""
Nearly there! Level 8!

What happens if the player types something silly like "banana"?
Let's check if their choice is in our list, and skip the turn if it's not.

We'll use "continue" to do this. When Python sees "continue" inside a loop,
it skips the rest of the turn and jumps back to the top of the loop.
"""

import random

life = 3

while life > 0:
    options = ["rock", "paper", "scissors"]
    player_hand = input("Enter your choice " + str(options) + ": ")

    # Step 1: Check if the player's choice is NOT in our list of valid options.
    # Write the following below this line:
    # if player_hand not in options:
    #     print("Oops! That's not a valid choice. Try again!")
    #     continue




    computer_hand = random.choice(options)

    print("The computer chose " + computer_hand + "!")

    if player_hand == computer_hand:
        print("It's a tie!")
    elif (player_hand == "rock" and computer_hand == "scissors") or \
         (player_hand == "paper" and computer_hand == "rock") or \
         (player_hand == "scissors" and computer_hand == "paper"):
        print("You win!")
    else:
        print("You lose!")
        life -= 1  # This is a shortcut for life = life - 1
        print("You have " + str(life) + " lives remaining.")  # str() turns a number into text

# Run the code with "python level-8.py" and try typing "banana"!

# One more to go! Open level-9.py!
