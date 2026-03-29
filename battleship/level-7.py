"""
You're getting the hang of this! Level 7!

Now let's add the play loop! Players will take turns attacking each other.

After each attack we'll show the result and print a list of all their
previous attacks so they can keep track.
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


class Game:
    player1: Player
    player2: Player

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def place_ship(self, player):
        ship_name = "Destroyer"
        text = input(player.name + ", enter 3 positions for your " + ship_name + " (e.g. A1 A2 A3): ")
        positions = text.split()
        ship = Battleship()
        ship.name = ship_name
        ship.positions = positions
        player.add_ship(ship)

    def setup(self):
        players = [self.player1, self.player2]
        for player in players:
            self.place_ship(player)
            print("\n" * 50)
            input("Pass the device to the other player and press Enter.")

    # Step 1: Add a play method with a loop where players take turns.
    # We use two variables to keep track of whose turn it is.
    # Write the following below this line:
    # def play(self):
    #     current_player = self.player1
    #     next_player = self.player2
    #
    #     while True:
    #         position = input(current_player.name + "'s turn! Which position do you want to attack? ")
    #         result = current_player.attack(next_player, position)
    #         print(position + " is a " + result + "!")
    #         print("Your attacks: " + str(current_player.attacks))
    #
    #         # Swap turns — we need a temporary variable so we don't lose track
    #         previous_player = current_player
    #         current_player = next_player
    #         next_player = previous_player



player1 = Player()
player1.name = "Player 1"
player2 = Player()
player2.name = "Player 2"

game = Game(player1, player2)
game.setup()

# Step 2: Start the game! Write game.play() below this line:


# Run the code with "python battleship/level-7.py" and battle!
# The game won't end yet — press Ctrl+C to stop it.

# One more level! Open level-8.py!
