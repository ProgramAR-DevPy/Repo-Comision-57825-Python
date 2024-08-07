
# #!CREAR UNA LISTA DE CORREOS
# nombres = ["ana", "juan", "maria"]
# dominio = "ejemplo.com"
# correos = [f"{nombre}@{dominio}" for nombre in nombres]
# lista_correos = ", ".join(correos)  # Une los correos con comas y espacios
# print(lista_correos)  # Output: "ana@ejemplo.com, juan@ejemplo.com, maria@ejemplo.com"

# #TODO: ################################################################################
# #!CREANDO UNA RUTA DE ARCHIVO
# carpetas = ["usuario", "documentos", "proyectos"]
# nombre_archivo = "informe.txt"
# ruta = "/".join(carpetas + [nombre_archivo])  # Une las carpetas y el nombre del archivo con barras diagonales
# print(ruta)  # Output: "/usuario/documentos/proyectos/informe.txt"

# #TODO: ################################################################################
# #!CONVIRTIENDO UNA LISTA DE NUMEROS A UNA CADENA
# numeros = [1, 2, 3, 4, 5]
# cadena_numeros = ", ".join(str(num) for num in numeros)  # Convierte cada número a cadena antes de unir
# print(cadena_numeros)  # Output: "1, 2, 3, 4, 5"

#TODO: ################################################################################
#!PROGRAMA DE USO REAL
def formatear_lista_compras(lista_compras):
    """Formatea una lista de compras en una cadena legible."""
    return "\n".join(f"- {item}" for item in lista_compras)

# Solicitar al usuario los elementos de la lista de compras
lista_compras = []
while True:
    item = input("Ingresa un artículo (o escribe 'fin' para terminar): ")
    if item.lower() == "fin":
        break
    lista_compras.append(item)

# Formatear y mostrar la lista de compras
lista_formateada = formatear_lista_compras(lista_compras)
print("\nLista de compras:")
print(lista_formateada)
