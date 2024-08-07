#Clase Padre
class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.__encendido = False #Privado no puedo acceder desde afuera

    def encender(self):
        self.__encendido = True
        print(f"El {self.marca} {self.modelo} se encendió")

    def apagar(self):
        self.__encendido = False
        print(f"El {self.marca} {self.modelo} se apagó")

    def __str__(self):
        estado = "encendido" if self.__encendido else "apagado"
        return f"Celular {self.marca} {self.modelo} {estado} - Y su precio es: ${self.precio}"
    


#Clase Hija
class Smartphone(Celular):
    def __init__(self, marca, modelo, precio, sistema_operativo, almacenamiento):
        super().__init__(marca, modelo, precio)
        self.sistema_operativo = sistema_operativo
        self.almacenamiento = almacenamiento

    def instalar_aplicacion(self, nombre_aplicacion):
        print(f" Instalando {nombre_aplicacion} en el celular {self.marca} {self.modelo}")




# #Instanciados nuestros objetos
celular1 = Celular("Samsung", "S24", 100)
smartphone = Smartphone("Motorola", "G5", 50, "Android", 128)


celular1.encender()
smartphone.encender()

smartphone.instalar_aplicacion("Whatsapp")
celular1.apagar()


print(celular1)

##################################################
# class Pato:
#     def hablar(self):
#         print("¡Cua Cua!")

# class Perro:
#     def hablar(self):
#         print("¡Guau!")

# class Gato:
#     def hablar(self):
#         print("¡Miau!")

# def hacer_hablar(animal):
#     animal.hablar()

# pato = Pato()
# perro = Perro()
# gato = Gato()

# hacer_hablar(pato)   # Output: ¡Cua Cua!
# hacer_hablar(perro)  # Output: ¡Guau!
# hacer_hablar(gato)   # Output: ¡Miau!


class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def __hablar(self):  # Método privado
        print("Este es el método hablar (privado).")

    def moverse(self):
        print("Este es el método moverse (público).")

class Perro(Animal):
    pass  # Perro hereda de Animal, pero no puede acceder a __hablar()

perro1 = Perro("Mamífero", 11)

perro1.moverse()       # Output: Este es el método moverse (público).
perro1.__hablar()      # Error: AttributeError: 'Perro' object has no attribute '__hablar'