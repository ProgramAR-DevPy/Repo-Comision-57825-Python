# Herencia en POO: ¡La Familia de las Clases! 👨‍👩‍👧‍👦
### ¿Qué es la Herencia? 🧬
- Imagina una familia. Los hijos heredan características (ojos, cabello, etc.) y comportamientos (hablar, caminar, etc.) de sus padres. En POO, la herencia es similar: permite crear nuevas clases (clases hijas) que heredan atributos y métodos de clases existentes (clases padres).

### ¿Por qué Usar Herencia? ♻️
- Reutilización de código: Evita repetir código al crear clases similares.
Jerarquía de clases: Organiza tus clases en una estructura lógica y fácil de entender.
- Extensibilidad: Permite agregar nuevas funcionalidades a las clases hijas sin modificar las clases padres.

### Cómo Funciona la Herencia en Python 🐍

En Python, la herencia se implementa pasando la clase padre como argumento al definir la clase hija:

```python
class Animal:  # Clase padre
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hablar(self):
        print("¡Sonido de animal!")

class Perro(Animal):  # Clase hija
    def hablar(self):
        print("¡Guau!")

class Gato(Animal):  # Clase hija
    def hablar(self):
        print("¡Miau!")

```
### En este ejemplo:

- Animal es la clase padre.
- Perro y Gato son clases hijas que heredan de Animal.
- Ambas clases hijas tienen su propio método hablar(), que sobreescribe el método de la clase padre.
- Principio DRY: ¡No te Repitas! ❌
- La herencia es una excelente manera de aplicar el principio DRY (Don't Repeat Yourself). Al crear una clase base (Animal) con atributos y métodos comunes, evitamos duplicar código en las clases hijas (Perro y Gato).

### Ejemplo de Uso

```python
mi_perro = Perro("Fido", "Canino")
mi_gato = Gato("Whiskers", "Felino")

mi_perro.hablar()  # Output: ¡Guau!
mi_gato.hablar()   # Output: ¡Miau!
```

### Más Allá de la Herencia Simple: Herencia Múltiple 👪

Python también permite la herencia múltiple, donde una clase hija puede heredar de varias clases padres. Esto puede ser útil en situaciones complejas, pero también puede generar problemas si no se utiliza con cuidado.

### **¡Importante! La herencia es una herramienta poderosa, pero debe utilizarse con precaución. Una jerarquía de clases mal diseñada puede llevar a un código confuso y difícil de mantener.**

# Herencia de Clases: Conceptos Clave

1. Clase Padre (Superclase o Clase Base): Es la clase general que contiene atributos y métodos comunes a un conjunto de objetos. En el ejemplo, Animal es la clase padre.
- Clase Hija (Subclase o Clase Derivada): Es la clase que hereda características (atributos y métodos) de la clase padre, pero también puede tener sus propios atributos y métodos específicos. En el ejemplo, Perro, Abeja, etc., son clases hijas.
- Herencia: Es el mecanismo que permite a una clase hija adquirir las características de su clase padre. Esto promueve la reutilización de código y una estructura jerárquica más organizada.
- Sobreescritura (Override): Es la capacidad de redefinir un método heredado de la clase padre en la clase hija, adaptándolo al comportamiento específico de esa clase.
- Polimorfismo: Es la habilidad de un objeto de tomar diferentes formas, es decir, un mismo método (por ejemplo, hablar) puede tener diferentes implementaciones en distintas clases hijas.

### Ejemplo en Python:

```python
class Animal:  # Clase padre
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Sonido genérico de animal")

    def moverse(self):
        print("Moverse de forma genérica")

    def describirme(self):
        print(f"Soy un animal llamado {self.nombre}")


class Perro(Animal):  # Clase hija
    def hablar(self):
        print("Guau!")

    def moverse(self):
        print("Correr en cuatro patas")


class Abeja(Animal):  # Otra clase hija
    def hablar(self):
        print("Bzzzz!")

    def moverse(self):
        print("Volar")

    def picar(self):
        print("¡Pique!")


perro = Perro("Firulais")
perro.describirme()  # Heredado directamente
perro.hablar()       # Sobreescrito
perro.moverse()      # Sobreescrito

abeja = Abeja("Maya")
abeja.describirme()  # Heredado directamente
abeja.hablar()       # Sobreescrito
abeja.moverse()      # Sobreescrito
abeja.picar()        # Nuevo método
```

# Herencia en Inteligencia Artificial

La herencia de clases es un concepto fundamental en IA, especialmente en áreas como:

- Aprendizaje Automático: Se utiliza para crear modelos jerárquicos de clasificación, donde las clases hijas representan categorías más específicas.
- Robótica: Se aplica para modelar robots con diferentes capacidades y comportamientos, heredando de una clase base común.
- Procesamiento del Lenguaje Natural (PLN): Se usa para representar entidades lingüísticas (palabras, frases, etc.) con relaciones jerárquicas.

### Ejemplo en IA:

Imagina un sistema de reconocimiento de animales. Podrías tener una clase base Animal y luego clases hijas como Mamífero, Ave, Reptil, etc. Cada clase hija heredaría atributos comunes de Animal (como nombre, edad) y tendría sus propios atributos específicos (como tipo_pelaje para Mamífero o envergadura_alas para Ave).


# super()

### ¿Qué hace super()?

- La función super() te permite acceder y llamar a métodos de la clase padre (superclase) desde la clase hija (subclase). Esto es especialmente útil cuando:

- Sobreescribes un método: Si redefines un método de la clase padre en la clase hija, super() te permite llamar a la implementación original del método en la clase padre, además de agregar tu propio código específico en la clase hija.
- Accedes a atributos de la clase padre: Puedes utilizar super() para acceder a atributos definidos en la clase padre, incluso si la clase hija tiene atributos con el mismo nombre.
- Inicialización de clases: En el constructor (__init__) de la clase hija, puedes usar super() para llamar al constructor de la clase padre, asegurándote de que los atributos heredados se inicialicen correctamente.

### Ejemplo con Animal y Perro:

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)  # Llama al constructor de Animal
        self.dueño = dueño
