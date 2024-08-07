# POO: ¡El Mundo como un Juego de Construcción! 🧱
Imagina que estás construyendo con bloques de LEGO. Cada bloque es un objeto, y cada tipo de bloque es una clase.

- Clases: Los Planos de tus Bloques 📐
Las clases son como los planos de tus bloques de LEGO. Te dicen qué forma tiene cada bloque, qué color es y qué puedes hacer con él. Por ejemplo, una clase "Casa" podría tener:

1. - **Atributos (Características):**
- Número de pisos
- Color de las paredes
- Número de ventanas

2. - **Métodos (Acciones):**
- Abrir la puerta
- Encender las luces
- Construir un techo

3. - **Objetos: Tus Bloques Únicos 🏠🚗:**
Los objetos son los bloques reales que construyes siguiendo los planos (clases). Cada objeto es único y puede tener valores diferentes para sus atributos. Por ejemplo, puedes tener:

 - __Objeto 1:__ Una casa roja de dos pisos con cuatro ventanas.
- __Objeto 2:__ Una casa azul de un piso con dos ventanas.
- __Objeto 3:__ Un auto rojo con cuatro ruedas.
- __Atributos:__ Las Características de tus Bloques 🎨📏
Los atributos son las características que describen tus objetos. Son como los detalles de tus bloques de LEGO: color, tamaño, forma, etc.
- __Métodos:__ Las Acciones de tus Bloques 🏃‍♂️🗣️
Los métodos son las cosas que tus objetos pueden hacer. Son como las acciones que puedes realizar con tus bloques de LEGO: construir, mover, apilar, etc.

### Ejemplo: Clase Perro 🐶
```python
class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        print("¡Guau!")

    def comer(self):
        print("El perro está comiendo.")
```

# POO en Python: ¡Construyendo Clases y Objetos! 🐶
### Creando una Clase Básica
En Python, utilizamos la palabra clave class para definir una clase. Aquí tienes un ejemplo de una clase vacía llamada Perro:

```python
class Perro:
    pass  # Indicamos que la clase está vacía por ahora
```

### Instanciando una Clase (Creando Objetos)
Una vez que tenemos la clase Perro, podemos crear objetos (instancias) de esa clase. Cada objeto representa un perro individual:

```python
mi_perro = Perro()
```

### Atributos: Las Características de los Objetos 🐕
Los atributos son las características que describen a los objetos. En nuestra clase Perro, podemos agregar atributos como nombre, raza y edad:

```python
class Perro:
    def __init__(self, nombre, raza, edad):  # Constructor
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
```

El método __init__ es un método especial llamado constructor. Se ejecuta automáticamente cuando creamos un nuevo objeto Perro y nos permite asignar valores iniciales a los atributos.

### Ejemplo de Uso

```python
mi_perro = Perro("Fido", "Labrador", 5)
print(mi_perro.nombre)  # Output: Fido
print(mi_perro.raza)    # Output: Labrador
print(mi_perro.edad)     # Output: 5
```

### Tipos de Atributos
- **Atributos de Instancia:** Pertenecen a cada objeto individual. En el ejemplo anterior, nombre, raza y edad son atributos de instancia.
- **Atributos de Clase:** Son compartidos por todos los objetos de la clase. Se definen fuera del constructor, directamente dentro de la clase.

```python
class Perro:
    especie = "Canis lupus familiaris"  # Atributo de clase

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
```

#### Ahora, todos los perros creados a partir de esta clase tendrán el mismo valor para el atributo especie.

# El Misterioso self: ¡El Actor Principal de tus Objetos! 🎭
### ¿Qué es self? 👤

- Imagina que cada objeto es un actor en una obra de teatro. self es como el nombre artístico de ese actor. Le permite referirse a sí mismo y acceder a sus propios atributos (características) y métodos (acciones).

En Python, self es el primer parámetro de cualquier método dentro de una clase. No es una palabra clave reservada, pero es una convención muy importante. Cuando llamas a un método en un objeto, Python automáticamente pasa ese objeto como el primer argumento (self).

Ejemplo: El Perro Actor 🐶

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")
```

Cuando creamos un objeto Perro y llamamos al método ladrar(), Python hace lo siguiente:

- 1. Pasa el objeto mi_perro como el argumento self al método ladrar().
- 2. Dentro del método, self.nombre se refiere al atributo nombre del objeto mi_perro.

```python
mi_perro = Perro("Fido")
mi_perro.ladrar()  # Output: Fido dice: ¡Guau!
```

### Definiendo Métodos: Las Acciones de tus Objetos 🎬
Los métodos son las acciones que un objeto puede realizar. Se definen dentro de la clase, utilizando la palabra clave def.

```python
class Perro:
    # ... (atributos y constructor)

    def caminar(self, pasos):
        print(f"{self.nombre} camina {pasos} pasos.")

    def comer(self, comida):
        print(f"{self.nombre} come {comida}.")
