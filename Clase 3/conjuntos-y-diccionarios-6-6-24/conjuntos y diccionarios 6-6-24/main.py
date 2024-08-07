"""
Conjuntos: conjunto o set es una colección no ordenada de objetos únicos, es decir, no tiene elementos duplicados
"""

"""Reconocemos un conjunto por que está entre llaves y dentro no contienen una clave:valor
Y una particularidad de los set es que cada vez que se devuelven lo hacen de forma desordenada."""

conjunto_vacio = set()

# Conjunto de numeros
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto_numeros)
#Conjunto de string
conjunto_string = {"programacion", "python"}

"""Conjunto Heterogeneo que no puede incluir objetos mutables como listas, diccionarios, e incluso otros conjuntos o set."""
conjunto_heterogeneo = {42, "Hola mundo", 3.14159, True, None, [1, 2, 3]} 
print(conjunto_heterogeneo)

#De la misma forma podemos obtener un conjunto a partir de cualquier objeto iterable:
set1 = set([1, 2, 3, 4])
print(set1)
set2 = set(range(11))
print(set2)

#"que es un iterable?"
"""
Un objeto iterable en Python es aquel que puede ser recorrido elemento por elemento, uno a la vez. 
En otras palabras, es un objeto que se puede utilizar en un bucle
"""


# # Un set puede ser convertido a una lista y viceversa. En este último caso, los elementos duplicados son unificados.

mi_lista = list({1, 2, 3, 4})
lista = [1, 2, 3, 4]
mi_set = set(lista)
print(type(mi_set))

conjunto = {"a", "a", "b", "b", "c", "c", "d", "e", "f"}
#conjunto[:3] = ["A", "B", "C"]
print(conjunto)

#FUNCIONES EN CONJUNTOS
"""
La primera función de los conjuntos de la que estaremos hablando es ADD. Esta función permite agregar un nuevo ítem al set. La misma se escribe mi_conjunto.add(ítem_a_agregar)
"""
numeros =  {1,2,3,4}
numeros.add(5)

print(numeros)

#OPERACIONES ARITMETICAS CON ADD
numeros =  {1,2,3,4}
numeros.add(3*2)
print(numeros)
operacion = (3**2+1-12+5*3)
print(operacion)
numeros.add(3**2+1-12+5*3)
print(numeros)

#UPDATE
"""
Se pueden añadir multiples elementos
"""
# Creamos un conjunto inicial
frutas = {"manzana", "banana"}

# Creamos una lista con los elementos que queremos agregar
nuevas_frutas = ["pera", "uva", "naranja"]

# Usamos update() para agregar los elementos de la lista al conjunto
frutas.update(nuevas_frutas)

# Imprimimos el conjunto actualizado
print(frutas)  # Output: {'manzana', 'pera', 'naranja', 'banana', 'uva'}


#LONGITUD DE UN SET
# Creamos un conjunto con algunos colores
colores = {"rojo", "verde", "azul", "amarillo"}

# Usamos len() para obtener la cantidad de elementos del conjunto
cantidad_colores = len(colores)

# Imprimimos el resultado
print("El conjunto colores tiene", cantidad_colores, "elementos.")

#ELIMINAR UN ELEMENTO DEL SET
# Creamos un conjunto de números
numeros = {1, 2, 3, 4, 5}

# Eliminamos el número 3 del conjunto
numeros.discard(3)

# Intentamos eliminar el número 6 (que no existe en el conjunto)
numeros.discard("hola")  # No se produce ningún error

# Imprimimos el conjunto resultante
print(numeros)  # Output: {1, 2, 4, 5}


#USAMOS REMOVE, QUE A DIFERENCIA DE discard(), EN remove() SI UN ELEMENTO NO EXISTE, TIRA ERROR.
numeros = {1, 2, 3, 4, 5}

numeros.remove(3)  # Elimina el número 3 sin problemas
print(numeros)  # Output: {1, 2, 4, 5}

numeros.remove(6)  # KeyError: 6 (porque 6 no está en el conjunto)
print(numeros)



# VERIFICAR SI UN ELEMENTO PERTENECE A UN SET (in)
frutas = {"manzana", "pera"}

if "banana" in frutas:
    print("Sí, hay bananas en el conjunto.")
else:
    print("No hay bananas en el conjunto.")

frutas = {"manzana", "pera"}
elemento = "banana"

pertenece = elemento in frutas
print(pertenece)  # Output: True

# VACIAR UN CONJUNTO clear()
# Creamos un conjunto con algunos números
numeros = {1, 2, 3, 4, 5}

# Imprimimos el conjunto original
print("Conjunto original:", numeros)  

# Usamos clear() para eliminar todos los elementos
numeros.clear()

# Imprimimos el conjunto vacío
print("Conjunto después de clear():", numeros)  

"""comparando set y dict"""
conjunto = {"ale", "sosa"}
print(type(conjunto))

