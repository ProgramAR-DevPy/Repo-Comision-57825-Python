"""
# Operadores

## Tipo lógico (True / False)

Guardamos el valor en una variable
"""

es_mayor = True
print(es_mayor)

es_mayor = False
print(es_mayor)

"""Se puede negar un valor, en otras palabras, lo cambia al estado contrario"""

es_mayor = not True
print(es_mayor)

es_mayor = not False
print(es_mayor)

"""Podemos castear cualquier tipo de dato a boolean

"Castear" es convertir el tipo de dato, ejemplo:
valor = int("123")
"""

respuesta_1 = bool(1)
respuesta_2 = bool("Buenas noches!")
respuesta_3 = bool(123.56)
respuesta_4 = bool(["a", "b"])
respuesta_5 = bool((1,))
respuesta_6 = bool({1,2,3})
respuesta_7 = bool({"hola": "Comi"})

respuesta_8 = bool(0)
respuesta_9 = bool("")
respuesta_10 = bool(0.0)
respuesta_11 = bool([])
respuesta_12 = bool(())
respuesta_13 = bool({})

print(respuesta_1)
print(respuesta_2)
print(respuesta_3)
print(respuesta_4)
print(respuesta_5)
print(respuesta_6)
print(respuesta_7)

print(respuesta_8)
print(respuesta_9)
print(respuesta_10)
print(respuesta_11)
print(respuesta_12)
print(respuesta_13)


valor01 = True

valor02 = False

operacion = (valor01 + valor01) * (valor01 + valor01)

print(operacion)










x = 5
y = 3

print(x - y)

x = 2
y = 2

print(x * y)

x = 12
y = 3

print(x / y)

x = 12
y = 5

print(x // y)

x = 14
y = 5

print(x % y)

x = 2
y = 5

print(x ** y)

"""## Operadores relacionales"""

# Operadores de asignación vs relacionales
valor_1 = 5
valor_2 = 10

valor_1 == valor_2
if valor_1 == valor_2:
    print("Son iguales nene")
else: print("Son diferentes perro")

# IGUALDAD
valor_1 = 5
valor_2 = 10

respuesta = valor_1 == valor_2
print(respuesta)

# DESIGUALDAD
valor_1 = 5
valor_2 = 10

respuesta = valor_1 != valor_2
print(respuesta)

# MENOR QUE
valor_1 = 5
valor_2 = 10

respuesta = valor_1 < valor_2
print(respuesta)

# MENOR IGUAL QUE
valor_1 = 5
valor_2 = 10

respuesta = valor_1 <= valor_2
print(respuesta)

# MAYOR QUE
valor_1 = 5
valor_2 = 10

respuesta = valor_1 > valor_2
print(respuesta)

# MAYOR IGUAL QUE
valor_1 = 5
valor_2 = 10

respuesta = valor_1 >= valor_2
print(respuesta)

# Todas las operaciones aplican a diferentes tipos de datos
valor_1 = "Hola"
valor_2 = "Amigos"

respuesta = valor_1 >= valor_2
print(respuesta)

valor_1 = [1,2,3]
valor_2 = [5]

respuesta = valor_1 >= valor_2
print(respuesta)

"""Los tipo lógicos (True/False) tienen un valor por defecto:
True = 1
False = 0
"""

True * 100

False + 5

"""## Ejercicio: Operadores relacionales"""

#PREGUNTA: ¿Esto es una buena practica?
expresiones = [False == True, 10 >= 2*4, 33/3 == 11, True > False, True*5 == 2.5*2]


print(expresiones)

"""Operadores lógicos

NOT
Negación, invierte el valor booleano de una comparación
"""

not True

not False

not 5 > 10

not 10 > 5

"""AND
Devuelve verdadero si 2 comparaciones son verdaderas.
Devuelve falso si al menos una de las 2 comparaciones es falsa.
"""

True and True

print(True and True)
print(True and False)
print(False and True)
print(False and False)

2 > 1 and 5 > 2

2 > 1 and 5 > 20

edad = input("Ingrese una edad: ")
edad = int(edad)

mayor = edad >= 18
print(mayor)

"""OR
Devuelve verdadero si al menos una comparación es verdadera.
Devuelve falso si ambas comparaciones son falsas.
"""

print(True or True)
print(True or False)
print(False or True)
print(False or False)

2 > 1 or 5 > 2

5 < 20 or 20 < 1

10 > 5 or 55 > "5asdfasdfbgadfbgadebadedfebaen5" or "lwglwqrg" or 0

"""## Ejercicio: Operadores lógicos"""

expresiones = [
not False,
not 3 == 5,
33/3 == 11 and 5 > 2,
True or False,
True*5 == 2.5*2 or 123 >= 23,

12 > 7 and True < False
]
print(expresiones)

"""## Repaso General"""

-32.366 <= -90

1 + 3 == 8 - 4

"Nasdgasdgasdgfasdg" >= "N"

"NIco" == "Nlco"

"NIco" >= "Nlco"

"Nico" >= "Melanie"

"""
"Ana" < "Antonio" (porque "n" es menor que "t")
"Casa" > "Carro" (porque "s" es mayor que "r")
"Hola" == "Hola" (porque son idénticas)
"""



nombre = "Nico Perez"
nombre2 = "Brenda"
nombre3 = "Pepito"

nombre[-2] != "R"

nombre2 < nombre3

(len(nombre) < 15) == False



"""##AND OR NOT"""

print(100 > 3 and 100 < 10)

print(100 > 3 or 100 < 4)

print(not(100 > 3 and 100 < 10))

x = ["manzas", "peras"]
y = ["manzanas", "banana"]
z = x
print(x)
print(y)
print(z)

print(x in z)
print(x == z)
print(x in y)
print(x == y)



"""##Listas y operaciones lógicas"""

listaNueva = [3+1-11 , 20/6, 11-8]
print(listaNueva)

expresiones = [False == True, 10 >= 2*4, 33/3 == 11, True > False, True*5 == 2.5*2]
variable1 = expresiones[0]
print(variable1)

edadNadia = 27
edadNico = 32
edadLuis = 17
variable = edadNadia >= 18 and edadNico >= 18 and edadLuis >= 18

print(variable)

edadNadia >= 18 or edadLuis >= 18

not (edadNico >= 18)

"""## Operadores de asignación"""

a = 0
a += 1
print(a)

a = 0
a =+ 1
print(a)




expresiones22 = [
False == True,
10 >= 2*4,
33/3 == 11,
True > False,
True*5 == 2.5*2
]

print(expresiones22)