
#!CORRIGIENDO ERRORES TIPOGRAFICOS
palabra = "corecto"
palabra_corregida = palabra.replace("c", "r")  # Reemplaza "c" por "r"
print(palabra_corregida)  # Output: "correcto"

#TODO: ################################################################################

#!ACTUALIZAR DATOS DE UNA CADENA
informacion = "Nombre: Juan, Edad: 30"
nueva_edad = 31
informacion_actualizada = informacion.replace("30", str(nueva_edad))  # Reemplaza "30" por "31"
print(informacion_actualizada)  # Output: "Nombre: Juan, Edad: 31"

#TODO: ################################################################################
#!PROGRAMA DE USO REAL
def censurar_palabras(texto, palabras_prohibidas):
    """Reemplaza palabras prohibidas en un texto por asteriscos."""
    for palabra in palabras_prohibidas:
        texto = texto.replace(palabra, "*" * len(palabra))  # Reemplaza cada palabra por asteriscos de igual longitud
    return texto

# Lista de palabras prohibidas
palabras_prohibidas = ["malo", "feo", "horrible"]

# Solicitar al usuario un texto
texto = input("Ingresa un texto: ")

# Censurar las palabras prohibidas y mostrar el resultado
texto_censurado = censurar_palabras(texto, palabras_prohibidas)
print("Texto censurado:", texto_censurado)