```

#### En este caso, super().__init__(especie, edad) dentro del constructor de Perro llama al constructor de Animal, pasando los argumentos especie y edad. Esto asegura que esos atributos se inicialicen correctamente en el objeto Perro, antes de asignar el atributo dueño.

### Ventajas de usar super():

- Código más limpio y legible: Evita la repetición de código al no tener que escribir manualmente la inicialización de atributos heredados.
- Mantenimiento más sencillo: Si la clase padre cambia, solo necesitas modificar la clase padre, y las clases hijas que usan super() se actualizarán automáticamente.
- Flexibilidad: Te permite combinar fácilmente el comportamiento heredado con el comportamiento específico de la clase hija.

### ¿Cuándo usar super()?

Es recomendable usar super() siempre que quieras:

- Extender el comportamiento de un método heredado: Llamar al método original de la clase padre y luego agregar tu propio código.
- Inicializar atributos heredados: Asegurarte de que los atributos de la clase padre se inicialicen correctamente en la clase hija.
- Trabajar con herencia múltiple: super() maneja correctamente la resolución de métodos en casos de herencia múltiple.

# Herencia Múltiple en Python: ¡Combina Superpoderes! 🦸‍♂️🦸‍♀️
- Imagina que un superhéroe 🦸 puede heredar los poderes de varios personajes, como la fuerza de Hulk 💪, la velocidad de Flash ⚡ y la inteligencia de Iron Man 🧠. ¡Eso es herencia múltiple en programación!

- En Python, una clase puede heredar atributos y métodos de varias clases padres (superclases). Esto te permite combinar características de diferentes clases para crear una nueva clase más poderosa y versátil.

### Ejemplo 1: Herencia de dos clases

```python
class Clase1:
    def metodo1(self):
        print("Método 1 de Clase1")

class Clase2:
    def metodo2(self):
        print("Método 2 de Clase2")

class Clase3(Clase1, Clase2):  # Clase3 hereda de Clase1 y Clase2
    pass

objeto = Clase3()
objeto.metodo1()  # Output: Método 1 de Clase1
objeto.metodo2()  # Output: Método 2 de Clase2
```

### Ejemplo 2: Herencia en cadena

```python
class Animal:
    def hablar(self):
        print("¡Sonido de animal!")

class Mamifero(Animal):
    def caminar(self):
        print("¡Caminando!")

class Perro(Mamifero):
    def hablar(self):
        print("¡Guau!")

