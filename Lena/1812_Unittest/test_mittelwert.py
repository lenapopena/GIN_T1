import unittest
from mittelwert import mittelwert_flexibel  # Importa la función principal

class TestMittelwertFlexibel(unittest.TestCase):
    # Testfall: Eingabe ist korrekt (normale Liste)
    def test_normale_liste(self):
        self.assertEqual(mittelwert_flexibel([2, 4, 6]), 4)
        self.assertAlmostEqual(mittelwert_flexibel([1.5, 2.5, 3.5]), 2.5, places=2)

    # Testfall: Leere Liste
    def test_leere_liste(self):
        with self.assertRaises(ValueError):
            mittelwert_flexibel([])

    # Testfall: Eingabe ist kein Liste
    def test_keine_liste(self):
        with self.assertRaises(TypeError):
            mittelwert_flexibel(123)

     # Testfall: Mixed numbers
    def test_mixed_numbers(self):
        self.assertEqual(mittelwert_flexibel([10, -10, 20, -20]), 0)
        self.assertEqual(mittelwert_flexibel([100, -50, 25, -75]), 0)       

    # Testfall: Elemente sind keine Zahlen
    def test_nicht_numerische_elemente(self):
        with self.assertRaises(TypeError):
            mittelwert_flexibel([1, "zwei", 3])

    # Testfall: Liste mit negativen Zahlen
    def test_negative_zahlen(self):
        self.assertEqual(mittelwert_flexibel([-2, -4, -6]), -4)

if __name__ == "__main__":
    unittest.main()
