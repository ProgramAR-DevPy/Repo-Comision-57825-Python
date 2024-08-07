
#!TITULOS DE ARTICULOS O LIBROS
titulo = "cien años de soledad"
titulo_formateado = titulo.capitalize()  # Convierte a "Cien años de soledad"
print(titulo_formateado)

#TODO: ################################################################################

#!NOMBRE DE VARIABLES EN CODIGO
variable_nombre = "nombreDelUsuario"
variable_nombre_formateada = variable_nombre.capitalize()  # Convierte a "Nombredelusuario"
print(variable_nombre_formateada) 

#TODO: ################################################################################

#!FORMATEO DE DATOS PARA EL USUARIO
ciudad = "buenos aires"
ciudad_formateada = ciudad.capitalize()  # Convierte a "Buenos aires"
print("La ciudad es:", ciudad_formateada)

#TODO: ################################################################################
#!PROGRAMA DE USO REAL
#!FORMATEO DE NOMBRES
def formatear_nombre(nombre_completo):
    """Formatea un nombre completo poniendo en mayúscula la primera letra de cada nombre y el resto en minúsculas."""
    nombres = nombre_completo.split()  # Divide el nombre completo en una lista de nombres
    nombres_formateados = [nombre.capitalize() for nombre in nombres]  # Formatea cada nombre individualmente
    return " ".join(nombres_formateados)  # Une los nombres formateados en una sola cadena

# Solicitar al usuario que ingrese su nombre completo
nombre_completo = input("Ingresa tu nombre completo: ")

# Formatear el nombre y mostrarlo por pantalla
nombre_formateado = formatear_nombre(nombre_completo)
print("Tu nombre formateado es:", nombre_formateado)
