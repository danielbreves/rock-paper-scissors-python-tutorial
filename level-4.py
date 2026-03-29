"""
Level 4 already? Let's go!

Let's put it all together and figure out who wins!
We'll use "if" to compare the player's hand to the computer's hand.

New things in this level:
  "==" checks if two things are the same. (One "=" sets a value, two "==" compares.)
  "and" means both sides must be true at the same time.

Important: In Python, the spaces at the start of a line matter!
The code inside an "if" must be indented (moved to the right) with 4 spaces.
This is how Python knows which code belongs inside the "if".
"""

import random

options = ["rock", "paper", "scissors"]
player_hand = input("Enter your choice (rock, paper, scissors): ")
computer_hand = random.choice(options)

print("The computer chose " + computer_hand + "!")

# Step 1: First let's check if it's a tie. Write the following below this line:
# if player_hand == computer_hand:
#     print("It's a tie!")



# Step 2: Now let's check if the player wins with rock. Write the following below this line:
# if player_hand == "rock" and computer_hand == "scissors":
#     print("You win! Rock beats scissors!")



# Step 3: Can you figure out the other two winning combinations?
# Hint: paper beats rock, and scissors beats paper.
# Write two more "if" checks below this line:





# Run the code with "python level-4.py" and try to win!

# Nice work! Head to level-5.py!