conjunto_2 = set()
print(type(conjunto_2))

"""
La función pop retorna un elemento en forma aleatoria (no podría ser de otra manera, ya que los elementos no están ordenados). Así, el siguiente bucle imprime y remueve uno por uno los miembros de un conjunto.

"""
numeros =  {1,2,3,4}
print(f"Así inicia el set: {numeros}")
while numeros:
    print("Se está borrando: ", numeros.pop())

print(f"Así quedó el set: {numeros}")


"""
Crear un conjunto en Python que posea los siguientes elementos: 

Colores: Rojo, Blanco, Azul.
Posteriormente, agrega nuestro set de colores, los valores de: Violeta y Dorado
Elimina a los colores: Celeste, Blanco y Dorado

"""
colores = {"rojo", "blanco", "azul"}

colores.update({"Violeta", "DORADO"})
print(colores)
colores.discard("celeste")
# colores.discard("blanco")
# colores.discard("DORADO")
# print(colores)

#VERSION 1
diccionario_vacio = dict()

#VERSION 2
diccionario_vacio2 = {}
print(type(diccionario_vacio2), type(diccionario_vacio))

"""
Para crear un diccionario se emplean llaves {}, y sus pares clave-valor se separan por comas. A su vez, intercalamos la clave del valor con dos puntos (:)
"""
persona = {"nombre": "Ana", "edad": 30,"ciudad": "Buenos Aires"}

#TRAYENDO UN VALOR DE UN DICCIONARIO (POR SU CLAVE)
nombre = persona["nombre"]
edad = persona["edad"]
ciudad = persona["ciudad"]




print(nombre)


#MUTABILIDAD DE DICCIONARIOS
colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
colores["amarillo"] = "white"

print(colores)

#ASIGNACION
edades = {"Juan": 26, "Esteban": 35, "Maria": 29}
print(edades)
edades["Juan"] += 5
print(edades)



# AGREGANDO ELEMENTOS
numeros = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
numeros['cinco'] = 5  #OUTPUT: {"uno": 1, "dos": 2, "“tres”": 3, "“cuatro”": 4, "cinco": 5}

# FUNCIONES DE DICCIONARIOS no tiene una funcion add
mi_diccionario = {}  # Diccionario vacío
mi_diccionario["clave"] = "valor"  # Agrega un par clave-valor

print(mi_diccionario)
#UPDATE ACTUALIZA UN DICCIONARIO AGREGANDO PARES CLAVE:VALOR
mi_diccionario = {"a": 1, "b": 2}
print(mi_diccionario)
mi_diccionario.update({"c": 3, "d": 4})  # Agrega varios pares clave-valor a la vez
print(mi_diccionario)
# También puedes usar una lista de tuplas:
mi_diccionario.update([("e", 5), ("f", 6)])
print(mi_diccionario)

# LONGITUD DE UN DICCIONARIO
# Creamos un diccionario con información de una persona
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Buenos Aires"}

# Usamos len() para obtener la cantidad de elementos del diccionario
cantidad_elementos = len(persona)

# ELIMINANDO ITEMS DEL DICT SIN MODIFICARLO Y SI EL ELEMENTO PASADO EN del() no existe, tira error KeyError
mi_dict = {"a": 1, "b": 2}
del mi_dict["c"]  # KeyError: 'c'


#BUSCANDO ELEMENTOS EN EL DICT (in)
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}

if "edad" in persona:
    print("La clave 'edad' existe en el diccionario.")

else:
    print("La clave 'edad' no existe en el diccionario.")

#BORRANDO TODOS ELEMENTOS DE UN DICT
mi_dict = {"a": 1, "b": 2, "c": 3}
print("Diccionario original:", mi_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
mi_dict.clear()
print("Diccionario después de clear():", mi_dict)  # Output: {}

# TODO: ACTIVIDAD EN CLASE
ganadores_mundial = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "España",
    2014: "Alemania",
     2018: "Francia"
 }

# print("Ganadores de la Copa Mundial de la FIFA (1990-2018):")
# for año, pais in ganadores_mundial.items():
#     print(f"{año}: {pais}")

ganadores_mundial = {
    1990: 'Alemania',
    1994: 'Brasil',
    1998: 'Francia',
    2002: 'Brasil',
    2006: 'Italia',
    2010: 'España',
    2014: 'Alemania',
    2018: 'Francia'
}

print(ganadores_mundial)


"""
Crear un conjunto en Python que posea los siguientes elementos:
Países: Inglaterra, USA, México.
Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA
Elimina a los países: Chile e Italia
"""

paises = {"Inglaterra", "USA", "Mexico"}
print(paises)
paises.update({"Islandia", "Italia", "Argentina" , "Portugal", "USA"})
print(paises)
paises.discard("chile")
paises.discard("Italia")

print(paises)