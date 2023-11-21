import unittest
import sys
import os

# Etant donné que les exercices sont dans un autre dossier, on doit ajouter le chemin du dossier pour que Python puisse le trouver.
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Exercices"))

# On import donc la fonction de notre fichier Exercice_1 afin d'effectuer des tests unitaires.
from Exercice_3 import is_prime_number

# On crée une classe étendant la classe unittest.TestCase
class TestCountingVowelFunction(unittest.TestCase):

    def test_is_prime_number(self):
        self.assertEqual(is_prime_number(2), True)
        
        self.assertEqual(is_prime_number(7), True)

        self.assertEqual(is_prime_number(15), False)
        
        self.assertEqual(is_prime_number(43), True)


if __name__ == '__main__':
    unittest.main()


