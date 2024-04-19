import unittest
"""Supongamos que tenemos una base de datos de personas, por ejemplo:
Construir una funcion que permita recibir los nombres y apellidos de una persona, 
para verificar si se encuentra en la base de datos. 
La función debería retornar el "id" o la key del diccionario que contiene a una persona 
con todos los nombres y apellidos pasados como parametros a la funcion buscar_datos()
Ejemplo:
Si busco una persona cuyo nombre sea "Pablo Diego Ruiz Picasso", entonces, la llamada a la función será:
buscar_datos("Pablo", "Diego","Ruiz","Picasso", **database)
Donde cada uno de los primeros argumetos serán los nombres 
y apellidos (no necesariamente ordenados) y el último parametro, indicado con
asteriscos, sería la base de datos.
En base a esta llamada a la función, se debería retornar 
el valor de la key del diccionario que contiene los valores "Pablo, Diego, Ruiz, Picasso"
buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database) -> 1
Donde 1 es la key que identifica al diccionario correspondiente 
que contiene todos esos valores (ni mas ni menos)"""
database = {
            '1':{"nombre1":"Pablo","nombre2":"Diego", "apellido1":"Ruiz","apellido2":"Picasso"},
            '2':{"nombre1":"Elio", "apellido1":"Anci"},
            '3':{"nombre1":"Elias", "nombre2":"Marcos", "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"}}
# La función devolverá False, en caso de no encontrar a la persona,
#o un int(key del dict) en caso de encontrarla
# La función consiste en 3 etapas, primero hay que desempaquetar los datos
# Despues hay que interpretarlos, y por último, devolver un resultado
def buscar_datos(*args:str, **kwargs:dict): 
    id_list = []
    datadict_list = []
    comparison_list = []
    print(kwargs)
# Desempaquetar
    for id,data in kwargs.items:
        id_list.append(id)
        datadict_list.append(data)
# Analizar
    for argument in args:
        comparison_list.append(argument)
# Retornar
    for dictionary in datadict_list:
        if comparison_list == dictionary.values():
            return id_list[dictionary.index()]
    return False

class Testdebuscardatos(unittest.TestCase):
    def testbasicodesetup(self):
        personaobj = buscar_datos('Juancito', kwargs=database)
        self.assertEqual(personaobj, False)
    #def test
unittest.main()