
#!INVERTIR UNA LISTA HETEROGENEA
elementos = [1, "dos", True, 3.14]
elementos.reverse()
print(elementos)  # Output: [3.14, True, 'dos', 1]

#!INVERTIR UNA LISTA Y ASIGNARLA A UNA VARIABLE
original = [10, 20, 30]
invertida = original.copy()  # Crea una copia de la lista original
invertida.reverse()  # Invierte la copia
print(original)  # Output: [10, 20, 30] (la lista original no se modifica)
print(invertida)  # Output: [30, 20, 10]


#!PROGRAMA DE USO REAL
def es_palindromo(palabra):
    """Verifica si una palabra es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""
    palabra_minusculas = palabra.lower()  # Convierte a minúsculas para ignorar mayúsculas/minúsculas
    lista_caracteres = list(palabra_minusculas)
    lista_caracteres.reverse()
    palabra_invertida = "".join(lista_caracteres)
    return palabra_minusculas == palabra_invertida

# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Verificar si es palíndromo y mostrar el resultado
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")




