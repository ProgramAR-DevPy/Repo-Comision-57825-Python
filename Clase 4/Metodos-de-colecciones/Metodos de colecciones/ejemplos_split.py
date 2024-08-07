
#!DIVIDIR UNA RUTA DE ARCHIVO
ruta = "/home/usuario/documentos/archivo.txt"
partes_ruta = ruta.split("/")  # Separa por barras diagonales
print(partes_ruta)  # Output: ['', 'home', 'usuario', 'documentos', 'archivo.txt']

#TODO: ################################################################################

#!DIVIDE EN LINEAS
texto = """
Primera línea
Segunda línea
Tercera línea
"""
lineas = texto.splitlines()  # Separa por saltos de línea
print(lineas)  # Output: ['', 'Primera línea', 'Segunda línea', 'Tercera línea']

#TODO: ################################################################################

#!PROGRAMA DE USO REAL
def extraer_hashtags(tweet):
    """Extrae los hashtags de un tweet."""
    palabras = tweet.split()  # Divide el tweet en palabras
    hashtags = [palabra for palabra in palabras if palabra.startswith("#")]  # Filtra las palabras que comienzan con "#"
    return hashtags

# Solicitar al usuario un tweet
tweet = input("Ingresa un tweet: ")

# Extraer los hashtags y mostrarlos
hashtags_encontrados = extraer_hashtags(tweet)
if hashtags_encontrados:
    print("Hashtags encontrados:")
    for hashtag in hashtags_encontrados:
        print(hashtag)
else:
    print("No se encontraron hashtags en el tweet.")

