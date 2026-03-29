"""
Level 6! Things are getting interesting!

Right now the game only plays once. Let's use a "while" loop to keep playing
until the player runs out of lives!

A "while" loop repeats the code inside it over and over, as long as
something is true. For example, "while life > 0" means "keep going
as long as the player has lives left".

Tip: if you get stuck in the game and want to stop it, press Ctrl+C in the terminal.
"""

import random

life = 3

# Step 1: We need a while loop that keeps going as long as the player has lives.
# Write "while life > 0:" below this line, and make sure everything after it is indented:

    player_hand = input("Enter your choice (rock, paper, scissors): ")
    computer_hand = random.choice(["rock", "paper", "scissors"])

    print("The computer chose " + computer_hand + "!")

    if player_hand == computer_hand:
        print("It's a tie!")
    elif (player_hand == "rock" and computer_hand == "scissors") or \
         (player_hand == "paper" and computer_hand == "rock") or \
         (player_hand == "scissors" and computer_hand == "paper"):
        print("You win!")
    else:
        print("You lose!")
        # Step 2: When the player loses, we need to subtract 1 from their lives.
        # Write "life = life - 1" below this line:


        # Step 3: Let's tell the player how many lives they have left.
        # Write print("You have", life, "lives remaining.") below this line:


# level-7.py is waiting for you!
