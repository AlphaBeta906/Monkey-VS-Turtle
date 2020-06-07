# Imports
from random import choice
from Character import Character

#Variables
monkeyItemsDefault = \
    {
        "monkey chow": ["+ 26 HP\n+ 5 ATK\n+ 5 DEF", 1, 26, 5, 5, "all", "all"],
        "banana": ["+ 15 HP\n+ 3 ATK\n+ 6 DEF for 3 moves", 1, 15, 3, 6, "all", 3],
        "lettuce": ["+ 15 HP\n+ 6 ATK for 3 moves\n+ 3 DEF", 2, 3, 4, 4, 3, "all"]
    } # Items dict template: "item":[description, amount, +hp, +atk, +def, movesforatk, movesfordef]

turtleItemsDefault = \
    {
        "turtle pellet": ["+ 26 HP\n + 5 ATK + 5 DEF", 1, 26, 5, 5, "all", "all"],
        "apple": ["+ 15 HP\n + 3 ATK\n 6 DEF for 3 moves", 1, 15, 3, 6, "all", 3],
        "lettuce": ["+ 15 HP\n+ 6 ATK for 3 moves\n+ 3 DEF", 2, 3, 4, 4, 3, "all"]
    }

turns = 0
whoseTurn = 1
# Functions
def introduction():
    print("""Welcome to Monkey VS Turtle!
    This is a Pokemon-based multiplayer fighting game!
    You can either play as a monkey or a turtle.
    The monkey deals more damage, but the turtle is more defensive.
    
    How to play:
    Both players can do 4 things: Attack, Defend, Use a food item, or surrender
    When defending, the player's defense temporarily increases for the turn.
    
    To win, you have to take down your opponent's health to 0.
    
    There must only be one monkey and only one turtle.""")

# Main code
introduction()
p1Character = input(
    "\nSelect character for player 1(M for monkey, T for turtle, default is M): ").upper()
print("-" * 23)
if p1Character.upper() != "T":
    p1Character = Character(monkeyItemsDefault, 15, 6, "M")
    p2Character = Character(turtleItemsDefault, 10, 8, "T")
else:
    p1Character = Character(turtleItemsDefault, 10, 8, "T")
    p2Character = Character(monkeyItemsDefault, 15, 6, "M")

print("Player 1: %s\nPlayer 2: %s" % (p1Character.characterType, p2Character.characterType))

while p1Character.hp >= 1 and p2Character.hp >= 1:
    turns += 1
    turn = 1 if turns % 2 != 0 else 2

    print("%s\nCurrent stats:\nP1 HP: %s\nP2 HP: %s\n" % ("-" * 23, p1Character.hp, p2Character.hp))
    action = input("Player %s, what do you do?\nA: Attack\nD: Defend\nI: Use an item\nS: Surrender\n> " % turn)

    if action == "A":
        if turn == 1:
            if p2Character.isUsingDefend:
                if p1Character.atk <= p2Character.defense + 3:
                    p2Character.swapDefend()
                    print("No damage was dealt! Player 2's DEF is too big!\nPlayer 2 is not defending now!")

                else:
                    p1Character.attack(p2Character)
                    print("Player 1 dealt %s damage! Player 2 is now at %s health." % (p1Character.atk - p2Character.defense + 3, p2Character.hp))

            else:
                if p1Character.atk <= p2Character.defense:
                    print("No damage was dealt! Player 2's DEF is too big!")

                else:
                    p1Character.attack(p2Character)
                    print("Player 1 dealt %s damage! Player 2 is now at %s health." % (p1Character.atk - p2Character.defense, p2Character.hp))

        elif turn == 2:
            if p1Character.isUsingDefend:
                if p2Character.atk <= p1Character.defense + 3:
                    print("No damage was dealt! Player 1's DEF is too big!\nPlayer 1 is not defending now!")
                    p1Character.swapDefend()

                else:
                    p2Character.attack(p1Character)
                    print("Player 2 dealt %s damage! Player 1 is now at %s health." % (p2Character.atk - p1Character.defense + 3, p1Character.hp))

            else:
                if p2Character.atk <= p1Character.defense:
                    print("No damage was dealt! Player 1's DEF is too big!")

                else:
                    p2Character.attack(p1Character)
                    print("Player 2 dealt %s damage! Player 1 is now at %s health." % (p2Character.atk - p1Character.defense, p1Character.hp))

    elif action == "D":
        if turn == 1:
            if p1Character.isUsingDefend:
                print("Too bad! Player 1 is already defending!")

            else:
                print("Player 1 defends!")
                p1Character.swapDefend()

        elif turn == 2:
            if p2Character.isUsingDefend:
                print("Too bad! PLayer 2 is already defending!")

            else:
                print("Player 2 defends!")
                p2Character.swapDefend()

    elif action == "I":
        if turn == 1:
            p1Character.item()

        elif turn == 2:
            p2Character.item()

    elif action == "S":
        if turn == 1:
            p1Character.surrender()

        elif turn == 2:
            p2Character.surrender()

#When loop is broken
if p1Character.hp <= 0:
    print("Player 2 wins! Congratulations!")

elif p2Character.hp <= 0:
    print("PLayer 1 wins! Congratulations!")