

# #!DIFERENCIA CON UN CONJUNTO VACIO
# set1 = {1, 2, 3}
# set2 = set()  # Conjunto vacío
# diferencia = set1.difference(set2)
# print(diferencia)  # Output: {1, 2, 3} (la diferencia con un conjunto vacío devuelve el conjunto original)


# #!DENTRO DE UNA FUNCION
# def encontrar_diferentes(set1, set2):
#     """Encuentra los elementos diferentes entre dos conjuntos."""
#     return set1.difference(set2)

# numeros = {1, 2, 3, 4}
# pares = {2, 4, 6}
# diferentes = encontrar_diferentes(numeros, pares)
# print(diferentes)  # Output: {1, 3}



#!PROGRAMA DE USO REAL
def encontrar_canciones_diferentes(lista1, lista2):
    """Encuentra las canciones que están en una lista pero no en la otra."""
    set1 = set(lista1)
    set2 = set(lista2)
    diferentes_en_lista1 = set1.difference(set2)
    diferentes_en_lista2 = set2.difference(set1)
    return diferentes_en_lista1, diferentes_en_lista2

# Listas de reproducción de música
mis_canciones = ["Canción A", "Canción B", "Canción C", "Canción D"]
canciones_amigo = ["Canción B", "Canción E", "Canción F"]

# Encontrar canciones diferentes en cada lista
diferentes_en_mi_lista, diferentes_en_lista_amigo = encontrar_canciones_diferentes(mis_canciones, canciones_amigo)

print("Canciones que tengo y mi amigo no:")
for cancion in diferentes_en_mi_lista:
    print("- ", cancion)

print("\nCanciones que mi amigo tiene y yo no:")
for cancion in diferentes_en_lista_amigo:
    print("- ", cancion)
