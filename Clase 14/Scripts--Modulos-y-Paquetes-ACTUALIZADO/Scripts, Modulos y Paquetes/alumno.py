class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Alumno: {self.nombre} Nota: {self.nota}")