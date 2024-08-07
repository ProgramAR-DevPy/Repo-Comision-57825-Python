
# class Animal:  
#     def __init__(self, nombre, especie):
#         self.nombre = nombre
#         self.especie = especie

#     def hablar(self):
#         print("¡Sonido de animal!")

# class Perro(Animal):  
#     def hablar(self):
#         print("¡Guau!")

# class Gato(Animal):  
#     def hablar(self):
#         print("¡Miau!")

# class Animal:  # Clase padre
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def hablar(self):
#         print("Sonido genérico de animal")

#     def moverse(self):
#         print("Moverse de forma genérica")

#     def describirme(self):
#         print(f"Soy un animal llamado {self.nombre}")


# class Perro(Animal):  # Clase hija
#     def hablar(self):
#         print("Guau!")

#     def moverse(self):
#         print("Correr en cuatro patas")


# class Abeja(Animal):  # Otra clase hija
#     def hablar(self):
#         print("Bzzzz!")

#     def moverse(self):
#         print("Volar")

#     def picar(self):
#         print("¡Pique!")


# perro = Perro("Firulais")
# perro.describirme()  # Heredado directamente
# perro.hablar()       # Sobreescrito
# perro.moverse()      # Sobreescrito

# abeja = Abeja("Maya")
# abeja.describirme()  # Heredado directamente
# abeja.hablar()       # Sobreescrito
# abeja.moverse()      # Sobreescrito
# abeja.picar()        # Nuevo método



# class Animal:
#     def __init__(self, especie, edad):
#         self.especie = especie
#         self.edad = edad

# class Perro(Animal):
#     def __init__(self, especie, edad, dueño):
#         super().__init__(especie, edad)  # Llama al constructor de Animal
#         self.dueño = dueño


# class Animal:
#     def __init__(self, especie, edad):
#         self.especie = especie
#         self.edad =  edad

# class Perro(Animal):
#     def __init__(self, especie, edad, dueño):
#         super().__init__(especie, edad)
#         self.dueño = dueño


# class Volador:
#     def __init__(self, altura_maxima):
#         self.altura_maxima = altura_maxima

#     def volar(self):
#         print(f"Estoy Volando a {self.altura_maxima} metros ")

# class Nadador:
#     def __init__(self, profundidad_maxima):
#         self.profundidad_maxima = profundidad_maxima

#     def nadar(self):
#         print(f"Estoy  nadando a  {self.profundidad_maxima} metros de profundidad")

# class Pato(Volador, Nadador):
#     def __init__(self, altura_maxima, profundidad_maxima, nombre):
#         Volador.__init__(self, altura_maxima)
#         Nadador.__init__(self, profundidad_maxima)
#         self.nombre = nombre

#     def presentar(self):
#         print(f"Hola, soy {self.nombre}")
    
# mi_pato = Pato(50, 200, "Alejandro")

# mi_pato.volar()
# mi_pato.nadar()

# mi_pato.presentar()


# class Animal:
#     def hablar(self):
#         print("¡Sonido de animal!")

# class Mamifero(Animal):
#     def caminar(self):
#         print("¡Caminando!")

# class Perro(Mamifero):
#     def hablar(self):
#         print("¡Guau!")

# perro = Perro()
# perro.hablar()   # Output: ¡Guau!
# perro.caminar()  # Output: ¡Caminando!

# print(Perro.__mro__) 


class Animal:
    def hablar(self):
        print("¡Sonido de animal!")

class Perro(Animal):
    def hablar(self):
        print("¡Guau!")

class Gato(Animal):
    def hablar(self):
        print("¡Miau!")


# Creamos una lista de animales de diferentes tipos
animales = [Perro(), Gato(), Animal()]


# Hacemos que cada animal "hable" (polimorfismo en acción)
for animal in animales:
    animal.hablar()


