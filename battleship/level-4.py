"""
Level 4! Time for players!

A battleship game needs players! Each player has a list of ships.

Let's create a Player class and give it a method to add ships.
"""

class Battleship:
    name: str
    positions: list
    hits: list
    status: str

    def __init__(self):
        self.hits = []
        self.status = "afloat"

    def check_status(self):
        if len(self.hits) == len(self.positions):
            self.status = "sunk"
        return self.status

    def receive_attack(self, position):
        if position in self.positions:
            self.hits.append(position)
            if self.check_status() == "sunk":
                print("You sunk the " + self.name + "!")
            return True
        return False


# Step 1: Let's create a Player class with a list of ships.
# Write the following below this line:
# class Player:
#     name: str
#     ships: list
#
#     def __init__(self):
#         self.ships = []




# Step 2: Can you write a method called "add_ship" that takes a ship and adds
# it to self.ships? Remember: methods inside a class must be indented!
# Hint: in level 3 we used self.hits.append(position) to add a hit — the same
# pattern works here with self.ships and ship.
# Write your add_ship method inside the Player class, after __init__:



# Step 3: Let's test it! Create a player and give them a ship.
# Write the following below this line:
# player1 = Player()
# player1.name = "Player 1"
#
# destroyer = Battleship()
# destroyer.name = "Destroyer"
# destroyer.positions = ["A1", "A2", "A3"]
#
# player1.add_ship(destroyer)
# print(player1.name + " has " + str(len(player1.ships)) + " ship(s)")



# Run the code with "python battleship/level-4.py"!

# Nice work! Head to level-5.py!
