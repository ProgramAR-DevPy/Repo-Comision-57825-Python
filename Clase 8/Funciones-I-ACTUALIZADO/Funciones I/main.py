def preparar_pizza(ingredientes):
    """Prepara una pizza con los ingredientes dados y devuelve un mensaje."""
    print("Preparando la masa...")
    print("Agregando los ingredientes:", ingredientes)
    print("Horneando la pizza...")
    mensaje = f"pizza de {' y '.join(ingredientes)} esta lista"
    return mensaje
    
#VOLVEMOS EN SEGUIDA
pizza1 = preparar_pizza()




# Preparamos diferentes pizzas y guardamos los mensajes
preparar_pizza(["queso", "jamón"])
preparar_pizza(["pepperoni", "aceitunas"])
preparar_pizza(["champiñones", "pimientos", "cebolla"])



#SUMAR NUMEROS DE UNA LISTA
def sumar_lista(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma 

resultado = sumar_lista([1, 2, 3, 4, 5]) 



suma = resultado + resultado
print(suma)


#NUMERO MAYOR DE UNA LISTA
def encontrar_mayor(numeros):
    mayor = numeros[0]
    for num in numeros:
        if num > mayor:
            mayor = num
    return mayor

print(encontrar_mayor([3, 5, 7, 2, 8])) 

#CONTADOR DE ELEMENTOS DE UNA LISTA
def contar_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

print(contar_elementos([1, 2, 3, 4, 5]))


#IMPRIMIENDO NUMEROS CON WHILE
def imprimir_numeros():
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1

imprimir_numeros()

#RANGOS
def imprimir_numeros_for():
    for numero in range(1, 11):
        print(numero)

imprimir_numeros_for()


#SUMANDO NUMEROS PARES
def sumar_pares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 == 0:
            suma += num
    return suma

print(sumar_pares([1, 2, 3, 4, 5, 6]))





#Actividad en Clase
"""
Escribir una función a la que se le pase una cadena del nombre de una ciudad <ciudad> y muestre por pantalla el saludo ¡hola bienvenidx a <nombre>!.
"""

def ciudad(cadena):
    return f"Bienvenido a {cadena}"

respuesta = ciudad("Argentina")

print(respuesta)



#MEDIA
"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.

"""
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

lista = [1, 2, 3, 4, 5]
media = calcular_media(lista)
print(f"La media de la muestra es: {media}")

#MULTIPLO
"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.

"""
def es_multiplo(a, b):
    return a % b == 0 or b % a == 0

numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))


if es_multiplo(numero1, numero2):
    print(f"Sí, {numero1} y {numero2} son múltiplos uno del otro.")
else:
    print(f"No, {numero1} y {numero2} no son múltiplos uno del otro.")




























