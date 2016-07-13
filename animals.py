from species import *
from movement import *

class Animal:
  def __init__(self, name, species):
    self.species = species
    self.name = name



class Betta(Animal, Swimming):
  def __init__(self, color, name):
    Animal.__init__(self, name, BettaTrifasciata(color)) ### you have to pass in self if you explicitly call the constructor function for Animal

