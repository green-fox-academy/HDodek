class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companion.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)

    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companion:
            companion.notify("damage", self)

    def heal(self):
        self.hp = hp

    def cursed(self, opponent):
        opponent.join(Cursed())

class Healer:
    def __notify__(self, type, warrior):
        if type == "damage":
            warrior.heal(10)

class Cursed:
    def __notify__(self, type, warrior):
        if type == "cursed"
        warrior.heal(-10)

rabbit = Warrior()
wolf = Warrior()
shaman = Healer()

rabbit.join(shaman)

wolf.strike(rabbit)
print(rabbit, hp)
