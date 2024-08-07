"""
DIFERENTES FORMAS DE CONVERTIR A MAYUSCULAS Y MINUSCULAS
"""
#! METODO UPPER(MAYUSCULAS) Y LOWER(minusculas)
#! IMPRIMO DIRECTAMENTE EN UN PRINT
texto = "HOLA MUNDO"
print(texto.lower())  # Imprime "hola mundo"
texto = "hola mundo"
print(texto.upper())  #Imprime "HOLA MUNDO"

#! IMPRIMO LA VARIABLE QUE CONTIENE LA CONVERSION
nombre = "Juan Pérez"
nombre_minusculas = nombre.lower()
print(nombre_minusculas)  # Imprime "juan pérez"
nombre_mayusculas = nombre.upper()
print(nombre_mayusculas)  # Imprime "JUAN PEREZ"

#! CONVIRTIENDO DESDE LA SOLICITUD DE USUARIO
nombre = input("Ingrese un nombre: ").lower()
print(nombre)  #Imprime lo que pone el usuario en minuscula
nombre = input("Ingrese otro nombre: ").upper()
print(nombre)  #Imprime lo que pone el usuaro en mayuscula

"""
HINT: Ver mas ejemplos en ejemplos_upper.py y en ejemplos_lower.py
"""

#TODO:#############################################################################################
#!METODO CAPITALIZE 
#FORMATEANDO NOMBRE
nombre = "ana maría"
nombre_formateado = nombre.capitalize()  # Convierte a "Ana maría"
print(nombre_formateado)

#!CORRIGIENDO ERRORES TIPOGRAFICOS
texto = "eSTE ES UN eJEMPLO"
texto_corregido = texto.capitalize()  # Convierte a "Este es un ejemplo"
print(texto_corregido)

#TODO:##############################################################################################
#!METODO TITTLE
#!FORMATEO DE NOMBRES
nombre = "ana maría lópez"
nombre_formateado = nombre.title()  # Convierte a "Ana María López"
print(nombre_formateado)

#!FORMATEO DE CIUDADES
ciudad = "nueva york"
ciudad_formateada = ciudad.title()  # Convierte a "Nueva York"
print(ciudad_formateada)

#TODO:##############################################################################################
#!METODO COUNT
#!CONTAR PALABRAS EN UN TEXTO
texto = "Este es un ejemplo de texto con palabras repetidas como ejemplo"
palabra = "ejemplo"
cantidad = texto.count(palabra)
print(f"La palabra '{palabra}' aparece {cantidad} veces en el texto.")

#!CONTANDO ESPECIFICAMENTE LA APARICION DE ALGO ESPECIFICO
frase = "Python es un lenguaje de programación divertido"
caracter = "o"
cantidad_caracteres = frase.count(caracter)
print(f"El carácter '{caracter}' aparece {cantidad_caracteres} veces en la frase.")

#!BUSCANDO EN UNA SECUENCIA UN PATRON ESPECIFICO
secuencia = "ABABACABAB"
patron = "AB"
cantidad_patrones = secuencia.count(patron)
print(f"El patrón '{patron}' aparece {cantidad_patrones} veces en la secuencia.")

#? HINT: MOSTRAR PROGRAMA EN ejemplos_count.py

#TODO:##############################################################################################
#!METODO FIND
#!ENCONTRAR LA POSICION DE UNA PALABRA EN UNA FRASE
frase = "Python es un lenguaje de programación"
palabra = "lenguaje"
indice = frase.find(palabra)
if indice != -1:
    print(f"La palabra '{palabra}' se encuentra en la posición {indice}.")
else:
    print(f"La palabra '{palabra}' no se encuentra en la frase.")

#!ENCUENTRA LA PRIMERA APARICION DE UN CARACTER
email = "ejemplo@correo.com"
indice_arroba = email.find("@")
if indice_arroba != -1:
    print(f"El símbolo '@' se encuentra en la posición {indice_arroba}.")

#?Hint: Mostrar como se imprime una documentación de una funcion encontrar_arroba().
#?Hint2: Ejemplo de find formateado

#TODO:##############################################################################################
#!METODO RFIND
#!ULTIMA POSICION DE UNA PALABRA EN UNA CADENA
frase = "Python es un lenguaje de programación Python"
palabra = "Python"
indice = frase.rfind(palabra)
if indice != -1:
    print(f"La última ocurrencia de '{palabra}' está en la posición {indice}.")
