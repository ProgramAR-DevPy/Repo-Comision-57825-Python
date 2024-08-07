# # #Argumentos por posicion
# # # Calcular el área de un rectángulo
# # def calcular_area_rectangulo(base, altura):
# #     """
# #     Calcula el área de un rectángulo.

# #     Args:
# #         base: La longitud de la base del rectángulo.
# #         altura: La longitud de la altura del rectángulo.

# #     Returns:
# #         El área del rectángulo.
# #     """
# #     area = base * altura
# #     return area

# # # Llamada a la función con argumentos por posición
# # base = 5
# # altura = 10
# # area_rectangulo = calcular_area_rectangulo(base, altura)  # El primer argumento es la base, el segundo la altura
# # print("El área del rectángulo es:", area_rectangulo)  # Output: El área del rectángulo es: 50

# # #ARGUMENTOS POR NOMBRE
# # #Crear un perfil de usuario
# # def crear_perfil(nombre, edad, ciudad="Desconocida", intereses=None):
# #     """Crea un perfil de usuario con información personal."""

# #     perfil = {
# #         "nombre": nombre,
# #         "edad": edad,
# #         "ciudad": ciudad  # Valor por defecto "Desconocida" si no se proporciona
# #     }

# #     if intereses:  # Si se proporciona una lista de intereses, la agrega al perfil
# #         perfil["intereses"] = intereses

# #     return perfil

# # # Llamar a la función con argumentos por nombre
# # perfil_ana = crear_perfil(nombre="Ana", edad=30, intereses=["música", "cine"])
# # print(perfil_ana)  # Output: {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Desconocida', 'intereses': ['música', 'cine']}

# # perfil_juan = crear_perfil(edad=25, nombre="Juan", ciudad="Madrid")  # Orden diferente de argumentos
# # print(perfil_juan)  # Output: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}




# # def duplicar(numero):
# #     """Duplica un número."""
# #     numero *= 2
# #     print("Dentro de la función:", numero)

# # valor = 5
# # duplicar(valor)  # Se pasa una copia de 'valor'
# # print("Fuera de la función:", valor)  # El valor original no cambia


# # def agregar_elemento(lista, elemento):
# #     """Agrega un elemento a una lista."""
# #     lista.append(elemento)
# #     print("Dentro de la función:", lista)

# # mi_lista = [1, 2, 3]
# # agregar_elemento(mi_lista, 4)  # Se pasa una referencia a 'mi_lista'
# # print("Fuera de la función:", mi_lista)  # La lista original se modifica



# # #Ejemplo filmina
# # def suma(*args):
# #     s = 0
# #     for arg in args:
# #         s += arg
# #     return s

# # suma(1, 3, 4, 2)
# # #salida 10

# # suma(1, 1)
# # #salida 2

# # def suma(*args):
# #     return sum(args)

# # suma(5, 5, 3)


# # def contar_hasta_cero(numero):
# #     if numero < 0:  # detener la recursión si el número es negativo
# #         return

# #     print(numero)  # Realizar una acción (imprimir el número)
# #     contar_hasta_cero(numero - 1)  # Llamada recursiva con un número menor

# # contar_hasta_cero(10)

# # def saludar(nombre, mensaje):  # nombre y mensaje son parámetros
# #     """Imprime un saludo personalizado."""
# #     return (f"¡Hola, {nombre}! {mensaje}")





# # #saludar("Ana", "Bienvenido/a")  # "Ana" y "Bienvenido/a" son argumentos

# # print(saludar("Devolveme la plata", "Jose"))



# def resta(a, b):
#     """Resta dos números y devuelve el resultado."""
#     return a - b

# resultado = resta(b=15, a=12)  # Asignamos 15 a b y 12 a a
# print(resultado)  # Output: -3


# def resta(a, b):
#     """Resta dos números y devuelve el resultado."""
#     return a - b

# resultado = resta()

# print(resultado)

# def resta(a=100, b=50):  # a y b tienen valores por defecto
#     """Resta dos números y devuelve el resultado."""
#     return a - b

# resultado = resta()  # No se pasan argumentos, se usan los valores por defecto
# print(resultado)  # Output: 5


# def resta(a=10, b=5):  # a y b tienen valores por defecto
#     """Resta dos números y devuelve el resultado."""
#     return a - b

# resultado = resta()  # No se pasan argumentos, se usan los valores por defecto
# print(resultado)  # Output: 5

# resultado = resta(20)  # Se pasa un argumento para a, b usa el valor por defecto
# print(resultado)  # Output: 15 

# resultado = resta(b=8)  # Se pasa un argumento por nombre para b, a usa el valor por defecto
# print(resultado)  # Output: 2


# def duplicar(numero):
#     """Duplica un número."""
#     numero *= 2
#     print("Dentro de la función:", numero)

# valor = 5
# duplicar(valor)  # Se pasa una copia de 'valor'
# print("Fuera de la función:", valor )  # El valor original no cambia

# def agregar_elemento(lista, elemento):
#     """Agrega un elemento a una lista."""
#     lista.append(elemento)
#     print("Dentro de la función:", lista)

# mi_lista = [1, 2, 3]
# agregar_elemento(mi_lista, 4)  # Se pasa una referencia a 'mi_lista'
# print("Fuera de la función:", mi_lista)  # La lista original se modifica


# def suma(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# resultado = suma(1, 1, 1, 1, 1)
# print(resultado)  # Output: 10


# def mostrar_informacion(**kwargs):
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# mostrar_informacion(nombre="Ana", edad=30, ciudad="Madrid")

# def suma_lista(lista):
#     """Calcula la suma de los elementos de una lista de forma recursiva."""
#     if not lista:  # Caso base: si la lista está vacía, la suma es 0
#         return 0
#     else:
#         return lista[0] + suma_lista(lista[1:])  # Llamada recursiva con el resto de la lista

# # Ejemplo de uso:
# mi_lista = [1, 2, 3, 4, 5]
# resultado = suma_lista(mi_lista)
# print(resultado)  # Output: 15

def cuenta_regresiva(numero):
   
    if numero <= 0:  
        return  print("nada mas")

    print(numero)    
    cuenta_regresiva(numero - 1)  # Llamada recursiva con el número disminuido en 1

# Ejemplo de uso:
cuenta_regresiva(50)