```

### Ejemplo de Uso de Métodos

```python
mi_perro.caminar(10)  # Output: Fido camina 10 pasos.
mi_perro.comer("croquetas")  # Output: Fido come croquetas.
```

### Métodos Especiales: Los Guiones Bajos Dobles ✨

- Los métodos que comienzan y terminan con doble guion bajo (__) son métodos especiales en Python. El constructor __init__ es un ejemplo de ello. Otros métodos especiales comunes son:

- __str__: Define cómo se representa el objeto como una cadena de texto.
- __repr__: Define una representación oficial del objeto (útil para depuración).
- __eq__: Define cómo se comparan dos objetos para determinar si son iguales.


# Métodos Especiales en Python: ¡La Magia Detrás de las Clases! ✨
### ¿Qué son los Métodos Especiales? 🪄
Los métodos especiales (también conocidos como métodos mágicos o dunder methods) son funciones especiales en Python que comienzan y terminan con doble guion bajo (__). Estos métodos permiten personalizar el comportamiento de los objetos y hacer que tus clases interactúen con el lenguaje de una manera más natural.

- __init__: El Constructor 🏗️
El método __init__ es el constructor de una clase. Se ejecuta automáticamente cuando creas un nuevo objeto y te permite inicializar sus atributos.

**HINT: Los atributos que estan dentro del constructor init se van a ejecutar cada vez que se inicie la clase. Los creados dentro del metodo, se ejecutan solo cuando lo hace el metodo.**

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

- __str__: La Representación en Texto 📝
El método __str__ te permite definir cómo se representa un objeto como una cadena de texto. Es útil para imprimir información sobre el objeto de manera legible.

```python
class Persona:
    # ... (constructor)

    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"

p = Persona("Ana", 30)
print(p)  # Output: Persona: Ana, 30 años
```

### Otros Métodos Especiales Útiles 🧰
- __repr__: Similar a __str__, pero proporciona una representación más técnica del objeto (útil para depuración).
- __len__: Define la longitud de un objeto (por ejemplo, el número de elementos en una lista).
- __getitem__: Permite acceder a los elementos de un objeto mediante índices (como en las listas).
- __add__, __sub__, etc.: Permiten sobrecargar operadores aritméticos para que funcionen con tus objetos.
### Ejemplo: Clase Vector 🧮
```python
class Vector:
    def __init__(self, datos):
        self._datos = datos

    def __str__(self):
        return f"Vector: {self._datos}"

    def __len__(self):
        return len(self._datos)

    def __getitem__(self, indice):
        return self._datos[indice]
```

En este ejemplo, el método __getitem__ permite acceder a los elementos del vector como si fuera una lista:

```python
v = Vector([1, 2, 3])
print(v[0])  # Output: 1
```


# Métodos Especiales en Python: ¡Personalizando tus Objetos! 🛠️
### __len__: ¿Cuántos Elementos Hay? 📏
- El método __len__ te permite definir la longitud de un objeto. Es decir, cuántos elementos contiene. Python lo utiliza automáticamente cuando llamas a la función len() sobre tu objeto.

```python
class ListaPersonalizada:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

mi_lista = ListaPersonalizada([1, 2, 3])
print(len(mi_lista))  # Output: 3
```

### __getitem__: Accede a tus Elementos con Índices 🔍
- El método __getitem__ te permite acceder a los elementos de un objeto utilizando índices, como si fuera una lista o un diccionario.

```python
class ListaPersonalizada:
    # ... (constructor y __len__)

    def __getitem__(self, indice):
        return self.elementos[indice]

mi_lista = ListaPersonalizada([1, 2, 3])
print(mi_lista[0])  # Output: 1
```

### __setitem__: Modifica tus Elementos ✏️
- El método __setitem__ te permite modificar los elementos de un objeto utilizando índices.

```python
class ListaPersonalizada:
    # ... (constructor, __len__, __getitem__)

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

mi_lista = ListaPersonalizada([1, 2, 3])
mi_lista[1] = 10
print(mi_lista.elementos)  # Output: [1, 10, 3]
```
### __iter__: ¡Haz que tu Objeto sea Iterable! 🔄
- El método __iter__ convierte tu objeto en un iterable, lo que significa que puedes recorrerlo con un bucle for.

```python
class ListaPersonalizada:
    # ... (constructor, __len__, __getitem__, __setitem__)

    def __iter__(self):
        return iter(self.elementos)

