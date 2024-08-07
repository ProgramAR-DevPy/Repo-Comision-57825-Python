
# # #!UNION CONJUNTO VACIO
# # set1 = {1, 2, 3}
# # set2 = set()  # Conjunto vacío
# # union_set = set1.union(set2)
# # print(union_set)  # Output: {1, 2, 3} (la unión con un conjunto vacío devuelve el conjunto original)


# #!UNION CON DIFERENTES TIPOS DE DATOS
# set1 = {1, "dos", True}
# set2 = {3.14, False, "dos"}
# union_set = set1.union(set2)
# print(union_set)  # Output: {1, 3.14, 'dos', True, False}

# #!DENTRO DE UNA FUNCION
# def unir_conjuntos(set1, set2):
#     """Une dos conjuntos y devuelve el resultado."""
#     return set1.union(set2)

# numeros = {1, 2}
# letras = {"a", "b"}
# union_set = unir_conjuntos(numeros, letras)
# print(union_set)  # Output: {1, 2, 'a', 'b'}


#!PROGRAMA DE USO REAL
def combinar_amigos(amigos_facebook, amigos_twitter, amigos_instagram):
    """Combina listas de amigos de diferentes redes sociales en un solo conjunto."""
    return set(amigos_facebook).union(amigos_twitter, amigos_instagram)

# Listas de amigos de diferentes redes sociales
amigos_facebook = ["Ana", "Juan", "Pedro", "María"]
amigos_twitter = ["Juan", "Luis", "Sofía"]
amigos_instagram = ["María", "Carlos", "Ana"]

# Combinar amigos en un solo conjunto
todos_mis_amigos = combinar_amigos(amigos_facebook, amigos_twitter, amigos_instagram)

# Mostrar el conjunto de amigos (sin duplicados)
print("Todos mis amigos:", todos_mis_amigos)


