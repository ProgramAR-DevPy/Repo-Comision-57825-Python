
#!CONTANDO VOCALES
cadena = "aeiouAEIOU"
vocales = "aeiou"
cantidad_vocales = sum(cadena.count(vocal) for vocal in vocales)
print(f"La cadena '{cadena}' tiene {cantidad_vocales} vocales.")

#TODO: ################################################################################
#!PROGRAMA DE USO REAL
def contar_letras_a(texto):
    """Cuenta el número de letras "a" (mayúsculas y minúsculas) en un texto."""
    return texto.count("a") + texto.count("A")

# Solicitar al usuario un texto
texto = input("Ingresa un texto: ")

# Contar las letras "a" y mostrar el resultado
num_letras_a = contar_letras_a(texto)
print(f"El texto contiene {num_letras_a} letras 'a'.")