perro = Perro()
perro.hablar()   # Output: ¡Guau!
perro.caminar()  # Output: ¡Caminando!
```

## Method Resolution Order (MRO): ¡El Orden de los Poderes! 🗺️
Cuando una clase hereda de varias clases, ¿cómo sabe Python qué método usar si hay varios con el mismo nombre? ¡Ahí es donde entra el MRO!

El MRO es el orden en que Python busca los métodos en las clases padre. Puedes verlo usando la función mro():

```python
print(Perro.mro())  
# Output: [<class '__main__.Perro'>, <class '__main__.Mamifero'>, <class '__main__.Animal'>, <class 'object'>]
```

- El MRO en este caso es: Perro, Mamifero, Animal, object. Python buscará primero en Perro, luego en Mamifero, luego en Animal y finalmente en la clase base object.

### ¡Cuidado con los Conflictos! 💥
Si dos clases padre tienen un método con el mismo nombre, Python usará el método de la primera clase que encuentre en el MRO. ¡Asegúrate de que no haya conflictos entre tus superclases!

__HINT: VER EJEMPLO DE FILMINA PARA EL MRO__

# Polimorfismo en Python: ¡Objetos Camaleónicos! 🦎
- Imagina que tienes un control remoto universal 📺. Puedes usarlo para controlar diferentes dispositivos (televisor, reproductor de DVD, equipo de música) sin tener que cambiar de control. ¡Eso es polimorfismo en programación!

- En Python, el polimorfismo significa que objetos de diferentes clases pueden responder al mismo mensaje (método) de manera diferente. Es como si los objetos fueran camaleones que cambian de color según el entorno. 🦎🌈

### ¿Para qué sirve el polimorfismo? 🤔

- Flexibilidad: Permite escribir código más genérico que puede trabajar con diferentes tipos de objetos sin tener que preocuparse por sus detalles específicos.
- Reutilización de código: Evita la necesidad de escribir código duplicado para cada tipo de objeto.
- Extensibilidad: Facilita agregar nuevas clases al sistema sin tener que modificar el código existente.

### ¿Cómo se usa el polimorfismo? 🛠️
En Python, el polimorfismo se logra principalmente a través de la herencia y la sobreescritura de métodos.

- Herencia: Una clase hija hereda los métodos de su clase padre.
Sobreescritura de métodos: La clase hija puede redefinir (sobreescribir) los métodos heredados para que se comporten de manera diferente.
Ejemplo: ¡Animales que Hablan! 🗣️

```python
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
```

Salida:
```
¡Guau!
¡Miau!
¡Sonido de animal!
```

### Explicación:

- Todas las clases (Animal, Perro, Gato) tienen un método hablar().
Cada clase implementa el método hablar() de manera diferente.
Cuando llamamos a animal.hablar(), Python sabe qué versión del método ejecutar según el tipo de objeto al que se refiere animal.
### ¡Sorpresa! ¡Ya usabas polimorfismo! 🤯
Si has estado usando la herencia y sobreescribiste métodos, ¡ya has estado usando polimorfismo sin saberlo! Es una característica fundamental de la programación orientada a objetos que te permite escribir código más flexible, reutilizable y fácil de mantener. 🎉


HINT: POLI= MUCHAS - MORFO= FORMA (POLIMORFISMO: MUCHAS FORMAS)

# Duck Typing en Python: ¡Si Camina como Pato y Habla como Pato, es un Pato! 🦆

El polimorfismo en Python es un concepto fascinante, y entenderlo a fondo requiere conocer el Duck Typing. ¿Qué es esto? Es una filosofía de programación que dice:

- "Si camina como un pato y habla como un pato, entonces debe ser un pato."

### ¿Qué tiene que ver esto con la programación? 🤔
- Imagina que los "patos" son objetos y "caminar/hablar" son métodos. En Python, si un objeto tiene los métodos que necesitas, ¡no importa a qué clase pertenezca!

### Ejemplo: ¡Animales que Hablan! 🗣️
```python
class Pato:
    def hablar(self):
        print("¡Cua Cua!")

class Perro:
    def hablar(self):
        print("¡Guau!")

class Gato:
    def hablar(self):
        print("¡Miau!")

def hacer_hablar(animal):
    animal.hablar()

pato = Pato()
perro = Perro()
gato = Gato()

