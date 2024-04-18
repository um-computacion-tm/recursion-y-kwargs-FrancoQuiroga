import unittest
# Factorial consiste en multiplicar el número actual, por el numactual -1... hasta 1

def factorialfor(numero):
    resultado = 1
    for i in range(numero + 1):
        if i == 0:
            continue
        resultado *= i
    return resultado

def factorialwhile(numero):
    resultado = 1
    while numero > 1:
        resultado *= numero
        numero -= 1
    return resultado

def factorialrecursivo(numero):
    if numero < 2:
        return 1
    return numero * factorialrecursivo(numero-1)

class Testfactorialwhile(unittest.TestCase):
    def testfactbasico1y0(self):
        numero = 1
        factos = factorialwhile(numero)
        self.assertEqual(1, factos)

    def testfact5(self):
            numero = 5
            factos = factorialwhile(numero)
            self.assertEqual(120, factos)

    def testfact6(self):
        numero = 6
        factos = factorialwhile(numero)
        self.assertEqual(720, factos)

class Testfactorialfor(unittest.TestCase):
    def testfactbasico1y0(self):
        numero = 1
        factos = factorialfor(numero)
        self.assertEqual(1, factos)
    def testfactbasico5(self):
            numero = 5
            factos = factorialfor(numero)
            self.assertEqual(120, factos)

class Testfactorialrecursivo(unittest.TestCase):
    def testfactbasico1y0(self):
        numero = 1
        factos = factorialrecursivo(numero)
        self.assertEqual(1, factos)
    def testfactbasico5(self):
            numero = 5
            factos = factorialrecursivo(numero)
            self.assertEqual(120, factos)
unittest.main()