else:
    print(f"La palabra '{palabra}' no se encuentra en la frase.")  


#!BUSCAR LA POSICION DE LA ULTIMA ETIQUETA DE CIERRE
html = "<div><p>Hola</p></div>"
indice_cierre_div = html.rfind("</div>")
if indice_cierre_div != -1:
    print(f"La etiqueta de cierre </div> se encuentra en la posición {indice_cierre_div}.")

#TODO:##############################################################################################
#!METODO SPLIT HINT: DEVUELVE SIEMPRE UNA LISTA
#!DIVIDIENDO UNA CADENA EN PALABRAS
frase = "Este es un ejemplo de frase"
palabras = frase.split()  # Separa por espacios por defecto
print(palabras)  # Output: ['Este', 'es', 'un', 'ejemplo', 'de', 'frase']

#!DIVIDIR UNA CADENA DE ELEMENTOS SEPARADOS POR COMAS
elementos = "manzana,pera,uva"
lista_frutas = elementos.split(",")  # Separa por comas
print(lista_frutas)  # Output: ['manzana', 'pera', 'uva']

#!DIVIDIR UNA CADENA EN UN NUMERO LIMITADO DE PARTES
datos = "nombre:edad:ciudad:parque:zona:palo:pala:carta"
informacion = datos.split(":", 2)  # Separa por dos puntos, máximo 2 divisiones
print(informacion)  # Output: ['nombre', 'edad', 'ciudad']

#!SEPARA POR PUNTOS
ip = "192.168.1.100"
octetos = ip.split(".")  # Separa por puntos
print(octetos)  # Output: ['192', '168', '1', '100']

#TODO:##############################################################################################
#!METODO JOIN
#!UNIENDO PALABRAS
palabras = ["Hola", "mundo", "!"]
frase = " ".join(palabras)  # Une las palabras con espacios
print(frase)  # Output: "Hola mundo !"

#!FORMATEANDO NUMEROS DE TELEFONO
digitos = ["123", "456", "7890"]
numero_telefono = "-".join(digitos)  # Une los dígitos con guiones
print(numero_telefono)  # Output: "123-456-7890"

#TODO:##############################################################################################
#!METODO STRIP
texto = "   Hola, mundo!   "
texto_limpio = texto.strip()  # Elimina espacios en blanco al inicio y al final
print(texto_limpio)  # Output: "Hola, mundo!"

#!ELIMINANDO CARACTERES ESPECIFICOS
cadena = "***Python es genial***"
cadena_limpia = cadena.strip("*")  # Elimina asteriscos al inicio y al final
print(cadena_limpia)  # Output: "Python es genial"

#!ELIMINANDO CARACTERES MULTIPLES
texto = "!!!Hola, mundo!!!???"
texto_limpio = texto.strip("!?")  # Elimina signos de exclamación e interrogación al inicio y al final
print(texto_limpio)  # Output: "Hola, mundo"


#!ELIMINANDO TABULACIONES Y SALTOS DE LINEA (SON ESPACIOS)
texto_con_espacios = "\n\tEste texto tiene espacios en blanco.\n\t"
texto_limpio = texto_con_espacios.strip()  # Elimina espacios en blanco, saltos de línea y tabulaciones
print(texto_limpio)  # Output: "Este texto tiene espacios en blanco."


#TODO: ################################################################################
#!METODO REPLACE
texto = "El perro juega con el gato."
nuevo_texto = texto.replace("perro", "gato")  # Reemplaza todas las ocurrencias de "perro" por "gato"
print(nuevo_texto)  # Output: "El gato juega con el gato."

#!REEMPLAZANDO MULTIPLES CARACTERES
cadena = "abc123def456"
nueva_cadena = cadena.replace("123", "xyz").replace("456", "789")  # Reemplaza "123" por "xyz" y "456" por "789"
print(nueva_cadena)  # Output: "abcxyzdef789"

#!REEMPLAZANDO UN NUMERO LIMITADO DE APARICIONES
texto = "El perro persigue al gato. El gato persigue al perro."
nuevo_texto = texto.replace("perro", "gato", 1)  # Reemplaza solo la primera ocurrencia de "perro"
print(nuevo_texto)  # Output: "El gato persigue al gato. El gato persigue al perro."


