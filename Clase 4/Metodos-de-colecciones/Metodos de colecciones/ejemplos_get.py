
# #!OBTENER UN VALOR SON ESPECIFICAR UNA RESPUESTA POR DEFECTO
# colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
# color_rojo = colores.get("rojo")  # No se especifica valor por defecto, devuelve None
# print(color_rojo)  # Output: None

# #!BUSCAR DATOS DE UNA BASE DE DATOS(BD) SIMULADA
# usuarios = {
#     "123": {"nombre": "Ana", "edad": 30},
#     "456": {"nombre": "Juan", "edad": 25}
# }
# id_usuario = "456"
# datos_usuario = usuarios.get(id_usuario, {"error": "Usuario no encontrado"})  # Si no existe, devuelve un diccionario de error
# print(datos_usuario)  # Output: {'nombre': 'Juan', 'edad': 25}

#!PROGRAMA DE USO REAL
#!TRADUCTOR
diccionario_espanol_ingles = {
    "hola": "hello",
    "gato": "cat",
    "perro": "dog"
}

def traducir_palabra(palabra):
    """Traduce una palabra del español al inglés."""
    traduccion = diccionario_espanol_ingles.get(palabra.lower(), "Palabra no encontrada")  # Convertimos a minúsculas para evitar errores
    return traduccion

# Solicitar al usuario una palabra en español
palabra_espanol = input("Ingresa una palabra en español: ")

# Traducir y mostrar el resultado
traduccion_ingles = traducir_palabra(palabra_espanol)
print(f"La traducción al inglés de '{palabra_espanol}' es: {traduccion_ingles}")
