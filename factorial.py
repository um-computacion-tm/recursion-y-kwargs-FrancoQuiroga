import unittest
# Factorial consiste en multiplicar el número actual, por el numactual -1... hasta 1

def factorialFor(numero):
    resultado = 1
    for i in range(numero + 1):
        if i == 0:
            continue
        resultado *= i
    return resultado

def factorialWhile(numero):
    resultado = 1
    while numero > 1:
        resultado *= numero
        numero -= 1
    return resultado

def factorialRecursivo(numero):
    if numero < 2:
        return 1
    return numero * factorialRecursivo(numero-1)

class Testfactorialwhile(unittest.TestCase):
    def testfactbasico1y0(self):
        numero = 1
        factos = factorialWhile(numero)
        self.assertEqual(1, factos)

    def testfact5(self):
            numero = 5
            factos = factorialWhile(numero)
            self.assertEqual(120, factos)

    def testfact6(self):
        numero = 6
        factos = factorialWhile(numero)
        self.assertEqual(720, factos)

class Testfactorialfor(unittest.TestCase):
    def testfactbasico1y0(self):
        numero = 1
        factos = factorialFor(numero)
        self.assertEqual(1, factos)
    def testfactbasico5(self):
            numero = 5
            factos = factorialFor(numero)
            self.assertEqual(120, factos)

class Testfactorialrecursivo(unittest.TestCase):
    def testfactbasico1y0(self):
        numero = 1
        factos = factorialRecursivo(numero)
        self.assertEqual(1, factos)
    def testfactbasico5(self):
            numero = 5
            factos = factorialRecursivo(numero)
            self.assertEqual(120, factos)
unittest.main()