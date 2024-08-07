# Scripts con Argumentos: ¡Dale Superpoderes a tus Programas! 💪
- Imagina que tu programa es un robot 🤖. Hasta ahora, solo ha seguido instrucciones predefinidas. ¡Pero con los argumentos, puedes darle nuevas órdenes y hacerlo más flexible!

### ¿Qué son los Argumentos? 🤔
- Son valores que le pasas a tu script cuando lo ejecutas desde la línea de comandos (cmd o terminal). Estos valores pueden ser números, texto, listas, ¡lo que necesites! Tu script puede usarlos para realizar cálculos, tomar decisiones o personalizar su comportamiento.

### ¡Pásale Argumentos a tu Script! 🏃‍♂️
- Abre tu línea de comandos (cmd en Windows, terminal en macOS o Linux).
Navega hasta la carpeta donde está guardado tu script.
Escribe el siguiente comando:
```Bash
python nombre_de_tu_script.py argumento1 argumento2 ...

```

Reemplaza nombre_de_tu_script.py por el nombre real de tu archivo.
Puedes pasar tantos argumentos como quieras, separados por espacios.

#### Ejemplo: ¡Un Saludo Personalizado! 👋

Archivo saludo.py:

```python
import sys

nombre = sys.argv[1]  # Obtenemos el primer argumento
print(f"¡Hola, {nombre}!")
```

En la línea de comandos:

```Bash
python saludo.py "Alice"
```

### **Salida**:
```
¡Hola, Alice!
```

## ¡Atención! ⚠️
- Todos los argumentos se pasan como cadenas de texto (strings).
- Si necesitas usar números o listas, debes convertirlos dentro de tu script.
- Python almacena los argumentos en una lista especial llamada sys.argv.
- El primer elemento de sys.argv (sys.argv[0]) es el nombre del script mismo.
- Los argumentos que pasas al script comienzan desde sys.argv[1].

### Ejemplo con Múltiples Argumentos: ¡Repite un Mensaje! 🔁
```python
import sys

if len(sys.argv) == 3:  # Verificamos que se hayan pasado 2 argumentos (además del nombre del script)
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])  # Convertimos el segundo argumento a entero

    for _ in range(repeticiones):
        print(texto)
else:
    print("Error: Debes proporcionar dos argumentos: texto y número de repeticiones.")
```

## En la línea de comandos:

```Bash
python repetir_mensaje.py "Hola" 5
```

### *Salida*:
```
Hola
Hola
Hola
Hola
Hola
```


# Módulos en Python: ¡Organiza y Reutiliza tu Código como un Profesional! 📦
- Imagina que estás construyendo un gran castillo de LEGO 🏰. En lugar de tener todas las piezas mezcladas en una caja gigante, las organizas en bolsas más pequeñas según su tipo (bloques, ventanas, puertas). ¡Los módulos en Python son como esas bolsas!

- Un módulo es simplemente un archivo de Python (.py) que contiene definiciones de funciones, clases y variables. Puedes pensar en él como una caja de herramientas 🧰 que guarda tus herramientas de programación (funciones, clases) para que puedas usarlas en diferentes proyectos.

### ¿Por qué usar módulos? 🤔
- Organización: Agrupan el código relacionado en un solo lugar, haciendo que tu proyecto sea más fácil de entender y mantener.
- Reutilización: Puedes usar las funciones y clases definidas en un módulo en otros programas sin tener que reescribir el código.
- Evitar conflictos de nombres: Los módulos crean espacios de nombres separados, lo que evita que los nombres de tus funciones y variables entren en conflicto con los de otros módulos o bibliotecas.

### Creando y Usando Módulos: ¡Paso a Paso! 🪜
1. Crea un archivo Python: Guarda tu código en un archivo con la extensión .py (por ejemplo, funciones_matematicas.py).

2. Define funciones, clases y variables: Escribe tus definiciones dentro del archivo.

```python
# funciones_matematicas.py

def suma(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

def resta(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b
```

3. Importa el módulo: En otro archivo Python, usa la palabra clave import para acceder a las funciones, clases y variables definidas en el módulo.

```ython
# uso_funciones.py

import funciones_matematicas

resultado_suma = funciones_matematicas.suma(5, 3)
print(resultado_suma)  # Output: 8
```

