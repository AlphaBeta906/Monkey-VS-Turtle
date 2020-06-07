class Character:
    def __init__(self, items, attack, defense, characterType):
        self.hp = 100
        self.isUsingDefend = False
        self.atk = attack
        self.defense = defense
        self.items = items
        self.characterType = characterType

    def attack(self, enemy):
        if enemy.isUsingDefend:
            if not self.atk - enemy.defense + 3 <= 0:
                enemy.hp -= self.atk - enemy.defense

            enemy.swapDefend()
        else:
            if not self.atk - enemy.defense <= 0:
                enemy.hp -= self.atk - enemy.defense

    def swapDefend(self):
        if self.isUsingDefend:
            self.defense -= 3
            self.isUsingDefend = False

        else:
            self.defense += 3
            self.isUsingDefend = True

    def item(self):
        for i in range(len(self.items)):
            key = list(self.items.keys())[i]
            if self.items[key][1] == 0:
                pass

            else:
                print("%s x%s: \n%s\n" % (key.capitalize(), self.items[key][1], self.items[key][0]))

    def surrender(self):
        self.hp = 0