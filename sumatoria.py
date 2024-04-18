import unittest

def sumatoriawhile(value):
    resultado = 0
    while value > 0:
        resultado += value
        value -= 1
    return resultado

def sumatoriarecursive(numero):
    return numero + sumatoriarecursive(numero - 1)

class TestSumatoriaRecursive(unittest.TestCase):
    def test_basico1(self):
        numero = 4
        totalsum = sumatoriarecursive(numero)
        self.assertEqual(totalsum, 10)
class TestSumatoriawhile(unittest.TestCase):
    def test_bás(self):
        numero = 4
        totalsum = sumatoriawhile(numero)
        self.assertEqual(totalsum, 10)

    def test_bás2(self):
        numero = 6
        totalsum = sumatoriawhile(numero)
        self.assertEqual(totalsum, 21)
     

unittest.main()