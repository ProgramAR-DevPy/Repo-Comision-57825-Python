# class Perro:
#     def __init__(self, nombre, raza, edad):  # Constructor
#         self.nombre = nombre
#         self.raza = raza
#         self.edad = edad


# mi_perro = Perro("Fido", "Labrador", 5)

# perro = Perro("Nilak", "Siberian Husky", 2)


# print(mi_perro.nombre)  # Output: Fido
# print(mi_perro.raza)    # Output: Labrador
# print(mi_perro.edad)     # Output: 5
# print(perro.nombre)  
# print(perro.raza)   
# print(perro.edad)    


# class Perro2:
   
#     def __init__(self, nombre, raza, edad):
#         self.nombre = nombre
#         self.raza = raza
#         self.edad = edad

#     def ladrar(self):
#         print("guau")

# perro22 = Perro2("Siberia", "Siberian Husky", 5)

# print(perro22.nombre)




# #__getitem__ y __setitem__
# """
# __getitem__: Permite acceder a los elementos de mi_lista utilizando índices.
# __setitem__: Permite modificar los elementos de mi_lista utilizando índices.
# """
# class MiLista:
#     def __init__(self, elementos):
#         self._elementos = elementos

#     def __getitem__(self, indice):
#         return self._elementos[indice]

#     def __setitem__(self, indice, valor):
#         self._elementos[indice] = valor

# mi_lista = MiLista([1, 2, 3])
# print(mi_lista[1])  # Output: 2

# mi_lista[1] = 10
# print(mi_lista[1])  # Output: 10











# #get y set
# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad

#     def get_nombre(self):
#         return self._nombre

#     def set_nombre(self, nuevo_nombre):
#         self._nombre = nuevo_nombre

#     def get_edad(self):
#         return self._edad

#     def set_edad(self, nueva_edad):
#         if nueva_edad >= 0:
#             self._edad = nueva_edad
#         else:
#             raise ValueError("La edad no puede ser negativa")

# persona = Persona("Ana", 30)
# print(persona.get_nombre())  # Output: Ana
# persona.set_nombre("María")
# print(persona.get_nombre())  # Output: María

# print(persona.get_edad())   # Output: 30
# persona.set_edad(35)
# print(persona.get_edad())   # Output: 35
# # persona.set_edad(-5)       # Lanzaría un ValueError


# class MiLista:
#     def __init__(self, elementos):
#         self._elementos = elementos

#     def __getitem__(self, indice):
#         return self._elementos[indice]

#     def __setitem__(self, indice, valor):
#         self._elementos[indice] = valor  # Sobreescribe el valor existente

# mi_lista = MiLista([1, 2, 3])
# print(mi_lista[1])  # Output: 2
# mi_lista[1] = 10
# print(mi_lista[1])  # Output: 10 (El valor 2 ha sido sobreescrito por 10)










#EJEMPLO CLASE VECTOR COMPLETO
class Vector:
    def __init__(self, datos):
        self._datos = datos

    def __str__(self):
        return f"Vector: {self._datos}"

    def __len__(self):
        return len(self._datos)

    def __getitem__(self, indice):
        return self._datos[indice]

    def __setitem__(self, indice, valor):
        self._datos[indice] = valor

    def __iter__(self):
        return iter(self._datos)
    
# Crear un objeto Vector
v = Vector([5, 10, 15, 20])

# __str__
print("Usando __str__")
print(v)  # Output: Vector: [5, 10, 15, 20]

# __len__
print("Usando __len__")
print(len(v))  # Output: 4

# __getitem__
print("Usando __getitem__")
print(v[2])  # Output: 15

# __setitem__
print("Usando __setitem__")
v[2] = 100
print(v)  # Output: Vector: [5, 10, 100, 20]

# __iter__
print("Usando __iter__")
for elemento in v:
    print(elemento)  # Output: 5, 10, 100, 20
    print(type(elemento))




# """
# Consigna: Implementar la Clase de Alumno, creada en la actividad anterior, directamente en Python. 
# Aclaraciones Generales:
# El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
# El método resultado, evalúa la nota correspondiente del estudiante. Si el estudiante saca menos de 5 puntos desaprueba la materia, más de 5 puntos aprueba. Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.
# Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno.
# """
# #EJERCICIO
# #Luego vamos a jugar con el __str__
# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota

#     def imprimir(self):
#         print(f"Nombre: {self.nombre}, Nota: {self.nota}")

#     def resultado(self):
#         if self.nota >= 5:
#             print("Aprobado")
#         else:
#             print("Desaprobado")

# # Crear instancias de la clase Alumno
# alumno1 = Alumno("Juan", 8)
# alumno2 = Alumno("María", 4)

# # Imprimir datos de los alumnos
# alumno1.imprimir()
# alumno2.imprimir()

# # Mostrar resultados
# alumno1.resultado()
# alumno2.resultado()


# #como es eso del __str__
# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota

#     def __str__(self):
#         return f"Alumno(nombre='{self.nombre}', nota={self.nota})"

#     def resultado(self):
#         if self.nota >= 5:
#             print("Aprobado")
#         else:
#             print("Desaprobado")

# # Crear instancias de la clase Alumno
# alumno1 = Alumno("Juan", 8)
# alumno2 = Alumno("María", 4)

# # Imprimir datos de los alumnos (usando print directamente)
# print(alumno1)  # Output: Alumno(nombre='Juan', nota=8)
# print(alumno2)  # Output: Alumno(nombre='María', nota=4)

# # Mostrar resultados
# alumno1.resultado()  # Output: Aprobado
# alumno2.resultado()  # Output: Desaprobado
