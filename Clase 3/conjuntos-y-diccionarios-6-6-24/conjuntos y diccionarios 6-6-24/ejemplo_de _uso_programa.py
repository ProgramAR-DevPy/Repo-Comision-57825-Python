"""
ATENCION!!!! Este archivo es solo un ejemplo de uso
de lo que hacemos para traer datos especificos 
de un diccionario. 
No es un archivo a entregar para ser correjido.
Es solo para que lo ejecuten y vea como se comporta
"""


def obtener_datos_personales():
    """Solicita al usuario su nombre, apellido y edad y los almacena en un diccionario."""

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))

    return {"nombre": nombre, "apellido": apellido, "edad": edad}

def mostrar_dato(datos, clave):
    """Muestra un dato específico del diccionario."""

    if clave in datos:
        print(f"{clave.capitalize()}: {datos[clave]}")
    else:
        print(f"Error: La clave '{clave}' no existe.")

# Obtener datos del usuario
datos_usuario = obtener_datos_personales()

# Mostrar menú de opciones
while True:
    print("\nOpciones:")
    print("1. Mostrar nombre")
    print("2. Mostrar apellido")
    print("3. Mostrar edad")
    print("4. Mostrar todos los datos")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        mostrar_dato(datos_usuario, "nombre")
    elif opcion == "2":
        mostrar_dato(datos_usuario, "apellido")
    elif opcion == "3":
        mostrar_dato(datos_usuario, "edad")
    elif opcion == "4":
        for clave, valor in datos_usuario.items():
            print(f"{clave.capitalize()}: {valor}")
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
