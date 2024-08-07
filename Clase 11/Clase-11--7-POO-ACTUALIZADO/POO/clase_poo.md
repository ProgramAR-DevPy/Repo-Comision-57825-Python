# Programación Orientada a Objetos (POO): ¡El Mundo como lo Conoces! 🌎
### ¿Qué es la POO? 🤔
Imagina que estás construyendo una ciudad con LEGO. En lugar de tener un montón de piezas sueltas, la POO te permite crear diferentes tipos de bloques (clases) como casas, autos y personas. Cada tipo de bloque tiene sus propias características (atributos) como color, tamaño y funciones (métodos) como moverse, abrir puertas o hacer sonidos.

### ¿Por qué usar POO? 🏗️
- **Organización:** Al igual que una ciudad bien planificada, la POO te ayuda a organizar tu código en bloques lógicos y reutilizables.
- **Reutilización:** Puedes usar tus bloques (clases) una y otra vez para construir diferentes estructuras (programas).
- **Flexibilidad:** Si quieres cambiar algo en tu ciudad LEGO, solo necesitas modificar el bloque correspondiente. Lo mismo sucede con la POO, donde los cambios se realizan en las clases.

## POO vs. Programación Tradicional ⚔️
Imagina que la programación tradicional es como escribir una larga lista de instrucciones para construir tu ciudad LEGO. La POO, en cambio, te permite trabajar con planos (clases) y luego crear instancias de esos planos (objetos). Esto hace que tu código sea más fácil de entender y mantener.

### Conceptos Clave de la POO 🔑
- **Clases:** Planos o modelos para crear objetos.
- **Objetos:** Instancias de una clase con características y comportamientos específicos.
- **Atributos:** Características de un objeto (color, tamaño, etc.).
- **Métodos:** Acciones que un objeto puede realizar (moverse, hablar, etc.).

Ejemplo: Una Fábrica de Autos 🚗

```python
#Clase: Auto
class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print("¡Vruuum!")

    def frenar(self):
        print("¡Screeech!")

# Objetos (instancias de la clase Auto)
mi_auto = Auto("Ford", "Mustang", "rojo")
tu_auto = Auto("Toyota", "Corolla", "azul")

mi_auto.acelerar()  # ¡Vruuum!
tu_auto.frenar()    # ¡Screeech!
```

**En este ejemplo, Auto es la clase y mi_auto y tu_auto son objetos de esa clase. Cada objeto tiene sus propios atributos (marca, modelo, color) y puede realizar las mismas acciones (acelerar, frenar).**

# Y se va la segunda 
### La Biblioteca como un Sistema POO
#### Imagina que una biblioteca es un sistema POO:

- **Clases:** Representan los diferentes tipos de elementos en la biblioteca, como libros, revistas y DVDs.
- **Objetos:** Son instancias específicas de cada clase, por ejemplo, el libro "Cien años de soledad" o la revista "National Geographic".
- **Atributos:** Son las características de cada objeto, como el título, autor, género, ISBN, etc.
- **Métodos:** Son las acciones que se pueden realizar con los objetos, como prestar, devolver, reservar, buscar, etc.

#### Ejemplo: La Clase Libro 📖

```python
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
```
- Objetos (Instancias de la Clase Libro)

```python
cien_anios = Libro("Cien años de soledad", "Gabriel García Márquez", "9788420471839", "Novela")
rayuela = Libro("Rayuela", "Julio Cortázar", "9789500397240", "Novela")

cien_anios.prestar()  # El libro 'Cien años de soledad' ha sido prestado.
rayuela.prestar()     # El libro 'Rayuela' ha sido prestado.
cien_anios.devolver() # El libro 'Cien años de soledad' ha sido devuelto.
```

**En este ejemplo, Libro es la clase y cien_anios y rayuela son objetos de esa clase. Cada objeto tiene sus propios atributos (título, autor, ISBN, género, disponibilidad) y puede realizar las mismas acciones (prestar, devolver).**

## Relaciones en POO: ¡Conectando los Puntos! 🤝
Al igual que las personas interactúan entre sí, las clases en POO también establecen relaciones. Estas relaciones definen cómo los objetos se conectan y trabajan juntos.

