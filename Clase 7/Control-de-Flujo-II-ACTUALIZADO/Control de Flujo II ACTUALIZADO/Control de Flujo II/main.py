#Ejemplos de break
#Ejemplo 1 Deteniendo el bucle
numeros = [1, 5, 3, 8, 2]
numero_buscado = 3

for num in numeros:
    if num == numero_buscado:
        print(f"¡Encontramos el número {numero_buscado}!")
        break
else:  # Esta parte se ejecuta si el bucle termina sin encontrar el número
    print(f"El número {numero_buscado} no está en la lista.")


#Ejemplo 2 Rompiendo un bucle infinito (condicionalmente)
contador = 1

while True:
    print(contador)
    contador += 1
    if contador > 10:
        break 

#Ejemplos continue
#Ejemplo 1 Imprimiendo solo números pares

for num in range(1, 15, 2):
    print(num)  # Imprimir solo los números pares


#Ejemplo 2 Ignorando errores en un bucle
#Agregar el cero
datos = [1, 2, 'error', 4, 5]

for dato in datos:
    try:
        resultado = 10 / dato
        print(resultado)
    except ZeroDivisionError:
        print("¡Error! No se puede dividir por cero.")
        continue  # Saltar a la siguiente iteración si hay un error
    except TypeError:
        print("¡Error! Tipo de dato no soportado para la división.")
        continue  # Saltar a la siguiente iteración si hay un error


#Ejemplos pass
#Ejemplo 1: Marcador de posición para una función futura

def mi_funcion():
    pass  # Esta función no hace nada por ahora


#Ejemplo 2: Bloque vacío en una estructura condicional
if True:
    pass  # No hacer nada si la condición es verdadera
else:
    print("Esto no se imprimirá")

#Script de Ejemplo con pass
def procesar_datos(datos):
    for dato in datos:
        if dato == "valor_especial":
            # Aquí iría el código para manejar el valor especial, pero aún no está implementado
            pass
        else:
            print(f"Procesando dato: {dato}")

datos = ["valor1", "valor2", "valor_especial", "valor4"]
procesar_datos(datos)



#PARA PENSAR ¿QUE PASA EN ESTE EJEMPLO?
c = -3
while c < 10:
    c += 1
    if c == 2:
        pass
    print('c vale', c)





#ACTIVIDAD MANU CHAO
# Lista con los párrafos de la canción
letra = [
    "Me gustan los aviones, me gustas tú",
    "Me gusta viajar, me gustas tú",
    "Me gusta la mañana, me gustas tú",
    "Me gusta el viento, me gustas tú",
    "Me gusta soñar, me gustas tú",
    "Me gusta la mar, me gustas tú",
    "¿Qué voy a hacer? Je ne sais pas",
    "¿Qué voy a hacer? Je ne sais plus",
    "¿Qué voy a hacer? Je suis perdu",
    "¿Qué horas son, mi corazón?",
    "Me gusta la moto, me gustas tú",
    "Me gusta correr, me gustas tú",
    "Me gusta la lluvia, me gustas tú",
    "Me gusta volver, me gustas tú",
    "Me gusta marihuana, me gustas tú",
    "Me gusta colombiana, me gustas tú",
    "Me gusta la montaña, me gustas tú",
    "Me gusta la noche, me gustas tú"
]

# Iteración sobre la lista e impresión de cada párrafo
for verso in letra:
    print(verso)






#ACTIVIDAD EN CLASE
"""
Descripción de la actividad. 

Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente utilizando la función input (). 

Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit(). El programa debe validar dicha acción. 

Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida.



"""



suma_total = 0
suma_parcial = 0

while True:
    numero_str = input("Ingresa un número entero (o 'exit' para terminar): ")

    # Verificar si el usuario quiere salir
    if numero_str.lower() == "exit":
        break

    # Intentar convertir la entrada a un número entero
    try:
        numero = int(numero_str)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        continue  # Volver al inicio del bucle si la entrada no es válida

    # Actualizar las sumas
    suma_parcial += numero
    suma_total += numero

    # Mostrar la suma parcial
    print(f"Suma parcial: {suma_parcial}")





















