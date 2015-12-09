class Game_Character():
    def __init__(self, name, health_potions, damage):
        self.name = name
        self.health_potions = health_potions
        self.damage = damage

    def print_status(self):
        if self.health_potions <= 0:
            print(self.name + " " + "is dead!")
        elif self.health_potions > 0:
            print(self.name + " "  "HP " + str(self.health_potions))

    def drink_potion(self):
        self.health_potions += 10

    def strike(self, other):
        other.health_potions -= self.damage

class Wizard(Game_Character):
    def heal(self, ally):
        ally.health_potions += 10

alena =  Game_Character("Alena", 100, 50)
bergu = Game_Character("Bergu", 65, 150)
melkor = Wizard("Melkor", 60, 60)

alena.print_status()
for i in range(2):
    bergu.strike(alena)
    melkor.heal(alena)
alena.print_status()