1. Agregación: El Todo y sus Partes 🧩
Imagina un rompecabezas. Cada pieza (objeto) es parte de un todo (otro objeto). En POO, la agregación es cuando un objeto está formado por otros objetos.

### 1. Ejemplo:

Un automóvil (objeto) está compuesto por motor, ruedas, asientos, etc. (otros objetos).
Una computadora (objeto) está formada por monitor, teclado, mouse, etc. (otros objetos).
### 2. Asociación: ¡Trabajando Juntos! 🤝
La asociación es como una amistad entre objetos. Se conocen y pueden interactuar, pero no dependen uno del otro para existir.

### 2. Ejemplo:

Un estudiante (objeto) está asociado a un profesor (objeto) en una clase.
Un cliente (objeto) está asociado a un banco (objeto) a través de una cuenta bancaria.
### 3. Generalización (Herencia): ¡Familias de Objetos! 👨‍👩‍👧‍👦
La herencia es como una familia. Los hijos (clases hijas) heredan características (atributos) y comportamientos (métodos) de sus padres (clases padres).

### 3. Ejemplo:

- Un perro (clase hija) hereda características de la clase "Mamífero" (clase padre).
- Un automóvil deportivo (clase hija) hereda características de la clase "Automóvil" (clase padre).
### Herencia Simple vs. Herencia Múltiple 👪👨‍👩‍👧‍👦
- Herencia simple: Un hijo tiene un solo padre.
- Herencia múltiple: Un hijo tiene varios padres y hereda características de todos ellos. (Este concepto se verá más adelante)
### Diagrama de Relaciones: El Mapa de las Conexiones 🗺️
Los diagramas de clases UML (Unified Modeling Language) son como mapas que muestran las relaciones entre las clases. Utilizan diferentes símbolos para representar cada tipo de relación:

- **Agregación:** Un rombo vacío en el lado del objeto que contiene a los otros.
- **Asociación:** Una línea simple que conecta los objetos.
Herencia: Una flecha vacía que apunta de la clase hija a la clase padre.

### Material Extra: https://creately.com/blog/es/diagramas/relaciones-de-diagrama-de-clases-uml-explicadas-con-ejemplos/

## Cardinalidad en POO: ¡Contando Relaciones! 🧮
Imagina una escuela. En ella, hay diferentes tipos de relaciones entre alumnos, profesores y clases. La cardinalidad nos ayuda a describir cuántos objetos de cada tipo participan en una relación.

### Tipos de Cardinalidad 🔢
- #### Uno a Uno (1:1): Cada objeto de una clase se relaciona con un solo objeto de otra clase.
1. ***Ejemplo:*** Cada alumno tiene un número de identificación único.
- #### Uno a Muchos (1:N): Un objeto de una clase se relaciona con varios objetos de otra clase.
2. ***Ejemplo:*** Un profesor imparte varias clases.
- #### **Muchos a Uno (N:1):** Varios objetos de una clase se relacionan con un solo objeto de otra clase.
3. ***Ejemplo:*** Varios alumnos pertenecen a una misma clase.
- #### **Muchos a Muchos (N:N):** Varios objetos de una clase se relacionan con varios objetos de otra clase.
4. ***Ejemplo:*** Un alumno puede estar inscrito en varias clases, y cada clase puede tener varios alumnos.

### Ejemplo: Escuela 🏫
| Clase       | Atributos                      | Métodos          | Relaciones                                                                                              |
| :---------- | :------------------------------ | :--------------- | :------------------------------------------------------------------------------------------------------- |
| Alumno      | `nombre`, `edad`, `grado`             | `estudiar()`, `jugar()`  | N:1 con Clase, N:N con Profesor                                                                        |
| Profesor    | `nombre`, `materia`                 | `enseñar()`, `evaluar()` | 1:N con Clase, N:N con Alumno                                                                        |
| Clase       | `nombre`, `horario`                 | `iniciar()`, `terminar()` | 1:N con Alumno, N:1 con Profesor                                                                        |





SELf: https://ejemplos.net/que-significa-self-en-python/

VER EJEMPLO DE CODER: https://colab.research.google.com/drive/1izCL-BjzA6tvkXqtDtd-cv-RrOOG5qiU#scrollTo=Ko1Y5r-p4hW1