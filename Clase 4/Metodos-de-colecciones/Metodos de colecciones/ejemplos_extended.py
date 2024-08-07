
# #!UNIENDO LISTAS DE CADENAS
# nombres = ["Alice", "Bob"]
# apellidos = ["Smith", "Johnson"]
# nombres_completos = []
# nombres_completos.extend(nombres)  # Extiende la lista vacía con los nombres
# nombres_completos.extend(apellidos)  # Extiende la lista con los apellidos
# print(nombres_completos)  # Output: ['Alice', 'Bob', 'Smith', 'Johnson']

# #!AGREGAR CARACTERES DE UNA CADENA A UNA LISTA
# letras = ['a', 'b', 'c']
# palabra = "def"
# letras.extend(palabra)  # Extiende la lista letras con los caracteres de la cadena palabra
# print(letras)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']


#!EJEMPLO DE PROGRAMA REAL
def consolidar_listas_tareas(lista_tareas_principal, *otras_listas):
    """Consolida múltiples listas de tareas en una sola lista principal."""
    for lista in otras_listas:
        lista_tareas_principal.extend(lista)  # Extiende la lista principal con cada lista adicional

# Listas de tareas iniciales
tareas_personales = ["Comprar leche", "Pagar facturas"]
tareas_trabajo = ["Terminar informe", "Enviar correo"]
tareas_hogar = ["Limpiar cocina", "Lavar ropa"]

# Consolidar todas las listas en la lista principal
consolidar_listas_tareas(tareas_personales, tareas_trabajo, tareas_hogar)

# Mostrar la lista consolidada
print("Lista de tareas consolidada:")
for tarea in tareas_personales:
    print("- ", tarea)



