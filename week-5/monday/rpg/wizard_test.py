import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard("Test", 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard("Test", 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard("Test", 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike(self):
        wizard = Wizard("Test", 40, 10, 20)
        opponent = Wizard("Opponent", 40, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 15)

    def test_no_manna(self):
        wizard = Wizard("Test", 40, 10, 0)
        opponent = Wizard("Opponent", 40, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 0)

    def test_more_than_5_manna(self):
        wizard = Wizard("Test", 40, 10, 20)
        opponent = Wizard("Opponent", 40, 10, 20)
        self.assertEqual(wizard.manna, 15)
        wizard.strike(opponent)
        sels.assertEqual(opponent.hp, 0)

    def test_strike_without_manna(self):
        wizard = Wizard("Test", 40, 5, 0)
        opponent = Wizard("Opponent", 40, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(opponent.hp, 27)




unittest.main()
