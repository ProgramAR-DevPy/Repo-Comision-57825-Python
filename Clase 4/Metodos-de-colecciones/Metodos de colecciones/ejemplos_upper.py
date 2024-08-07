# Lista original de nombres con mayúsculas y minúsculas mezcladas
nombres = ["ana", "JUAN", "maría"]

# Crea una nueva lista donde cada nombre se convierte a mayúsculas usando una comprensión de lista
nombres_normalizados = [nombre.upper() for nombre in nombres]  

# Imprime la lista de nombres normalizados (todos en mayúsculas)
print(nombres_normalizados) # ['ANA', 'JUAN', 'MARÍA']


#TODO:###############################################################################

#MODIFICAR VARIABLE CONTRASEÑA PARA VER EL FUNCIONAMIENTO DEL CODIGO PARA QUE CUMPLA O NO CUMPLA AL SER VERIFICADO.
# Contraseña a validar
contraseña = "contraseña123"

# Verifica si hay al menos una letra mayúscula en la contraseña usando any() y una expresión generadora
if not any(c.isupper() for c in contraseña):
    # Si no hay ninguna letra mayúscula, imprime un mensaje de error
    print("La contraseña debe tener al menos una mayúscula")

#TODO:###############################################################################

# Nombre de archivo original
nombre_archivo = "documento.txt"

# Convierte el nombre del archivo a mayúsculas
nombre_archivo_mayusculas = nombre_archivo.upper()

print(nombre_archivo_mayusculas)

#TODO:###############################################################################

# Texto de ejemplo
texto = "Este es un texto de ejemplo"

# Divide el texto en palabras y crea una lista con las palabras que están completamente en mayúsculas
palabras_mayusculas = [palabra for palabra in texto.split() if palabra.isupper()]

print(palabras_mayusculas)

#TODO:###############################################################################

#PROGRAMA DE USO REAL DE PRUEBA
# Solicita al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Convierte la palabra a mayúsculas usando el método upper()
palabra_mayuscula = palabra.upper()

# Imprime la palabra convertida a mayúsculas
print("La palabra en mayúsculas es:", palabra_mayuscula)