### Atajo de Importación: ¡Directo al Grano! ⚡
Puedes importar elementos específicos de un módulo usando from ... import ...:

```python
# uso_funciones.py

from funciones_matematicas import suma

resultado_suma = suma(5, 3)
print(resultado_suma)  # Output: 8
```

¡Tu Primer Módulo con Clases! 🎓
Archivo alumno.py:

```python
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Alumno: {self.nombre}, Nota: {self.nota}")
```

Archivo main.py:

```python
import alumno

estudiante = alumno.Alumno("Alice", 95)
estudiante.imprimir()  # Output: Alumno: Alice, Nota: 95
```

# Paquetes en Python: ¡Organiza tus Módulos como un Profesional! 🗂️
- Imagina que tienes una colección de libros enorme 📚. En lugar de apilarlos todos en un estante gigante, los organizas en estanterías separadas por géneros (ficción, no ficción, poesía). ¡Los paquetes en Python son como esas estanterías!

- Un paquete es una forma de organizar tus módulos en Python. Es simplemente una carpeta que contiene varios módulos relacionados. Esto te permite agrupar tu código de manera lógica y evitar que tu proyecto se convierta en un caos de archivos .py.

### ¿Por qué usar paquetes? 🤔
- Organización: Agrupan módulos relacionados en un solo lugar, haciendo que tu código sea más fácil de entender y mantener.
- Espacios de nombres: Evitan conflictos de nombres entre módulos y funciones.
- Escalabilidad: Facilitan el crecimiento de tu proyecto a medida que agregas más módulos.

### Creando tu Primer Paquete: ¡Paso a Paso! 🪜
1. Crea una carpeta: Dale un nombre descriptivo a tu paquete (por ejemplo, mi_primer_paquete).
2. Archivo __init__.py: Dentro de la carpeta, crea un archivo vacío llamado __init__.py. Este archivo le indica a Python que la carpeta es un paquete.
3 .Crea módulos: Agrega tus archivos .py (módulos) dentro de la carpeta del paquete.

```mi_primer_paquete/
├── __init__.py
├── modulo1.py
└── modulo2.py
```

### Ejemplo:

```python
# modulo1.py
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

# modulo2.py
def despedirse(nombre):
    print(f"¡Adiós, {nombre}!")
```

**Importa y usa: En otro archivo Python (por ejemplo, main.py), importa los módulos del paquete y utiliza sus funciones.**

```python
# main.py
from mi_primer_paquete import modulo1, modulo2

modulo1.saludar("Alice")  # Output: ¡Hola, Alice!
modulo2.despedirse("Bob") # Output: ¡Adiós, Bob!
```


### ¡Organiza tus Proyectos como un Experto! 🧠
- Los paquetes son una herramienta esencial para mantener tus proyectos de Python organizados y escalables. ¡Utilízalos para agrupar tus módulos, evitar conflictos de nombres y hacer que tu código sea más fácil de entender y reutilizar!

# Paquetes Redistribuibles, Collections, Datetime y Math en Python: ¡Herramientas Esenciales para tus Proyectos! 🛠️

### Paquetes Redistribuibles: ¡Comparte tu Código con el Mundo! 🎁
- Un paquete redistribuible es como una caja de regalo 🎁 que contiene tu código Python (funciones, clases, módulos) listo para ser usado por otros desarrolladores o en otros proyectos.

### ¿Cómo usar un paquete distribuido?

- Obtener el paquete: Alguien te debe haber proporcionado un archivo con la extensión .tar.gz (por ejemplo, mi_paquete-0.1.tar.gz).
- Instalar con pip: Abre tu terminal o línea de comandos y ejecuta:

```Bash
pip3 install nombre_del_paquete.tar.gz
```

¡Ahora puedes importar y usar las funciones y clases del paquete en tu código!

### Collections: ¡Superpoderes para tus Colecciones de Datos! 💪
El módulo collections de Python es como un kit de herramientas 🧰 lleno de utilidades para trabajar con listas, tuplas, diccionarios y otras colecciones de datos.

