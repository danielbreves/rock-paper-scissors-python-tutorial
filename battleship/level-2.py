"""
Nice work! Welcome to level 2!

In level 1 we set the name, size, and positions after creating the battleship.
But what about things that should start with a default value every time?

For example, every new battleship starts with no hits and a status of "afloat".
We can use a special method called __init__ to set these up automatically
when a new battleship is created.

A method is just a function that lives inside a class. The first input is
always "self", which means "this particular battleship".
"""

class Battleship:
    name: str
    size: int
    positions: list
    hits: list
    status: str

    # Step 1: Let's add an __init__ method that sets up hits and status.
    # Write the following below this line:
    # def __init__(self):
    #     self.hits = []
    #     self.status = "afloat"




destroyer = Battleship()
destroyer.name = "Destroyer"
destroyer.size = 3
destroyer.positions = ["A1", "A2", "A3"]

# Step 2: Print the hits and status to make sure they were set automatically.
# Write print(destroyer.hits) below this line:


# Write print(destroyer.status) below this line:


# Run the code with "python battleship/level-2.py" — you should see [] and "afloat"!

# Bonus: Let's add a new property to the Battleship class!

# Step 3: Add "age: int" to the class properties (after status on line 20).
# Then inside __init__, set a default: self.age = 0
# Print destroyer.age to check it works below this line:


# Run the code again to see the results!

# On to level-3.py!
