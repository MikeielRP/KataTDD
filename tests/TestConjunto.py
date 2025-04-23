import unittest
from src.logica.Conjunto import conjunto

class testConjunto(unittest.TestCase):
    def test_conjunto_vacio_returnNone(self):
        Conjunto=conjunto([])
        self.assertIsNone(Conjunto.promedio())
    def test_unicoelemento(self):
        Conjunto=conjunto([5])
        self.assertEqual(5,Conjunto.promedio())
    def test_retornaPromedio(self):
        Conjunto= conjunto([5, 7])
        self.assertEqual(6, Conjunto.promedio())



if __name__ == '__main__':
    unittest.main()

