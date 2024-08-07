#Primer Programa en Python
#Notas del alumno
nota_1 = float(input("Ingrese por favor la nota 1: "))
nota_2 = float(input("Ingrese por favor la nota 2: "))
nota_3 = float(input("Ingrese por favor la nota 3: "))

#Promedios de las notas

promedio_nota_1 = (nota_1*20) / 100
promedio_nota_2 = (nota_2*30) / 100
promedio_nota_3 = (nota_3*50) / 100

#Calculo de nota final
nota_final = promedio_nota_1 + promedio_nota_2 + promedio_nota_3

#Muestro la nota final del alumno
print ("La nota final del alumno es de:",nota_final)