#!ELIMINAR CARACTERES DE UNA CADENA
cadena = "Esto es una cadena con espacios extra   ."
cadena_sin_espacios = cadena.replace(" ", "")  # Reemplaza espacios en blanco por una cadena vacía
print(cadena_sin_espacios)  # Output: "Estoesunacadenaconespaciosextra."

#TODO: ################################################################################
#!METODOS DE LISTAS EXTENDED
#!COMBINAR LISTAS

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)  # Extiende lista1 con los elementos de lista2
print(lista1)  # Output: [1, 2, 3, 4, 5, 6]


#!AGREGAR ELEMENTOS DE UNA TUPLA A UNA LISTA
frutas = ["manzana", "banana"]
citricos = ("naranja", "limón")
frutas.extend(citricos)  # Extiende la lista frutas con los elementos de la tupla citricos
print(frutas)  # Output: ['manzana', 'banana', 'naranja', 'limón']

#TODO: ################################################################################

#!METODO INSERT
#!INSERTAR UN ELEMENTO AL PRINCIPIO DE LA LISTA
numeros = [2, 3, 4]
numeros.insert(0, 1)  # Inserta el número 1 en la posición 0
print(numeros)  # Output: [1, 2, 3, 4]

#!INSERTAR ELEMENTOS A UNA LISTA VACIA
lista_vacia = []
lista_vacia.insert(0, "primer elemento")  # Inserta el primer elemento en la posición 0
print(lista_vacia)  # Output: ['primer elemento']

# #TODO: ################################################################################

#!METODO REVERSE
#!INVERTIR UNA LISTA DE NUMEROS
numeros = [1, 2, 3, 4, 5]
numeros.reverse()  # Invierte el orden de los elementos en la lista
print(numeros)  # Output: [5, 4, 3, 2, 1]


#!INVERTIR UNA LISTA DE CADENAS
palabras = ["Hola", "mundo", "!"]
palabras.reverse()
print(palabras)  # Output: ['!', 'mundo', 'Hola']

# #TODO: ################################################################################

#!METODO SORT
#!ORDENAR UNA LISTA DE NUMEROS DE MENOR A MAYOR
numeros = [5, 2, 8, 1, 9]
numeros.sort()  # Ordena la lista de menor a mayor (modifica la lista original)
print(numeros)  # Output: [1, 2, 5, 8, 9]


#!ORDENAR UNA LISTA DE NUMEROS DE MAYOR A MENOR
numeros = [5, 2, 8, 1, 9]
numeros.sort(reverse=True)  # Ordena la lista de mayor a menor
print(numeros)  # Output: [9, 8, 5, 2, 1]


#!ORDENAR UNA CADENA ALFABETICAMENTE
palabras = ["Hola", "mundo", "Python", "es", "genial"]
palabras.sort()  # Ordena la lista alfabéticamente (modifica la lista original)
print(palabras)  # Output: ['Hola', 'Python', 'es', 'genial', 'mundo']

# #TODO: ################################################################################

#!METODOS DE CONJUNTOS
#!CREAR UNA COPIA DE UN CONJUNTO
numeros = {1, 2, 3, 4, 5}
numeros_copia = numeros.copy()  # Crea una copia del conjunto
print(numeros_copia)  # Output: {1, 2, 3, 4, 5}

#!MODIFICAR LA COPIA SIN AFECTAR EL ORIGINAL
numeros = {1, 2, 3, 4, 5}
numeros_copia = numeros.copy()
numeros_copia.add(6)  # Agrega un elemento a la copia
print(numeros)  # Output: {1, 2, 3, 4, 5} (el conjunto original no cambia)
print(numeros_copia)  # Output: {1, 2, 3, 4, 5, 6}


#TODO: ################################################################################
#!METODO ISDISJOINT
#!CONJUNTOS SIN ELEMENTOS EN COMUN
set1 = {1, 2}
set2 = {3, 4}
resultado = set1.isdisjoint(set2)
print(resultado)  # Output: True (los conjuntos no tienen elementos en común)

#!CONJUNTOS CON ELEMENTOS EN COMUN
set1 = {1, 2, 3}
set2 = {3, 4, 5}
resultado = set1.isdisjoint(set2)
print(resultado)  # Output: False (comparten el elemento 3)

#!COMPARCION DE MULTIPLES CONJUNTOS
set1 = {1, 2}
set2 = {3, 4}
set3 = {2, 5}  # Comparte un elemento con set1
resultado1 = set1.isdisjoint(set2)
resultado2 = set1.isdisjoint(set3)
print(resultado1, resultado2)  # Output: True False

