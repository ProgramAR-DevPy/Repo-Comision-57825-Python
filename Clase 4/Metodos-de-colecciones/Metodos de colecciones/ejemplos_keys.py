
# #!ITERAR SOBRE LAS CLAVES DE UN DICCIONARIO
# colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
# for clave in colores.keys():
#     print(clave)  
# # Output:
# # amarillo
# # azul
# # verde

# #!CONVERTIRS LAS CLAVES A UNA LISTA
# colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
# lista_claves = list(colores.keys())  # Convierte las claves en una lista
# print(lista_claves)  # Output: ['amarillo', 'azul', 'verde']


# #!CREAR UN NUEVO DICCIONARIO APARTIR DE CLAVES ESPECIFICAS
# colores = {"amarillo": "yellow", "azul": "blue", "verde": "green", "rojo": "red"}
# claves_seleccionadas = ["amarillo", "azul"]
# nuevo_diccionario = {clave: colores[clave] for clave in claves_seleccionadas}
# print(nuevo_diccionario)  # Output: {'amarillo': 'yellow', 'azul': 'blue'}

#!PROGRAMA DE USO REAL
def mostrar_categorias_productos():
    """Muestra las categorías de productos disponibles en una tienda."""

    productos = {
        "Frutas": ["manzana", "banana", "naranja"],
        "Verduras": ["lechuga", "tomate", "pepino"],
        "Lácteos": ["leche", "queso", "yogur"]
    }

    print("Categorías de productos:")
    for categoria in productos.keys():
        print(f"- {categoria}")

# Mostrar las categorías de productos
mostrar_categorias_productos()
