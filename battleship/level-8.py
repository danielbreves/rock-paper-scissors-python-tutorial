"""
The final level! You've come a long way!

The game works, but it never ends! We need to check if all of a player's
ships have been sunk after each attack. When that happens, the attacker wins!

We'll also check if a player has already attacked a position so they
don't waste a turn.
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

    # Step 1: Add a method that checks if a player has lost.
    # A player loses when all their ships are sunk.
    # We check each ship — if we find one that's still afloat, they haven't lost yet.
    # Write the following below this line:
    # def check_loser(self):
    #     for player in [self.player1, self.player2]:
    #         all_sunk = True
    #         for ship in player.ships:
    #             if ship.status != "sunk":
    #                 all_sunk = False
    #         if all_sunk:
    #             return player
    #     return None



    def play(self):
        current_player = self.player1
        next_player = self.player2

        while True:
            position = input(current_player.name + "'s turn! Which position do you want to attack? ")

            # Step 2: Check if the player already attacked this position.
            # Write the following below this line:
            # if position in current_player.attacks:
            #     print("You already attacked " + position + "! Try a different position.")
            #     continue



            result = current_player.attack(next_player, position)
            print(position + " is a " + result + "!")
            print("Your attacks: " + str(current_player.attacks))

            # Step 3: Check if the game is over. Write the following below this line:
            # loser = self.check_loser()
            # if loser:
            #     print(current_player.name + " wins!")
            #     break



            # Swap turns
            previous_player = current_player
            current_player = next_player
            next_player = previous_player


player1 = Player()
player1.name = "Player 1"
player2 = Player()
player2.name = "Player 2"

game = Game(player1, player2)
game.setup()
game.play()

# Run the code with "python battleship/level-8.py" and play until someone wins!

# When you're done, open level-9.py for some bonus ideas!
