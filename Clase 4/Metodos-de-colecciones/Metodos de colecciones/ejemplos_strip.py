
#!LIMPIANDO DATOS DE ENTRADA DEL USUARIO
nombre = input("Ingresa tu nombre: ")
nombre_limpio = nombre.strip()  # Elimina espacios en blanco adicionales
print(nombre_limpio)

#TODO: ################################################################################
#!EJEMPLO DE USO PROGRAMA REAL
def limpiar_texto(texto):
    """Elimina espacios en blanco, saltos de línea y caracteres especiales de un texto."""
    caracteres_a_eliminar = " \n\t.,;:-_!?¡¿"  # Define los caracteres a eliminar
    texto_limpio = texto.strip(caracteres_a_eliminar)  # Elimina los caracteres especificados
    return texto_limpio

# Solicitar al usuario un texto
texto_sucio = input("Ingresa un texto: ")

# Limpiar el texto y mostrar el resultado
texto_limpio = limpiar_texto(texto_sucio)
print("Texto limpio:", texto_limpio)

