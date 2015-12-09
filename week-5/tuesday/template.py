class Weapon():
    def strike(self, warrior, opponent):
        opponent.hp -= self_damage
        self.hp = self.self_damage

    def damage(self):
        return "not implemented"

    def self_damage(self):
        return "not implemented"

class Sword(Weapon):
    def damage(self):
        return 10
    def self_damage(self):
        return 0

class Flamegun(Weapon):
    def damage(self):
        return 30
    def self_damage(self):
        return 10

class CriticalSword(Weapon):
    def damage(self):
        return 10 + random.rand(int(0, 10))
    def self_damage(self):
        return 0

class Enchanted(Weapon):
    def __init__(self, weapon):
    self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2

    def self_damage(self):
        return self.weapon.damage() / 2

class Warrior:
    def __init__(self, weapon):
        self.weapon = weapon
        self.hp = 100

    def strike(self, opponent):
        self.weapon.strike(self, opponent)

    def __repr__(self):
        return "Warrior.hp()", format(self, hp)

warrior = Warrior(Sword())
monster = Warrior(Flamegun())

warrior.strike(monster)
print(warrior)
print(monster)

monster.strike(warrior)
print(warrior)
print(monster)

warrior = Warrior(Enchanted(Sword()))
