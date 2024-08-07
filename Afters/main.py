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

#Instanciados nuestros objetos
celular1 = Celular("Samsung", "S24", 100)
smartphone = Smartphone("Motorola", "G5", 50, "Android", 128)


celular1.encender()
smartphone.encender()

smartphone.instalar_aplicacion("Facebook")
celular1.apagar()


print(celular1)





if estado:
    print("encendido")
else:
    print("apagado")