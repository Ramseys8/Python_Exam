import unittest
import sys
import os

# Etant donné que les exercices sont dans un autre dossier, on doit ajouter le chemin du dossier pour que Python puisse le trouver.
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Exercices"))

# On import donc la fonction de notre fichier Exercice_1 afin d'effectuer des tests unitaires.
from Exercice_1 import multiple_3_5

# On crée une classe étendant la classe unittest.TestCase
class TestMultiple35Function(unittest.TestCase):
    # On crée une fonction qui va tester notre autre fonction multiple_3_5, elle prends self en paramètre ce qui permettra
    # de tester plusieurs cas de figure.
    def test_multiple_3_5(self):
        # On teste avec Nb_max = 1000, le résultat doit être 233168
        self.assertEqual(multiple_3_5(1000), 233168)
        
        # On teste avec Nb_max = 1000, on test si un autre résultat que 233168 ne peut être accepté.
        self.assertNotEqual(multiple_3_5(1000), 233167)

        # On teste avec Nb_max = 37, le résultat doit être 329
        self.assertEqual(multiple_3_5(37), 329)

        # On teste avec Nb_max = 0, le résultat doit être 0
        self.assertEqual(multiple_3_5(0), 0)

        # On teste avec Nb_max = 50, le résultat doit être 543
        self.assertEqual(multiple_3_5(50), 543)

if __name__ == '__main__':
    unittest.main()
