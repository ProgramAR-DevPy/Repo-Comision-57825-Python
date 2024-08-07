
#!CORRIGIENDO ERRORES TIPOGRAFICOS
titulo = "la guerra de las galaxias: el imperio contraataca"
titulo_corregido = titulo.title()  # Convierte a "La Guerra De Las Galaxias: El Imperio Contraataca"
print(titulo_corregido)

#TODO: ################################################################################
#!FORMATEO DE DATOS PARA EL USUARIO
direccion = input("Ingrese su dirección: ")
direccion_formateada = direccion.title()  # Pone en mayúscula la primera letra de cada palabra
print(direccion_formateada)

#TODO: ################################################################################
#!Generando nombres de archivos
nombre_base = "informe_de_ventas"
fecha = "2023-06-15"
nombre_archivo = f"{nombre_base}_{fecha}".title()  # Convierte a "Informe_De_Ventas_2023-06-15"
print(nombre_archivo)


#TODO: ################################################################################
#!PROGRAMA DE USO REAL
def formatear_nombre_ciudad(nombre_ciudad):
    """Formatea un nombre de ciudad para que tenga la primera letra de cada palabra en mayúscula."""
    return nombre_ciudad.title()

# Solicitar al usuario que ingrese el nombre de una ciudad
nombre_ciudad = input("Ingresa el nombre de una ciudad: ")

# Formatear el nombre de la ciudad
nombre_ciudad_formateado = formatear_nombre_ciudad(nombre_ciudad)

# Mostrar el nombre formateado
print("El nombre de la ciudad formateado es:", nombre_ciudad_formateado)



