"""
You're on a roll! Level 3!

Now let's teach our battleship how to do things! We'll add methods that
check if the ship is sunk and handle being attacked.

Remember: a method is a function inside a class, and "self" means
"this particular battleship".
"""

class Battleship:
    name: str
    positions: list
    hits: list
    status: str

    def __init__(self):
        self.hits = []
        self.status = "afloat"

    # Step 1: Let's add a method that checks if the ship is sunk.
    # We can use len() to count the number of positions instead of keeping track
    # of size separately. A ship is sunk when the number of hits equals the number of positions.
    # Write the following below this line:
    # def check_status(self):
    #     if len(self.hits) == len(self.positions):
    #         self.status = "sunk"
    #     return self.status



    # Step 2: Now let's add a method that handles being attacked.
    # If the position is one of the ship's positions, it's a hit!
    # Write the following below this line:
    # def receive_attack(self, position):
    #     if position in self.positions:
    #         self.hits.append(position)
    #         if self.check_status() == "sunk":
    #             print("You sunk the " + self.name + "!")
    #         return True
    #     return False



destroyer = Battleship()
destroyer.name = "Destroyer"
destroyer.positions = ["A1", "A2", "A3"]

# Step 3: Let's test it! Try attacking all three positions to sink the ship.
# Write print(destroyer.receive_attack("A1")) below this line, then do the same for "A2" and "A3" on separate lines:



# Step 4: Now try attacking a position that's a miss (e.g. "B1") below this line:


# Run the code with "python battleship/level-3.py" — you should see True, True, True
# and "You sunk the Destroyer!", then False for the miss!

# Keep going! Open level-4.py to learn about debugging!
