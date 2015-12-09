from character import Character

class Cerlic(Character):

    def heal(self, ally):
        ally.hp += 10
