
# #!ITERAR SOBRE LOS VALORES DE UN DICCIONARIO
# colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
# for valor in colores.values():
#     print(valor)
# # Output:
# # yellow
# # blue
# # green

# #!CONVERTIR LOS VALORES EN UNA LISTA
# colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
# lista_valores = list(colores.values())  # Convierte los valores en una lista
# print(lista_valores)  # Output: ['yellow', 'blue', 'green']

# #!ENCONTAR EL VALOR MAXIMO DE UN DICCIONARIO
# temperaturas = {"Madrid": 25, "Barcelona": 28, "Sevilla": 32}
# temperatura_maxima = max(temperaturas.values())  # Encuentra la temperatura máxima
# print(temperatura_maxima)  # Output: 32


#!PROGRAMA DE USO REAL
def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    return sum(notas) / len(notas)

estudiantes = {
    "Ana": [8.5, 9.0, 7.5],
    "Juan": [9.2, 8.8, 9.5],
    "María": [7.8, 8.2, 8.0]
}

for estudiante, notas in estudiantes.items():
    promedio = calcular_promedio(notas)
    print(f"El promedio de {estudiante} es: {promedio:.2f}")  # Mostrar con dos decimales



