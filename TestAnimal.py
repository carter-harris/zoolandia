import unittest
from zoolandia import *


class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_animal_creation(self):
    bob = Betta('orange', 'Bob')
    self.assertIsInstance(bob, Swimming)

    self.assertEqual(bob.species.color, 'orange')
    self.assertEqual(bob.name, 'Bob')
    self.assertIsInstance(bob, Animal)
    self.assertIsInstance(bob.species, Species)
    self.assertIsInstance(bob.species, BettaTrifasciata)

if __name__ == '__main__':
    unittest.main()
