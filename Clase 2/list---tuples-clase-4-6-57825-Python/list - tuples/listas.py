# """
# Las listas son colecciones que nos permiten agrupar diferentes tipos de datos
# en un mismo lugar. Estas son ordenadas, por lo mantienen el orden de como las
# definieron


# Ejemplo de lista.
# """


# #Lista de numeros
# lista1 = [ 5, 11, 23, -100, 0 ]
# lista = []  #lista vacia


# #Lista de string
# lista2 = ["Que", "Onda", "perro?", "xD"]

# #Lista heterogeneas
# diccionario = "ale"
# ejemplo = 11111111111111

# lista3 = ["hola", "mundo", 15, ejemplo, -50, 1.5, [1, 2 ,3, 4, 5], diccionario, {"Nombre": "Alejandro", "Apellido": "Sosa", "Edad": 39 } ]


# # print(lista)
# # print(lista2)
# # print(lista3)
# # print(lista1)

# lista_vertical = [
#       "Ale",
#     123,
#     "sosa",
#     "sosa",
#     "lista",
#     "vertical"

# ]

# print(f"{lista1}, {lista2}, {lista3}, {lista_vertical}")

# nueva_lista = ["hola", "mundo", "de", "python",  "el", "mejor", "lenguaje","😂","en", "tu", "cara", "Javascript"]
# print(nueva_lista[0])  #hola
# print(nueva_lista[1])  #mundo
# print(nueva_lista[2])  #de
# print(nueva_lista[3])  #python
# print(nueva_lista[::-1])  #python de mundo hola
# print(nueva_lista[::2])  #hola de el lenguaje tu javascript
# print(nueva_lista[::]) #hola mundo de python el mejor lenguaje en tu cara javascript
# print(nueva_lista[::-1])


#Concatenando
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista_concatenada = lista2 + lista1  # [1, 2, 3, 4, 5, 6]
# print(lista_concatenada)

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista2 += lista1  # lista1 ahora es [1, 2, 3, 4, 5, 6]

# print(lista2)

#NO VA EN EL CURSO, SOLO PARA CONOCER
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista_concatenada = [*lista1, *lista2]  # [1, 2, 3, 4, 5, 6]

# print(lista_concatenada)


#Mutables 
# pares = [0, 2, 4, 5, 8, 10]
# pares[4] = 55555555555555

# print(pares)

#Funciones de listas integradas

# lista = [ 1, 2, 3, 4]
# print(f"Lista normal: {lista}")
# lista.append(5)
# print(f"lista con el 5 agregado por append: {lista}")



# #Contando elementos de una lista
# mi_lista = [1, 2, 3, "Hola", True, 5.7, " "]
# longitud = len(mi_lista) 

#Y si quiero contar un string sin espacios
# texto = "Hola mundo"
# longitud_sin_espacios = len(texto.replace(" ", ""))  # Resultado: 9
# print(longitud_sin_espacios)


# #un espacio " "
# #una vacia ""



# #Eliminando un elemento de la lista
# frutas = ["manzana", "banana", "pera", "uva"]
# ultima_fruta = frutas.pop(0)  # Elimina "uva" y la devuelve
# #print(ultima_fruta)  # Output: uva
# print(frutas)       # Output: ['manzana', 'banana', 'pera']

#El método count() se utiliza para contar cuántas veces aparece un elemento específico en una secuencia (como una lista o una cadena).

# numeros = [1, 2, 3, 2, 5, 2]
# cantidad_de_dos = numeros.count(2)  # Resultado: 3

# frutas = ["manzana", "banana", "pera", "banana"]
# cantidad_de_bananas = frutas.count("banana")  # Resultado: 2

#El método index() se utiliza para encontrar la posición (índice) de la primera aparición de un elemento específico en una secuencia.
# numeros = [1, 2, 3, 2, 5, 2]
# indice_del_primer_dos = numeros.index(2)  # Resultado: 1

# # print(indice_del_primer_dos)


# # frutas = ["manzana", "banana", "pera", "banana"]
# # indice_de_la_primera_banana = frutas.index("banana")  # Resultado: 1

# #Desafio Listas
# """
# Descripción de la actividad:

# En esta actividad, podrás poner en práctica lo aprendido. Usaremos Visual Studio Code.

# Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras. Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.

# Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
# Luego añade a la lista_2 el <str> "Hola y adiós", y luego el <int> 5555
# Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
# Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
# Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3 

# """
# lista_1 = [1, 2, 3]
# # print(f"lista 1 normal: {lista_1}")
# # lista_1.append(456789)
# # lista_1.append("hola mundo")
# # print(f"lista 1 modificada: {lista_1}")



# lista_2 = [4, 5, 6]
# # print(f"lista 2 normal: {lista_2}")
# # lista_2.append("hola y adios")
# # lista_2.append(5555)
# # print(f"lista 2 modificada: {lista_2}")

# lista_3 = lista_1[:-1]
# # print(lista_3)

# # lista_3 = lista_1.pop()
# # print(lista_3)

# lista_4 = lista_2[1:-1]
# print(lista_4)


# lista_5 = lista_3 + lista_4
# print(lista_5)


# #Las tuplas son colecciones de datos, al igual que las listas, con la única diferencia de que las tuplas son inmutables. 

# # Tupla con un solo elemento (necesita una coma al final)
# # Si no ponemos la coma al final, Python interpretará que asignamos el valor de un número entero (int) y no una tupla (tuple).
# tupla_un_elemento = (1,) 

# Tupla con múltiples elementos
# numeros = (1, 2, 3, 4, 5)
# colores = ("rojo", "verde", "azul")
# datos_mixtos = (10, "Hola", True, 3.14)


# #accediendo a elementos de una tupla
# numeros = (1, 2, 3, 4, 5)
# primer_numero = numeros[0]    # Resultado: 1
# ultimo2_numero = numeros[-1]   # Resultado: 5

# #Importante:  Las tuplas no contienen la función append() 👀, pero puedes agregar elementos con la técnica de concatenación:

# numeros = (1, 2, 3, 4)
# numeros += (5, 6, 7, 8)
# print(numeros)  #output (1, 2, 3, 4, 5, 6, 7, 8)
# años = (2020, 2021, 2022)
# años += (2023,)
# print(años)  #output(2020, 2021, 2022, 2023)

 #len tuplas
# numeros = (1, 2, 3, 4, 5)
# longitud = len(numeros)  # Resultado: 5

# #count tuplas
# numeros = (1, 2, 3, 2, 5, 2)
# cantidad_de_dos = numeros.count(2)  # Resultado: 3

# #index tuplas
# numeros = (1, 2, 3, 2, 5, 2)
# indice_del_primer_dos = numeros.index(2)  # Resultado: 1

arbol = [ 
    "A",
    ["B", ["C", "D"], "E"],
    ["F", "G"]
]

print(arbol[1][1][0])



