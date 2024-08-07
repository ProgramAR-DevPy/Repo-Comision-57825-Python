#Ejemplo básico de if:

"""
indentacion = termino correcto
identacion = termino equivocado
"""

x = 10

if x % 2 == 0:
    print("Es par")
else:
    print("Es Impar")







temperatura = 35
if temperatura > 30:
    print('Hace mucho calor')

#Ejemplo de if con una condición siempre verdadera:

if 5 > 3:
    print('5 es mayor que 3')

#Ejemplo con elif y else:

edad = 20
if edad < 18:
    print('Es un adolescente')


elif 18 <= edad < 65:
    print('Es un adulto')
else:
    print('Es un adulto mayor')

#Uso de operadores lógicos and y or:
a = 10
b = 5
c = 15
if a > b and a < c:
    print("a está entre b y c")

#Ejemplo con or:
a = 8
b = 12
c = 6
if a > b or a > c:
    print("a es mayor que b o c")

#Uso de operador lógico not:
y = 7
if not y == 5:
    print("y no es igual a 5")

#if en una sola línea:
#Ejemplo 1:
x = 100
y = 50
if x > y: print("x es mayor que y")

#Ejemplo 2:
a = 10
b = 20
print("A es mayor") if a > b else print("B es mayor")

#Ejemplo 3:
a = 30
b = 30
print("A es mayor") if a > b else print("Iguales") if a == b else print("B es mayor")


#Ejemplo de else:
numero = 10
if numero > 20:
    print("El número es mayor que 20")
else:
    print("El número es 20 o menor")


#Ejemplo de if anidado:
#Ejemplo 1:
valor = 35
if valor > 30:
    print("por encima de treinta,")
    if valor > 40:
        print("y también por encima de 40!")
    else:
        print("pero no por encima de 40")

#Ejemplo 2:
valor = 25
if valor > 20:
    print("por encima de veinte,")
    if valor > 30:
        print("y también por encima de 30!")
    else:
        print("pero no por encima de 30")

#Ejemplo de elif:
comando = "CHANCHITO FELIZ"
if comando == "INICIAR":
    print("Iniciando el sistema...")
elif comando == "PAUSAR":
    print("Pausando el sistema...")
elif comando == "DETENER":
    print("Deteniendo el sistema...")
else:
    print("Comando no reconocido")



#CUAL ES EL RESULTADO DE ESTE BLOQUE DE CODIGO?

a = 2 + 4
if a == 4: 
   print ("A es igual a cuatro")
elif a == 5:
   print ("A es igual a cinco")
elif a == 6:
   print ("A es igual a seis")
else:
   print ("No se cumple la condición")

#TODO: ######################################################################
"""
Descripción de la actividad. 

Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado. 
Trabajarán con el notebook de clase Clase_4.ipynb

Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: “No existe generación asociada”


"""



#EJERCICIOS DE LA CLASE
#Generaciones Digitales
anio = int(input("Ingrese su año de nacimiento: "))

if anio >= 2001 and anio <= 2010:
    print("Generación Z")

elif anio >= 1980 and anio <= 2000:
    print("Generación Y")

elif anio >= 1965 and anio <= 1979:
    print("Generacion X")

elif anio >= 1946 and anio <= 1964:
    print("Baby Boomer")
    
elif anio >= 1920 and anio <= 1940:
    print("Generación Silenciosa")
else:
    print("No clasificado")


#Crédito bancario
"""
Descripción de la actividad. 

Para aprobar un crédito, el cliente debe ser mayor de edad. Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.  En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. Si no cumple ninguna de las condiciones, no se aprueba el crédito

Datos iniciales
edad = 15
antigüedad = 10
ingreso = 1500

"""


edad = 18
antiguedad = 2
ingreso = 3999

if edad >= 18:

    if antiguedad >= 3 and ingreso >= 2500:
        print("Aprobado por el Ale")
    
    elif ingreso >= 4000:
        print("Aprobado por El jefe")

    else:
        print("No aprobado por el otro Ale")

else:
    print("No aprobado")


#Marvel vs Capcom
"""
Un curso se ha dividido en dos grupos diferentes: A y B de acuerdo al nombre y a una preferencia (Marvel o Capcom). El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla el grupo que le corresponde.
Ej.:
¿Cómo te llamas?  Alan
¿Cuál es tu preferencia (M o C)?  C
Tu grupo es B
Para preguntarle al usuario, recuerda usar input.

"""

nombre = input("¿Cómo te llamas?: ")
fan = input("¿Cuál es tu preferencia (Marvel o Capcom)?: ")

if (fan == "Marvel" and nombre < "M") or (fan == "Capcom" and nombre > "N"):

  print("SOS DEL GRUPO A")

else: 

  print("Sos del epico grupo B!!!!!!!!!")

  ##############################################
