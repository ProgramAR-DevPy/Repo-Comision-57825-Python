
#!EXTRAER APARTIR DE UN INDICE
url = "https://www.ejemplo.com/pagina"
indice_barra = url.find("/")
if indice_barra != -1:
    ruta = url[indice_barra:]  # Extrae la parte de la ruta después de la primera barra
    print(ruta)  # Imprime "/pagina"

#TODO: ################################################################################
#!MULTIPLES APARICIONES
texto = "El perro juega con el gato. El gato persigue al perro."
subcadena = "perro"
indice = -1
while True:
    indice = texto.find(subcadena, indice + 1)  # Busca desde la última posición encontrada + 1
    if indice == -1:
        break
    print(f"La subcadena '{subcadena}' se encuentra en la posición {indice}.")

#!ENCONTRAR POSICIONDE UN NUMERO EN UNA CADENA
texto = "Tengo 2 manzanas y 3 naranjas."
indice_numero = texto.find("2")
if indice_numero != -1:
    print(f"El número 2 se encuentra en la posición {indice_numero}.")


#TODO: ################################################################################
#!PROGRAMA DE USO REAL

def encontrar_arroba(correo_electronico):
    """Encuentra la posición del símbolo @ en un correo electrónico."""
    return correo_electronico.find("@")

# Solicitar al usuario un correo electrónico
correo = input("Ingresa tu correo electrónico: ")

# Encontrar la posición del símbolo @
posicion_arroba = encontrar_arroba(correo)

if posicion_arroba != -1:
    print(f"El símbolo @ se encuentra en la posición {posicion_arroba}.")
else:
    print("El correo electrónico no contiene el símbolo @.")



