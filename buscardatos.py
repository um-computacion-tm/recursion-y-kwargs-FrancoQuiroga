import unittest
database = {
            '1':{"nombre1":"Pablo","nombre2":"Diego", "apellido1":"Ruiz","apellido2":"Picasso"},
            '2':{"nombre1":"Elio", "apellido1":"Anci"},
            '3':{"nombre1":"Elias", "nombre2":"Marcos", "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"}}
# La función devolverá False, en caso de no encontrar a la persona, o un int(key del dict) en caso de encontrarla
# La función consiste en 3 etapas, primero hay que desempaquetar los datos Despues hay que interpretarlos, y por último, devolver un resultado
def buscar_datos(*args:str, **kwargs:dict): 
    id_list = []
    datadict_list = []
    comparison_list = []
# Desempaquetar
    for id,data in kwargs.items():
        id_list.append(id)
        datadict_list.append(data)
# Analizar
    for argument in args:
        comparison_list.append(argument)
# Retornar
    dictcounter = 0
    for dictionary in datadict_list:
#       dictionary.items(): # Mi problema es que estoy comparando una lista con un dictionario
        if comparison_list == list(dictionary.values()):
            #return int(id_list[dictcounter]) Esta línea es por si necesitamos que el return sea un int
            return id_list[dictcounter] #Esta línea devuelve un str
        dictcounter += 1
    return False

class Testdebuscardatos(unittest.TestCase):
    def testbasicodesetup(self):
        personaobj = buscar_datos('Juancito', **database)
        self.assertEqual(personaobj, False)
    def testconnombreyapellido(self):
        personaobj = buscar_datos('Elio', 'Anci', **database)
        self.assertEqual(personaobj, '2')
    def testconnombreyapellidodefinitivo(self):
        personaobj = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(personaobj, '1')
unittest.main()