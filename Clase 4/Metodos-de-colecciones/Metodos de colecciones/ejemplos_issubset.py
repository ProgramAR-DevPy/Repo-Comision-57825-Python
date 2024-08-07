
# #!CONJUNTO VACIO COMO SUBCONJUNTO
# set1 = set()  # Conjunto vacío
# set2 = {1, 2, 3}
# resultado = set1.issubset(set2)
# print(resultado)  # Output: True (un conjunto vacío es subconjunto de cualquier conjunto)

# #!COMPARACION CONSIGO MISMO
# set1 = {1, 2, 3}
# resultado = set1.issubset(set1)
# print(resultado)  # Output: True (un conjunto es siempre subconjunto de sí mismo)


# #!COMPARACION DE MULTIPLES SUBCONJUNTOS
# set1 = {1, 2}
# set2 = {1, 2, 3}
# set3 = {2, 3}
# resultado1 = set1.issubset(set2)
# resultado2 = set3.issubset(set2)
# print(resultado1, resultado2)  # Output: True True


# #!USO EN UNA FUNCION
# def es_subconjunto(set1, set2):
#     """Verifica si set1 es un subconjunto de set2."""
#     return set1.issubset(set2)

# numeros_pares = {2, 4, 6}
# numeros_enteros = {1, 2, 3, 4, 5, 6}
# resultado = es_subconjunto(numeros_pares, numeros_enteros)
# print(resultado)  # Output: True


#!PROGRAMA DE USO REAL
def es_palabra_valida(palabra, letras_disponibles):
    """Verifica si una palabra se puede formar con las letras disponibles en un juego de Scrabble."""
    letras_palabra = set(palabra.lower())  # Convertimos la palabra a minúsculas y a un conjunto
    return letras_palabra.issubset(letras_disponibles)  # Verificamos si es un subconjunto de las letras disponibles

# Letras disponibles en el juego
letras_disponibles = set("abcdefghijklmnñopqrstuvwxyz")

# Solicitar al usuario una palabra
while True:
    palabra = input("Ingresa una palabra (o 'salir' para terminar): ")
    if palabra.lower() == "salir":
        break

    # Verificar si la palabra es válida y mostrar el resultado
    if es_palabra_valida(palabra, letras_disponibles):
        print("La palabra es válida.")
    else:
        print("La palabra no es válida. No tienes las letras necesarias.")