#TODO: ################################################################################
#!METODO ISSUBSET
#!SUBCONJUNTO VERDADERO POR QUE 1,2 ESTAN DENTRO DE 1,2,3,4
set1 = {1, 2}
set2 = {1, 2, 3, 4}
resultado = set1.issubset(set2)
print(resultado)  # Output: True (set1 es subconjunto de set2)


#!SUBCONJUNTO FALSO
set1 = {1, 2, 5}
set2 = {1, 2, 3, 4}
resultado = set1.issubset(set2)
print(resultado)  # Output: False (set1 no es subconjunto de set2 porque contiene el 5)

#TODO: ################################################################################

#!METODO UNION
#!UNION DE DOS CONJUNTOS DE NUMEROS
set1 = {2, 3, 4}
set2 = {4, 5, 6}
union_set = set1.union(set2)  # Crea un nuevo conjunto con la unión de set1 y set2
print(union_set)  # Output: {2, 3, 4, 5, 6}


#!UNION DE MULTIPLES CONJUNTOS
set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}
union_set = set1.union(set2, set3)  # Une los tres conjuntos
print(union_set)  # Output: 

#TODO: ################################################################################
#!METODO DIFFERRENCE
#!DIFERENCIA ENTRE DOS CONJUNTOS DE NUMEROS
#set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diferencia = set1.difference(set2)  
print(diferencia)  # Output: {1, 2} (elementos que están en set1 pero no en set2)

#!DIFERENCIA CON MULTIPLES CONJUNTOS
set1 = {1, 2, 3}
set2 = {3, 4}
set3 = {4, 5}
diferencia = set1.difference(set2, set3)  # Elementos en set1 pero no en set2 ni en set3
print(diferencia)  # Output: {1, 2}

#!METODO INTERSECTION
#!INTERSECCION DE DOS CONJUNTOS
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
interseccion = set1.intersection(set2)
print(interseccion)  # Output: {3, 4} (elementos comunes a ambos conjuntos)

#!INTERSECCION DE MULTIPLES CONJUNTOS
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
interseccion = set1.intersection(set2, set3)
print(interseccion)  # Output: {3} (elemento común a los tres conjuntos)

#? 36-38 n/v

#TODO: ################################################################################
#!METODOS DICCIONARIO
#!METODO GET
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
color_amarillo = colores.get("amarillo", "no existe")  # Obtiene el valor "yellow"
color_rojo = colores.get("rojo", "no existe ese color")
print(color_amarillo)  # Output: "yellow"
print(color_rojo)  #output: "no existe ese color"


#!METODO KEYS
#!OBTENER TODAS LAS CLAVES DE UN DICCIONARIO
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
claves = colores.keys()  # Obtiene todas las claves del diccionario
print(claves)  # Output: dict_keys(['amarillo', 'azul', 'verde'])

#!VERIFICAR SI UNA CLAVE EXISTE EN UN DICCIONARIO
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
if "rojo" in colores.keys():
    print("La clave 'rojo' existe en el diccionario.")
else:
    print("La clave 'rojo' no existe en el diccionario.")

#TODO: ################################################################################
#!METODO VALUES
#!OBTENER LOS VALORES DE UN DICCIONARIO
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
valores = colores.values()  # Obtiene todos los valores del diccionario
print(valores)  # Output: dict_values(['yellow', 'blue', 'green'])

#!VERIFICAR SI UN VALOR EXISTE EN UN DICCIONARIO
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
if "yellow" in colores.values():
    print("El valor 'yellow' existe en el diccionario.")
else:
    print("El valor 'yellow' no existe en el diccionario.")

#TODO: ################################################################################
#!METODO ITEMS
#!OBTENER TODOS LOS PARES CLAVE VALOR DE UN DICCIONARIO
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
items = colores.items()  # Obtiene todos los pares clave-valor del diccionario
print(items)  # Output: dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])

#!CREAR UNA LISTA DE TUPLAS EN BASE A LOS ITEMS
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
lista_items = list(colores.items())  # Convierte los items en una lista de tuplas
print(lista_items)  # Output: [('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')]


#!ACTIVIDAD EJECUTANDO EL CODIGO

#Ejemplo 1:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.union(my_set_2)
print(my_new_set)

#Ejemplo 2:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.intersection(my_set_2)
print(my_new_set)

#Ejemplo 3:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.difference(my_set_2)
print(my_new_set)














