
#!COMPARANDO CONJUNTOS CON DIFERENTES TIPOS DE DATOS
set1 = {1, 2.5, "tres"}
set2 = {"tres", 4, True}
resultado = set1.isdisjoint(set2)
print(resultado)  # Output: False (comparten el elemento "tres")


#!COMPARACION CON UN CONJUNTO VACIO
set1 = {1, 2, 3}
set2 = set()  # Conjunto vacío
resultado = set1.isdisjoint(set2)
print(resultado)  # Output: True (un conjunto vacío es disjunto a cualquier otro conjunto)


#!USO DENTRO DE UNA FUNCION
def son_disjuntos(set1, set2):
    """Verifica si dos conjuntos son disjuntos."""
    return set1.isdisjoint(set2)

numeros = {1, 2, 3}
letras = {"a", "b", "c"}
resultado = son_disjuntos(numeros, letras)
print(resultado)  # Output: True


#!PROGRAMA DE USO REAL
def verificar_nombre_usuario_disponible(nombre_usuario, nombres_usuarios_existentes):
    """Verifica si un nombre de usuario está disponible (no existe en la lista de nombres existentes)."""

    nombre_usuario_en_minusculas = set(nombre_usuario.lower())  # Convertir a minúsculas y a conjunto
    nombres_existentes_en_minusculas = set(nombre.lower() for nombre in nombres_usuarios_existentes)

    return nombre_usuario_en_minusculas.isdisjoint(nombres_existentes_en_minusculas)

# Lista de nombres de usuario existentes
nombres_usuarios_existentes = ["Juan123", "Ana_Maria", "Pedro_Perez"]

# Solicitar al usuario un nombre de usuario
while True:
    nombre_usuario = input("Ingresa un nombre de usuario: ")

    # Verificar disponibilidad
    if verificar_nombre_usuario_disponible(nombre_usuario, nombres_usuarios_existentes):
        print("¡El nombre de usuario está disponible!")
        break  # Salir del bucle si el nombre está disponible
    else:
        print("El nombre de usuario ya existe. Intenta con otro.")
