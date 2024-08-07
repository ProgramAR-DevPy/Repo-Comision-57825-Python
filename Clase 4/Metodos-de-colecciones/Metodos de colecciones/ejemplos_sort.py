
#!ORDENAR UNA LISTA DE TUPLAS 
datos = [(3, "manzana"), (1, "pera"), (2, "naranja")]
datos.sort(key=lambda x: x[1])  # Ordena por el segundo elemento de cada tupla (la fruta)
print(datos)  # Output: [(3, 'manzana'), (2, 'naranja'), (1, 'pera')]


#!ORDENAR UNA LISTA DE DICCIONARIOS POR UN VALOR ESPECIFICO
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 35}
]
personas.sort(key=lambda x: x["edad"])  # Ordena por la edad de cada persona
print(personas)
# Output: [{'nombre': 'Juan', 'edad': 25}, {'nombre': 'Ana', 'edad': 30}, {'nombre': 'María', 'edad': 35}]

#!PROGRAMA DE USO REAL
def ordenar_estudiantes_por_promedio(estudiantes):
    """Ordena una lista de estudiantes por su promedio de notas de mayor a menor."""
    estudiantes.sort(key=lambda estudiante: estudiante["promedio"], reverse=True)

# Lista de estudiantes con nombre y promedio
estudiantes = [
    {"nombre": "Ana", "promedio": 8.5},
    {"nombre": "Juan", "promedio": 9.2},
    {"nombre": "María", "promedio": 7.8}
]

# Ordenar a los estudiantes por promedio y mostrar el resultado
ordenar_estudiantes_por_promedio(estudiantes)
print("Estudiantes ordenados por promedio (de mayor a menor):")
for estudiante in estudiantes:
    print(f"- {estudiante['nombre']}: {estudiante['promedio']}")
