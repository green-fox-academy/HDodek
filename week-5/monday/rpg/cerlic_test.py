import unittest
from cerlic import Cerlic

class TestCerlic(unittest.TestCase):
    def test_existance(self):
        cerlic = Cerlic("Test", 100, 10)

    def test_inheritance(self):
        cerlic = Cerlic("Test", 100, 10)
        self.assertEqual(cerlic. hp, 100)

    def test_healing(self):
        cerlic = Cerlic("Test", 100, 10)
        ally = Cerlic("Ally", 100, 10)
        cerlic.heal(ally)
        self.assertEqual(ally.hp, 110)




unittest.main()
