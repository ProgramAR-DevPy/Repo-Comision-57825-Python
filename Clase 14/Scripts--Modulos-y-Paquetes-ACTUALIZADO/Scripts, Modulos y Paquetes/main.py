# # import sys

# # nombre = sys.argv[1]  # Obtenemos el primer argumento
# # print(f"¡Hola, {nombre}!")

# import sys
# print(sys.argv)

# import alumno


# estudiante = alumno.Alumno("Jose", 150)

# estudiante.imprimir()


# from mi_primer_paquete.modulo1 import saludar
# from mi_primer_paquete.modulo2 import despedirse

# # main.py
# from mi_primer_paquete import modulo1, modulo2

# modulo1.saludar("Alice")  # Output: ¡Hola, Alice!
# modulo2.despedirse("Bob") # Output: ¡Adiós, Bob!


# from collections import namedtuple

# # Creamos una "clase" para representar peces
# Pez = namedtuple("Pez", ["nombre", "especie", "tanque"])

# # Creamos un objeto Pez
# nemo = Pez("Nemo", "Pez payaso", "Arrecife")

# print(nemo.nombre)  # Output: Nemo
# print(nemo.especie) # Output: Pez payaso


from datetime import datetime, timedelta

ahora = datetime.now()
print(ahora)  # Output: 2024-07-23 11:01:32.789101 (o similar)

# Sumar 5 días a la fecha actual
dentro_de_5_dias = ahora + timedelta(days=10)
print(dentro_de_5_dias)




















































