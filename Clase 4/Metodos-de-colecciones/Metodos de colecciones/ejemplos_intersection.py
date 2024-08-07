
# #!INTERSECCION DE UN CONJUNTO VACIO
# set1 = {1, 2, 3}
# set2 = set()  # Conjunto vacío
# interseccion = set1.intersection(set2)
# print(interseccion)  # Output: set() (la intersección con un conjunto vacío es siempre vacía)

# #!INTERSECCION CONSIGO MISMO
# set1 = {1, 2, 3}
# interseccion = set1.intersection(set1)
# print(interseccion)  # Output: {1, 2, 3} (la intersección consigo mismo devuelve el mismo conjunto)


# #!DENTRO DE UNA FUNCION
# def encontrar_comunes(set1, set2):
#     """Encuentra los elementos comunes entre dos conjuntos."""
#     return set1.intersection(set2)

# numeros = {1, 2, 3, 4}
# pares = {2, 4, 6}
# comunes = encontrar_comunes(numeros, pares)
# print(comunes)  # Output: {2, 4}


#!PROGRAMA DE USO REAL
def encontrar_ingredientes_comunes(receta1, receta2):
    """Encuentra los ingredientes comunes entre dos recetas."""
    ingredientes1 = set(receta1)
    ingredientes2 = set(receta2)
    return ingredientes1.intersection(ingredientes2)

# Ingredientes de dos recetas
receta_pizza = ["harina", "agua", "sal", "tomate", "queso"]
receta_pasta = ["harina", "huevo", "sal", "aceite"]

# Encontrar los ingredientes comunes
ingredientes_comunes = encontrar_ingredientes_comunes(receta_pizza, receta_pasta)

# Mostrar los ingredientes comunes
if ingredientes_comunes:
    print("Ingredientes comunes:")
    for ingrediente in ingredientes_comunes:
        print(f"- {ingrediente}")
else:
    print("No hay ingredientes comunes entre las recetas.")

