# #llename por favor. Tengo hambre xD

# print("Hola")  # "(" no estaba cerrado.(SyntaxError: unterminated string literal (detected at line 1))
# #print('Hola")  # "(" no estaba cerrado (SyntaxError: unterminated string literal (detected at line 2))


# if True:
#     print("Hola")  # Bloque con sangría previsto (IndentationError: expected an indented block after 'if' statement on line 1)

# def mi_funcion():
#     print("Hola")  # Se esperaba ":" (SyntaxError: expected ':')



# lista_vacia = []
# elemento = lista_vacia[0]  # Error:  IndexError, la lista está vacía por lo que da fuera de rango (IndexError: list index out of range)

# print(elemento)

# edad = input("Ingresa tu edad: ")
# edad_doble = edad / 2  # No tira error pero no va a ser el resultado esperado ya que va a repetir 2 veces lo que se ponga en el input

# print(edad_doble)


# try:
#     resultado = 10 / 0
# except ZeroDivisionError:
#     print("¡Error! No puedes dividir por cero.")
#     print("Hola mundo")


# try:
#     resultado = 10 / int(input("Ingresa un número: "))
# except ZeroDivisionError:
#     print("¡Error! No puedes dividir por cero.")
# except ValueError:
#     print("¡Error! Debes ingresar un número válido.")



# while True:
#     try:
#         a = float(input("Introduce un número: "))
#         b = float(input("Introduce otro número: "))
#         print(a + b)
#     except ValueError:
#         print("¡Error! Debes introducir números válidos.")
#     else:
#         print("¡La suma se realizó correctamente!")
#         break  # Salimos del bucle si todo salió bien


# try:
#     resultado = 10 / 0  # División por cero (genera una excepción ZeroDivisionError)
# except ZeroDivisionError:
#     print("Error: No se puede dividir por cero.")
# finally:
#     print("Esta línea siempre se imprime, incluso con el error.")

# print(type(1))
# print(type(3.14))
# print(type([]))
# print(type(()))


# print(type(1).__name__)
# print(type(3.14).__name__)
# print(type([]).__name__)
# print(type(()).__name__)


# try:
#     n = "hola"
#     5 / n
# except TypeError:
#     print("¡Error! No puedes dividir un número por una cadena de texto.")
# except ValueError:
#     print("¡Error! Debes introducir un número válido.")
# except ZeroDivisionError:
#     print("¡Error! No puedes dividir por cero.")
# except Exception as e:  # Captura cualquier otra excepción
#     print(f"¡Error inesperado! {type(e).__name__}: {e}")



#PRIMER EJERCICIO EN CLASE Desafío de errores
"""
Descripción de la actividad. 

Tomando la solución del ejercicio anterior, en lugar de devolver None al dividir entre cero, tienes que capturar una excepción que muestre por pantalla EXACTAMENTE el mensaje: “No se puede dividir entre cero”; si falla el código

"""
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
     
        return "No se puede dividir por cero"
    else:
        return resultado

#resultado1 = dividir(10, 2)
resultado2 = dividir(8, 0)

print( resultado2)