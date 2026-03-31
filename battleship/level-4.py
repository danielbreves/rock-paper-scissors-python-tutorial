"""
Level 4! Time to learn debugging!

Every programmer makes mistakes — even the pros! The trick is knowing how to
find and fix them. In this level you'll learn to use the debugger, a tool
that lets you pause your code and look at what's happening step by step.
"""

# Here's a Battleship class, but it has a bug hiding in it!
# Try running it with "python battleship/level-4.py" first — you'll see something isn't right.
# Then scroll down for instructions on how to find and fix it using the debugger!

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


destroyer = Battleship()
destroyer.name = "Destroyer"
destroyer.positions = ["A1", "A2", "A3"]

# Bug: We expected this to print True, True, True — but one of the attacks is wrong!
print(destroyer.receive_attack("A1"))
print(destroyer.receive_attack("A2"))
print(destroyer.receive_attack("A4"))

# We expected this to print "sunk" — but it doesn't!
print("Status: " + destroyer.check_status())


# Step 1: Let's use the debugger to find the bug!
# Click on the red dot that appears next to the line number 42 where we call destroyer.receive_attack("A1").
# This is called a BREAKPOINT. It tells the debugger to pause here.

# Step 2: Click the play icon (the one with a bug on it) on the left sidebar (4th from the top),
# then click the green play button at the top (or try pressing F5). The code will pause at your breakpoint.
# Look at the left side panel — you should see the destroyer object. Click on it to see its properties.
# You can also mouse over variables in the code to see their values.

# Step 3: Press the "Step Over" button (it looks like an arrow curving over a dot) to run one line at a time.
# Watch how the property hits changes after each line runs. Can you spot which attack is wrong?
# If you miss it, you can always stop the debugger (click the red square icon), and click play again!

# Step 4: The status still says "afloat" even after 3 attacks. Run the debugger again, and
# once the code pauses on the line 47 where we call destroyer.check_status(),
# step into the method by clicking the "Step Into" button (it looks like an arrow pointing at a dot below it).
# Mouse over self.hits to check their values. Are they what you expect?

# Spoiler alert! The bug is on line 44, we meant to attack "A3" instead of "A4".
# A4 is not part of the destroyer's positions, so it doesn't get added to hits, and the status never changes to "sunk".
# Can you fix line 44 and run the code again to see if it works? You can remove the breakpoint by clicking on the red dot again.
# The terminal should print:
# True
# True
# True
# You sunk the Destroyer!
# Status: sunk

# Great detective work! Open level-5.py!
