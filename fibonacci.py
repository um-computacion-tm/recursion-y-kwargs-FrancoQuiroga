import unittest

# En fibonacci vamos a sumar el resultado, con el valor anterior, para obtener el sig resultado
# Lista de fibonacci hasta 13 [0,1,1,2,3,5,8,13,21,34,55,89,144,233]
#                             [0,1,2,3,4,5,6, 7, 8, 9,10,11,12 ,13]
# se puede hacer mediante una lista, pero intento conseguirlo con un bucle for(sin listas):
    # En que contexto tengo que inicializar el bucle for? tengo que comenzar sabiendo que 0 y 1 ya están calculados
    # Lo que voy a hacer al principio  cada bucle, es sumar el numero anterior + actual
    # Después, tengo que actualizar el anterior con el resultado, para proseguir con el sig bucle
    # Faltaba una variable intermedia para cambiarle la paridad al cálculo, por eso es que lo unico que hacía era duplicar un 2



def fibonaccifor(posicion=int) -> int :
    actual = 1
    anterior = 0
    result = 0
    if posicion < 2:
        return posicion
    for _ in range(posicion - 1):
        result = actual + anterior
        anterior = actual
        actual = result
        
    return actual

def fibonacciwhile(posicion):
    resultado = 0
    anterior = 0
    actual = 1
    if posicion < 2:
         return posicion
    while posicion > 1:
         resultado = actual + anterior
         anterior = actual
         actual = resultado
         posicion -= 1
    return resultado

def fibonaccirecursivo(posicion):
    if posicion < 2:
         return 1
    return fibonaccirecursivo(posicion-1) + fibonaccirecursivo(posicion -2)
    
class TestsFibonacciFor(unittest.TestCase):
    
    def test_básico_fibonacci(self):
        posicionfibonacci = 1
        fibo = fibonaccifor(posicionfibonacci)
        self.assertEqual(1,fibo)

    def test_básico_fibonacci2(self):
        posicionfibonacci = 13
        fibo = fibonaccifor(posicionfibonacci)
        self.assertEqual(233,fibo)

class TestsFibonaccirecursivo(unittest.TestCase):
    def test_basico_en1(self):
        posicionfibo = 1
        fibo = fibonaccifor(posicionfibo)
        self.assertEqual(1,fibo)

    def test_basico_en5(self):
            posicionfibo = 5
            fibo = fibonaccifor(posicionfibo)
            self.assertEqual(5,fibo)

class TestsFibonacciwhile(unittest.TestCase):
        def test_basicoen1(self):
            pos = 1
            fibo = fibonacciwhile(pos)
            self.assertEqual(1,fibo)
        def test_básico_fibonacci2(self):
            posicionfibonacci = 13
            fibo = fibonacciwhile(posicionfibonacci)
            self.assertEqual(233,fibo)
unittest.main()