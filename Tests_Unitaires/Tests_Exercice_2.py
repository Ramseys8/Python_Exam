import unittest
import sys
import os

# Etant donné que les exercices sont dans un autre dossier, on doit ajouter le chemin du dossier pour que Python puisse le trouver.
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Exercices"))

# On import donc la fonction de notre fichier Exercice_1 afin d'effectuer des tests unitaires.
from Exercice_2 import counting_vowel

# On crée une classe étendant la classe unittest.TestCase
class TestCountingVowelFunction(unittest.TestCase):

    def test_counting_vowel(self):
        self.assertEqual(counting_vowel("BonJOUR"), 3)
        
        self.assertEqual(counting_vowel("Salut ça va ?"), 4)

        self.assertEqual(counting_vowel("Uluberlu orthodoxe"), 8)


if __name__ == '__main__':
    unittest.main()

