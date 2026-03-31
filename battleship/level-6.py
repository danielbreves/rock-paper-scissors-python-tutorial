"""
Level 6! Let's battle!

Now let's teach players how to attack and be attacked.

When a player gets attacked, we check each of their ships to see if
the position is a hit. When a player attacks, we save the result in
a dictionary so they can see what they've tried.

A dictionary stores pairs of things — like a position and its result.
For example: {"A1": "hit", "B3": "miss"}
You can add to a dictionary like this: attacks["A1"] = "hit"

Notice that Player and Battleship both have a method called receive_attack.
That's OK! They do different things — the Player's version checks all its
ships, while the Battleship's version checks one ship's positions.
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


class Player:
    name: str
    ships: list
    attacks: dict  # this is new!

    def __init__(self):
        self.ships = []
        self.attacks = {}  # an empty dictionary to track our attacks

    def add_ship(self, ship):
        self.ships.append(ship)

    # Step 1: Let's add a method that handles being attacked.
    # It checks each ship to see if the position is a hit.
    # Write the following below this line:
    # def receive_attack(self, position):
    #     for ship in self.ships:
    #         if ship.receive_attack(position):
    #             return "hit"
    #     return "miss"



    # Step 2: Can you complete the "attack" method below? It should:
    #   1. Call enemy.receive_attack(position) and save the result in a variable
    #   2. Save the result in self.attacks[position] (that's how you add to a dictionary!)
    #   3. Return the result
    def attack(self, enemy, position):
        pass  # Pass does nothing! Replace it with your code!



# Let's test it!
player1 = Player()
player1.name = "Player 1"

player2 = Player()
player2.name = "Player 2"

ship = Battleship()
ship.name = "Destroyer"
ship.positions = ["A1", "A2", "A3"]
player2.add_ship(ship)

# Step 3: Let's attack! Write the following below this line:
# print(player1.attack(player2, "A1"))
# print(player1.attack(player2, "B5"))
# print("Player 1's attacks: " + str(player1.attacks))



# Run the code with "python battleship/level-6.py" — you should see "hit", "miss",
# and the attacks dictionary!

# Open level-7.py for the next challenge!
