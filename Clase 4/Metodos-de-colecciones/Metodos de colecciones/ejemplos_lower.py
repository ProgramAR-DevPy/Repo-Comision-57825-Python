# Lista original de nombres con mayúsculas y minúsculas mezcladas
nombres = ["ANA", "Juan", "MARÍA"]

# Crea una nueva lista aplicando el método lower() a cada nombre de la lista original
nombres_normalizados = [nombre.lower() for nombre in nombres]

# Imprime la lista resultante con todos los nombres en minúsculas
print(nombres_normalizados)  # Output: ['ana', 'juan', 'maría']

#TODO:####################################################################

# # Dos palabras para comparar
palabra1 = "Hola"
palabra2 = "hOlA"

# Compara las palabras convertidas a minúsculas
if palabra1.lower() == palabra2.lower():
    # Si son iguales (ignorando mayúsculas/minúsculas), imprime el mensaje
    print("Las palabras son iguales (ignorando mayúsculas/minúsculas)")


#TODO: ####################################################################

# Texto en el que se buscará
texto = "Este es un texto de Ejemplo"

# Palabra a buscar
busqueda = "ejemplo"

# Convierte el texto y la palabra a minúsculas y verifica si la palabra está en el texto
if busqueda.lower() in texto.lower():
    # Si se encuentra, imprime el mensaje
    print("La palabra 'ejemplo' se encuentra en el texto")

#TODO: ####################################################################

# Solicita al usuario una respuesta (s/n)
respuesta = input("¿Quieres continuar? (s/n): ")

# Convierte la respuesta a minúsculas y verifica si es "s"
if respuesta.lower() == "s":
    # Si es "s", imprime el mensaje
    print("Continuando...")

#TODO ####################################################################

# Nombre de archivo original
nombre_archivo = "ARCHIVO.TXT"

# Convierte el nombre del archivo a minúsculas
nombre_archivo_minusculas = nombre_archivo.lower()

# Imprime el nombre del archivo en minúsculas
print(nombre_archivo_minusculas)  # Output: archivo.txt


#TODO:###################################################################

def buscar_palabra_en_frase(frase, palabra_buscada):
    """Busca una palabra en una frase sin distinguir mayúsculas/minúsculas."""
    frase_minusculas = frase.lower()  # Convierte la frase a minúsculas
    palabra_buscada_minusculas = palabra_buscada.lower()  # Convierte la palabra buscada a minúsculas

    if palabra_buscada_minusculas in frase_minusculas:  # Busca la palabra en la frase en minúsculas
        return True
    else:
        return False

# Solicitar al usuario una frase y una palabra a buscar
frase = input("Ingresa una frase: ")
palabra_buscada = input("Ingresa la palabra que quieres buscar: ")

# Llamar a la función para realizar la búsqueda
if buscar_palabra_en_frase(frase, palabra_buscada):
    print("La palabra", palabra_buscada, "se encuentra en la frase.")
else:
    print("La palabra", palabra_buscada, "no se encuentra en la frase.")