# Mostrar la suma total al final
print(f"\nSuma total: {suma_total}")


# 1. Definimos una variable llamada "valor" y le asignamos el valor 5.
valor = 5  

# 2. Creamos un string con dos marcadores de posición `{}`.
cadena_de_caracteres = "La suma de {} más 10 es: {}"  

# 3. Llamamos al método `.format()` y le pasamos dos argumentos:
#   - El primer argumento (valor) reemplazará el primer marcador de posición.
#   - El segundo argumento (valor + 10) reemplazará el segundo marcador de posición.
cadena_de_caracteres = cadena_de_caracteres.format(valor, valor + 10)  

# 4. Imprimimos el string resultante, donde los marcadores de posición han sido reemplazados
# por los valores proporcionados.
print(cadena_de_caracteres)  # Output: La suma de 5 más 10 es: 15


num = 5
while num >= -1:
    print(f'{num}')
    num -= 1


# 1. Inicialización: Creamos una variable llamada "contador" y le asignamos el valor inicial 0.
# Esta variable nos servirá para controlar cuántas veces se repite el bucle.
contador = 1 

# 2. Bucle While: Iniciamos el bucle while con la condición "contador < 5".
# Esto significa que el bucle se ejecutará mientras el valor de "contador" sea menor que 5.
while contador < 5:  

    # 3. Cuerpo del bucle: El código dentro del bucle se ejecuta en cada iteración.
    # En este caso, imprimimos el mensaje "¡Hola!" en la pantalla.
    print("¡Hola!")  

    # 4. Actualización del contador: Incrementamos el valor de "contador" en 1.
    # Esto es crucial para que la condición del bucle eventualmente se vuelva falsa y el bucle termine.
    contador = contador + 1 


# 1. Inicializamos la variable "intentos" con el valor 1.
intentos = 1  

# 2. Iniciamos el bucle while. La condición es "intentos <= 3", lo que significa que el
# bucle se ejecutará mientras el valor de "intentos" sea menor o igual a 3.
while intentos <= 3:  
    # 3. Cuerpo del bucle:
    #   - Pedimos al usuario que ingrese una respuesta.
    respuesta = input("¿Cuál es la capital de Francia? ")  

    #   - Verificamos si la respuesta es correcta.
    if respuesta.lower() == "paris":  
        #   - Si la respuesta es correcta, imprimimos un mensaje de éxito y salimos del bucle
        #     con "break".
        print(f"¡Correcto! Lo lograste en el intento {intentos}")  
        break  
    else:
        #   - Si la respuesta es incorrecta, imprimimos un mensaje de error y aumentamos
        #     el contador de intentos.
        print("Incorrecto. Intenta de nuevo.")  
    intentos += 1  

# 4. else:
#   - Si el bucle while termina de forma natural (es decir, si se agotaron los 3 intentos
#     sin adivinar la respuesta), se ejecuta el código dentro del "else".
else:  
    print("Agotaste tus tres intentos. ¡La respuesta era París!")  


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#PASS
#Ejemplo 1
n = 0  #DEFINIMOS LA VARIABLE Y ASIGNAMOS 0
while n < 10:  #MIENTRAS N MENOR QUE 10 ENTRA AL BUCLE 
    n += 1  #INCREMENTA 1 A N
    if n == 2: ##SI N ES IGUAL A 2
        pass
    print('n vale' , n)


#FOR
# 1. Creamos una lista llamada "numeros" con los números del 1 al 5.
numeros = (1, 2, 3, 4, 5)  

# 2. Iniciamos el bucle for. La variable "valor" tomará el valor de cada elemento de la lista
# en cada iteración.
for i in numeros:  
    # 3. Cuerpo del bucle: Imprimimos un mensaje que muestra el valor actual de "valor".
    print("Soy un ítem de la lista y valgo", i) 



# 1. Creamos una lista de frutas.
frutas = ["manzana", "banana", "naranja"]  

# 2. Usamos enumerate() para recorrer la lista y obtener tanto el índice como el valor de cada elemento.
for i, j in enumerate(frutas):  
    # 3. Imprimimos el índice y el valor en cada iteración.
    print(f"En la posición {i} está la fruta: {j}")