## Ejemplo: namedtuple (Tuplas con Nombre)
```python
from collections import namedtuple

# Creamos una "clase" para representar peces
Pez = namedtuple("Pez", ["nombre", "especie", "tanque"])

# Creamos un objeto Pez
nemo = Pez("Nemo", "Pez payaso", "Arrecife")

print(nemo.nombre)  # Output: Nemo
print(nemo.especie) # Output: Pez payaso
```

### Ejemplo: Counter (Contar Elementos)

```python
from collections import Counter

texto = "Hola mundo mundo"
conteo_palabras = Counter(texto.split())
print(conteo_palabras)  # Output: Counter({'mundo': 2, 'Hola': 1})
```

### Datetime: ¡Viaja en el Tiempo con Fechas y Horas! ⏱️
- El módulo datetime te permite trabajar con fechas y horas en Python. Puedes obtener la fecha y hora actual, crear objetos datetime personalizados, formatear fechas y realizar cálculos temporales.

#### Ejemplo:

```python
from datetime import datetime, timedelta

ahora = datetime.now()
print(ahora)  # Output: 2024-07-23 11:01:32.789101 (o similar)

# Sumar 5 días a la fecha actual
dentro_de_5_dias = ahora + timedelta(days=5)
print(dentro_de_5_dias)
```

## Math: ¡Calculadora Científica en Python! 🧮
- El módulo math te proporciona funciones matemáticas avanzadas, como seno, coseno, tangente, logaritmos, raíces cuadradas, etc.

### Ejemplo:

```python
import math

print(math.pi)       # Output: 3.141592653589793
print(math.sqrt(16))  # Output: 4.0
print(math.sin(math.pi / 2))  # Output: 1.0
```

MAS DEL MODULO MATH: https://www.w3schools.com/python/module_math.asp

# Random: ¡La Magia del Azar en Python! 🎲✨
- Imagina que tienes una bolsa llena de números 🔢. Cierras los ojos, metes la mano y sacas uno al azar. ¡El módulo random en Python hace algo similar!

- random es un módulo incorporado que te permite generar números aleatorios (o pseudoaleatorios, para ser precisos). Estos números pueden ser enteros, decimales, elementos de una lista, ¡incluso puedes barajar una lista entera!

### ¿Por qué usar random? 🤔
1. Juegos: Para crear elementos impredecibles, como dados, cartas o movimientos de enemigos.
2. Simulaciones: Para modelar eventos aleatorios, como el clima, el comportamiento de partículas o resultados de experimentos.
3. Seguridad: Para generar contraseñas seguras o tokens de autenticación.
4. Muestreo: Para seleccionar elementos aleatorios de una lista o conjunto de datos.

### Funciones Básicas de random:
- random.random(): Devuelve un número decimal aleatorio entre 0 y 1 (sin incluir el 1).
```python
import random

numero_aleatorio = random.random()
print(numero_aleatorio)  # Output: 0.7258170239500886 (o similar)
```

- random.randint(a, b): Devuelve un número entero aleatorio entre a y b (ambos incluidos).

```python
dado = random.randint(1, 6)
print(dado)  # Output: 4 (o cualquier número entre 1 y 6)
```

- random.choice(secuencia): Devuelve un elemento aleatorio de una secuencia (lista, tupla, string).

```python
frutas = ["manzana", "banana", "naranja"]
fruta_aleatoria = random.choice(frutas)
print(fruta_aleatoria)  # Output: naranja (o cualquier otra fruta de la lista)
```

- random.shuffle(lista): Mezcla los elementos de una lista de forma aleatoria.

```python
cartas = ["As", "Rey", "Reina", "Jota", 10, 9, 8, 7, 6, 5, 4, 3, 2]
random.shuffle(cartas)
print(cartas)  # Output: [2, 5, 'As', 9, 3, 'Reina', 7, 4, 10, 'Jota', 6, 8, 'Rey'] (o similar)
```

### ¡Más Funciones y Ejemplos! 🤯
- El módulo random tiene muchas más funciones para generar números aleatorios con diferentes distribuciones, elegir muestras aleatorias, etc. 

**¡Juega con el Azar! 🎲
Con el módulo random, puedes agregar un toque de imprevisibilidad y diversión a tus programas. ¡Úsalo para crear juegos, simulaciones, herramientas de seguridad y mucho más!**

