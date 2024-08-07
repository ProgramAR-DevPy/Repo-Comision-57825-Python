#Clase: Auto
"""
Las clases por convencion en python se escriben en pascal case (primera letra de cada palabra del nombre en mayuscula)
"""

class Auto:  #Definimos la clase Auto
    def __init__(self, marca, modelo, color):  #SELf: https://ejemplos.net/que-significa-self-en-python/
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def alecerar(self):  #metodo acelerar
        print("¡Vruuum!")

    def frenar(self):  #metodo frenar
        print("¡Screeech!")

#Instanciar mi objeto
auto1 = Auto("fiat","palio", "verde" )
auto2 = Auto("toyota", "corolla", "azul")

auto1.alecerar()
auto2.frenar()


#Clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.disponible = True
        
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

cien_anios = Libro("Cien años de soledad", "Gabriel García Márquez", "9788420471839", "Novela")
rayuela = Libro("Rayuela", "Julio Cortázar", "9789500397240", "Novela")

cien_anios.prestar()  # El libro 'Cien años de soledad' ha sido prestado.
rayuela.prestar()     # El libro 'Rayuela' ha sido prestado.
cien_anios.devolver() # El libro 'Cien años de soledad' ha sido devuelto.