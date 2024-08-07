
# #!EXTRAER LA EXTENSION DE UN ARCHIVO
# nombre_archivo = "documento.txt.bak"
# indice_punto = nombre_archivo.rfind(".")  # Busca el último punto
# if indice_punto != -1:
#     extension = nombre_archivo[indice_punto + 1:]  # Extrae la extensión después del último punto
#     print(f"La extensión del archivo es: {extension}")


# #TODO: ################################################################################
# #!ULTIMO NUMERO DE UNA CADENA
# texto = "Tengo 2 manzanas, 3 naranjas y 1 plátano."
# indice_numero = texto.rfind(lambda x: x.isdigit())  # Busca el último carácter que es un dígito
# if indice_numero != -1:
#     numero = texto[indice_numero]
#     print(f"El último número en el texto es: {numero}")

# #TODO: ################################################################################
# #!VERIFICANDO SI UN ENLACE TERMINA CON UNA EXTENSION ESPECIFICA
# enlace = "https://www.ejemplo.com/archivo.pdf"
# extensiones_validas = (".pdf", ".doc", ".txt")
# if any(enlace.endswith(ext) for ext in extensiones_validas):
#     print("El enlace es válido.")
# else:
#     print("El enlace no es válido.")


#TODO: ################################################################################
#!PROGRAMA DE USO REAL
def extraer_dominio(correo_electronico):
    """Extrae el dominio de un correo electrónico."""
    indice_arroba = correo_electronico.find("@")
    if indice_arroba != -1:
        dominio = correo_electronico[indice_arroba + 1:]
        return dominio
    else:
        return None  # El correo no tiene un formato válido

# Solicitar al usuario un correo electrónico
correo = input("Ingresa tu correo electrónico: ")

# Extraer y mostrar el dominio
dominio = extraer_dominio(correo)
if dominio:
    print(f"El dominio de tu correo es: {dominio}")
else:
    print("El correo electrónico no tiene un formato válido.")