mi_lista = ListaPersonalizada([1, 2, 3])
for elemento in mi_lista:
    print(elemento)  # Output: 1, 2, 3
```

### Ejemplo Completo: Clase Vector 🧮

```python
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
```

Este código define una clase Vector que se comporta como una lista, permitiendo acceder y modificar sus elementos, obtener su longitud y recorrerlo con un bucle for.

# Encapsulamiento en Python: ¡Protegiendo tus Datos! 🛡️
### ¿Qué es el Encapsulamiento? 🔒
- Imagina que tienes una caja fuerte con un código secreto. Solo tú puedes abrirla y acceder a su contenido. El encapsulamiento en POO es similar: protege los datos (atributos) y comportamientos (métodos) de un objeto, permitiendo que solo el propio objeto pueda acceder a ellos.

### ¿Por qué Encapsular? 🤔
- Protección de datos: Evita que otros objetos modifiquen accidentalmente los datos de tu objeto, garantizando su integridad.
- Flexibilidad: Puedes cambiar la implementación interna de un objeto sin afectar cómo otros objetos lo utilizan.
- Modularidad: Ayuda a dividir tu código en módulos independientes y bien organizados.
- Encapsulamiento en Python: Convención, no - - 

- Restricción 🐍
Python no tiene un mecanismo estricto de encapsulamiento como otros lenguajes (por ejemplo, private en Java). En cambio, utiliza una convención:

### Atributos y métodos públicos: Se acceden directamente desde fuera del objeto.
- Atributos y métodos "privados": Se nombran con un doble guion bajo (__) al principio. Esto indica que no deberían ser accedidos directamente desde fuera del objeto, aunque técnicamente es posible hacerlo.

### Ejemplo: Clase Cliente 💳


```python
class Cliente:
    def __init__(self, nombre, __numero_cuenta):
        self.nombre = nombre
        self.__numero_cuenta = __numero_cuenta  # Atributo "privado"

    def mostrar_saldo(self):
        # ... lógica para mostrar el saldo de la cuenta ...

    def __actualizar_saldo(self):  # Método "privado"
        # ... lógica para actualizar el saldo de la cuenta ...
```

### En este ejemplo:

- nombre es un atributo público, accesible desde fuera del objeto.
- __numero_cuenta es un atributo "privado", que no debería ser accedido directamente desde fuera.
- mostrar_saldo es un método público, accesible desde fuera del objeto.
- __actualizar_saldo es un método "privado", que solo debería ser llamado desde dentro de la clase Cliente.
#### Accediendo a Atributos "Privados" (No Recomendado) 🤫
Aunque no es una buena práctica, técnicamente puedes acceder a atributos "privados" utilizando el nombre modificado de la clase:

```python
cliente = Cliente("Ana", "12345")
print(cliente._Cliente__numero_cuenta)  # Output: 12345
```

**¡Importante! Evitar acceder directamente a atributos "privados" es fundamental para mantener la integridad de tus objetos y aprovechar los beneficios del encapsulamiento.**





# ententiendo getitem y setitem
#### Imagina que los métodos __getitem__ y __setitem__ son como las manos de un robot:

- __getitem__ (la mano que agarra): Este método permite al robot tomar un objeto específico de un lugar determinado. En el caso de una lista, ese lugar sería un índice. Por ejemplo, mi_lista[2] le dice al robot que agarre el tercer elemento de la lista.
- __setitem__ (la mano que coloca): Este método permite al robot colocar un objeto en un lugar específico. Siguiendo con el ejemplo de la lista, mi_lista[2] = 5 le dice al robot que coloque el número 5 en el tercer lugar de la lista.
Por otro lado, los métodos get y set son como botones en un panel de control:

- get (el botón de lectura): Al presionar este botón, el robot te muestra el valor de un atributo específico. Por ejemplo, mi_objeto.get_nombre() te mostraría el nombre del objeto.
set (el botón de escritura): Al presionar este botón, puedes cambiar el valor de un atributo específico. Por ejemplo, mi_objeto.set_nombre("Nuevo Nombre") cambiaría el nombre del objeto.
Diferencias clave:

- Sintaxis: Los métodos __getitem__ y __setitem__ usan corchetes ([]), mientras que get y set usan paréntesis ().
- Flexibilidad: __getitem__ y __setitem__ son más flexibles porque pueden trabajar con diferentes tipos de datos (listas, diccionarios, etc.). get y set suelen estar diseñados para atributos específicos.
Control: get y set te dan más control porque puedes agregar lógica adicional dentro de ellos (por ejemplo, validar si un valor es correcto antes de asignarlo).

