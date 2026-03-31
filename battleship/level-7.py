"""
Level 7! Building the game!

So far we have a Battleship class and a Player class. Now we need something
to run the game itself! Let's create a Game class.

A Game needs two players. We pass them in when we create the game,
and __init__ saves them.

In this level we'll let players place their ships by typing positions.
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
    attacks: dict

    def __init__(self):
        self.ships = []
        self.attacks = {}

    def add_ship(self, ship):
        self.ships.append(ship)

    def receive_attack(self, position):
        for ship in self.ships:
            if ship.receive_attack(position):
                return "hit"
        return "miss"

    def attack(self, enemy, position):
        result = enemy.receive_attack(position)
        self.attacks[position] = result
        return result


# Step 1: Let's create the Game class with two players.
# Write the following below this line:
# class Game:
#     player1: Player
#     player2: Player
#
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2



# Step 2: Add a method that asks one player to place a ship.
# Write the following inside the Game class:
#     def place_ship(self, player):
#         ship_name = "Destroyer"
#         text = input(player.name + ", enter 3 positions for your " + ship_name + " (e.g. A1 A2 A3): ")
#         positions = text.split()  # turns "A1 A2 A3" into ["A1", "A2", "A3"]
#         ship = Battleship()
#         ship.name = ship_name
#         ship.positions = positions
#         player.add_ship(ship)



# Step 3: Add a setup method that calls place_ship for each player.
# We print 50 blank lines to hide the first player's positions!
# Write the following inside the Game class:
#     def setup(self):
#         players = [self.player1, self.player2]
#         for player in players:
#             self.place_ship(player)
#             print("\n" * 50) # \n is a newline character, so this prints 50 blank lines!
#             input("Pass the device to the other player and press Enter.")



# Step 4: Let's test it! Write the following below this line:
# player1 = Player()
# player1.name = "Player 1"
# player2 = Player()
# player2.name = "Player 2"
#
# game = Game(player1, player2)
# game.setup()
# print("Setup complete!")



# Run the code with "python battleship/level-7.py" and place your ships!

# Nearly there! Open level-8.py!
