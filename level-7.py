"""
You're getting the hang of this! Level 7!

Programmers don't like to repeat themselves! But we have "rock", "paper", "scissors"
written in two places: once for the player's input and once for the computer's choice.

Let's save our options in a list variable so we only write them once!

One new thing: when we want to use a list inside a message, we need to turn it
into text first using str(). For example, str(options) turns the list into
the text "['rock', 'paper', 'scissors']".
"""

import random

life = 3

while life > 0:
    # Step 1: Let's put our options in a list called "options".
    # Write options = ["rock", "paper", "scissors"] below this line:


    # Step 2: Now let's use "options" in the input message.
    # Write player_hand = input("Enter your choice " + str(options) + ": ") below this line:


    # Step 3: Now let's use "options" for the computer's pick too.
    # Write computer_hand = random.choice(options) below this line:


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

# Run the code with "python level-7.py" to make sure it still works!

# Keep it up! Open level-8.py!
