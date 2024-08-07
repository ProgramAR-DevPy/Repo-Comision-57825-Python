
# # #!INSERTAR UN ELEMENTO EN EL MEDIO DE LA LISTA
# # colores = ["rojo", "verde", "azul"]
# # colores.insert(1, "amarillo")  # Inserta "amarillo" en la posición 1
# # print(colores)  # Output: ["rojo", "amarillo", "verde", "azul"]

# # #!INSERTAR UN ELEMENTO AL FINAL DE LA LISTA (EQUICALENTE A APPEND)
# # frutas = ["manzana", "banana"]
# # frutas.insert(len(frutas), "naranja")  # Inserta "naranja" al final 
# # print(frutas)  # Output: ["manzana", "banana", "naranja"]

# # #!INSERTANDO VARIOS ELEMENTOS USANDO SLICING
# # letras = ["a", "b", "f"]
# # letras[2:2] = ["c", "d", "e"]  # Inserta "c", "d" y "e" en la posición 2
# # print(letras)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']


# #!INSERTAR UN ELEMENTO A UNA POSICION QUE EXEDE LA LISTA
# numeros = [1, 2, 3]
# numeros.insert(10, 4)  # Inserta 4 al final de la lista (posición 3)
# print(numeros)  # Output: [1, 2, 3, 4]


#!PROGRAMA DE USO REAL
agenda = []

def agregar_contacto(nombre, telefono):
    """Agrega un contacto a la agenda en orden alfabético."""
    for i, contacto in enumerate(agenda):
        if nombre.lower() < contacto[0].lower():  # Comparación insensible a mayúsculas/minúsculas
            agenda.insert(i, (nombre, telefono))
            return
    agenda.append((nombre, telefono))  # Si no se encuentra una posición anterior, agrega al final

# Agregar contactos
agregar_contacto("Carlos", "555-1234")
agregar_contacto("Ana", "555-5678")
agregar_contacto("Beatriz", "555-9012")

# Mostrar la agenda
print("Agenda de contactos:")
for nombre, telefono in agenda:
    print(f"- {nombre}: {telefono}")