hacer_hablar(pato)   # Output: ¡Cua Cua!
hacer_hablar(perro)  # Output: ¡Guau!
hacer_hablar(gato)   # Output: ¡Miau!
```

### ¿Cómo funciona? ⚙️
- La función hacer_hablar espera un objeto que tenga un método llamado hablar().
- No importa si el objeto es un Pato, un Perro o un Gato, siempre y cuando tenga ese método.
- Python simplemente llama al método hablar() del objeto que recibe, sin importar su tipo específico.

### Ventajas del Duck Typing:
- Flexibilidad: Puedes usar objetos de diferentes clases en el mismo código sin necesidad de definir interfaces o jerarquías de clases complejas.
- Simplicidad: El código es más conciso y fácil de leer, ya que no hay necesidad de verificar explícitamente los tipos de objetos.

### Duck Typing vs. Polimorfismo:
- Duck Typing: Se basa en la estructura del objeto (qué métodos tiene).
- Polimorfismo: Se basa en la herencia (qué clase es el objeto).
En Python, el Duck Typing es una forma de lograr polimorfismo sin necesidad de herencia explícita.

### ¡Duck Typing en todas partes! 🦆
-El Duck Typing está presente en muchas partes de Python:

- La función len() funciona con cualquier objeto que tenga un método __len__.
- El operador + funciona tanto para sumar números como para concatenar cadenas de texto.

### ¡Python es Flexible! 🧘‍♀️
Gracias al Duck Typing, Python es un lenguaje muy flexible y expresivo. ¡No te limites por los tipos de datos! Si un objeto "camina como un pato y habla como un pato", ¡úsalo como un pato!

# SE VA LA SEGUNDA DEL PATO
- Imagina que estás en un parque y ves un animal que camina como un pato y hace "cuac" como un pato.  
- ¿Qué pensarías? ¡Probablemente que es un pato! 
- No necesitas saber si es un pato de Pekín, un pato criollo o cualquier otra raza específica. Lo importante es que se comporta como un pato.

- En Python, el Duck Typing funciona de manera similar. No le importa de qué "raza" (clase) es un objeto, sino qué puede hacer (qué métodos tiene).

### Por ejemplo, imagina que tienes una función llamada hacer_sonido:

```python
def hacer_sonido(animal):
    animal.hacer_ruido()
```

- Esta función espera recibir un objeto animal que tenga un método llamado hacer_ruido(). No le importa si el objeto es un perro, un gato, un pato o incluso un robot que imita sonidos de animales. Lo único que le importa es que el objeto tenga el método hacer_ruido().

### Si pasas un objeto perro a la función:

```python
class Perro:
    def hacer_ruido(self):
        print("¡Guau!")

mi_perro = Perro()
hacer_sonido(mi_perro)  # Output: ¡Guau!
```

La función llamará al método hacer_ruido() del perro y escucharás un ladrido.

### Si pasas un objeto pato:

```python
class Pato:
    def hacer_ruido(self):
        print("¡Cuak!")

mi_pato = Pato()
hacer_sonido(mi_pato)  # Output: ¡Cuak!
```

La función llamará al método hacer_ruido() del pato y escucharás un graznido.

RESUMIENDO

- Duck Typing: Se enfoca en el comportamiento de los objetos, no en su tipo.
- Si un objeto tiene los métodos necesarios, Python lo usará sin importar su clase.
- Esto hace que el código sea más flexible y fácil de usar, ya que no tienes que preocuparte por crear jerarquías de clases complejas.

# Herencia y Encapsulamiento: ¡Protegiendo los Secretos de tus Clases! 🤫
- Imagina que tienes una receta secreta para hacer una deliciosa salsa 🍝. No quieres compartir todos los detalles con cualquiera, pero sí quieres que tus amigos puedan usar la receta para hacer su propia versión de la salsa. ¡La herencia y el encapsulamiento en Python te permiten hacer algo similar!

### Herencia: ¡Comparte la Receta, pero no Todos los Secretos! 📝
- La herencia permite que una clase (la clase hija) herede atributos y métodos de otra clase (la clase padre). Es como compartir la receta básica de la salsa, pero puedes mantener algunos ingredientes o técnicas en secreto.

### Encapsulamiento: ¡Guarda los Secretos Bajo Llave! 🔒
- El encapsulamiento consiste en proteger los datos y métodos de una clase para que no puedan ser accedidos o modificados directamente desde fuera de la clase. Es como guardar los ingredientes secretos de tu salsa en una caja fuerte.

En Python, puedes lograr el encapsulamiento utilizando:

- Métodos privados: Métodos que comienzan con dos guiones bajos (__). Solo pueden ser accedidos desde dentro de la clase.
- Atributos privados: Atributos (variables) que comienzan con dos guiones bajos (__). También solo son accesibles desde dentro de la clase.

### Ejemplo: ¡Animales que Hablan (o No)! 🗣️🤐

```python
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
```

MAS EN DETALLE

- La clase Animal tiene un método privado __hablar().
- La clase Perro hereda de Animal, pero no puede acceder al método privado __hablar().
- Al intentar llamar a perro1.__hablar(), obtenemos un error porque el método no es accesible desde fuera de la clase Animal.

RESUMIENDO 📝
- Herencia: Permite que una clase herede de otra, compartiendo atributos y métodos (excepto los privados).
- Encapsulamiento: Protege los datos y métodos de una clase para que solo puedan ser accedidos desde dentro de la clase.
- Métodos y atributos privados: Comienzan con dos guiones bajos (__) y solo son accesibles desde dentro de la clase.