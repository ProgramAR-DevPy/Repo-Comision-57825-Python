# Parámetros y Argumentos en Funciones de Python

### Definición:

- Parámetros: Son las variables que se definen en la declaración de una función. Actúan como marcadores de posición para los valores que se espera que la función reciba cuando sea llamada.

- Argumentos: Son los valores reales que se pasan a una función cuando se la invoca. Estos valores se asignan a los parámetros correspondientes dentro de la función.

- **Imagina que una función es como una receta de cocina. Los parámetros son los ingredientes listados en la receta (harina, huevos, azúcar), mientras que los argumentos son las cantidades específicas que utilizas al preparar la receta (2 tazas de harina, 3 huevos, 1 taza de azúcar).**

Función con dos parámetros
```python
def saludar(nombre, mensaje):  # nombre y mensaje son parámetros
    """Imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}! {mensaje}")

saludar("Ana", "Bienvenido/a")  # "Ana" y "Bienvenido/a" son argumentos
```
### Argumentos por Posición

- En Python, cuando llamamos a una función y le pasamos argumentos, estos se asignan a los parámetros de la función según su orden o posición. Esto significa que el primer argumento se asigna al primer parámetro, el segundo argumento al segundo parámetro, y así sucesivamente.

#### Ejemplo 1: Suma

```python
def suma(numero1, numero2):
    """Suma dos números y devuelve el resultado."""
    return numero1 + numero2

resultado = suma(7, 5)  # 7 es numero1, 5 es numero2
print(resultado)  # Output: 12
```

#### En este caso:

El argumento 7 se asigna al parámetro numero1.
El argumento 5 se asigna al parámetro numero2.

#### Ejemplo 2: Resta
```python
def resta(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b

resultado = resta(15, 12)  # 15 es a, 12 es b
print(resultado)  # Output: 3
```
#### En este caso:

El argumento 15 se asigna al parámetro a.
El argumento 12 se asigna al parámetro b.

#### Importancia del orden:

- El orden de los argumentos es crucial. Si cambiamos el orden, el resultado de la función puede ser diferente:

```python
resultado = resta(12, 15)  # 12 es a, 15 es b
print(resultado)  # Output: -3 
```
## Buenas prácticas:

- Nombres descriptivos: Utiliza nombres de parámetros que indiquen claramente su propósito.
- Documentación: Documenta tus funciones explicando qué hacen y qué tipo de argumentos esperan.
- Orden lógico: Organiza los parámetros de manera lógica, siguiendo el orden en que se usarán dentro de la función.
- Valores por defecto (opcional): Considera usar valores por defecto para los parámetros que puedan tener valores comunes.

## Argumentos por Nombre (Keyword Arguments)

- Además de pasar argumentos por posición, Python permite utilizar argumentos por nombre (keyword arguments). Esto significa que podemos especificar explícitamente a qué parámetro corresponde cada argumento al momento de llamar a la función, utilizando la sintaxis nombre_parametro=valor.

#### Ventajas:

- Mayor claridad: El código se vuelve más legible, ya que se indica claramente qué valor se asigna a cada parámetro.
- Flexibilidad: No es necesario respetar el orden de los parámetros en la definición de la función, lo que permite cambiar el orden de los argumentos al llamarla.
- Valores por defecto: Se pueden omitir argumentos que tienen valores por defecto en la definición de la función.

#### Ejemplo 1: Resta con argumentos por nombre

```python
def resta(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b

resultado = resta(b=15, a=12)  # Asignamos 15 a b y 12 a a
print(resultado)  # Output: -3
```

##### En este ejemplo, indicamos explícitamente que el valor 15 corresponde al parámetro b y el valor 12 al parámetro a, sin importar el orden en que los escribimos.

#### Ejemplo 2: Resta con tres parámetros

```python
def resta(a, b, c):
    """Resta tres números y devuelve el resultado."""
    return a - b - c

resultado = resta(a=15, b=12, c=2) 
print(resultado)  # Output: 1

resultado = resta(c=2, a=15, b=12)  # Cambiamos el orden de los argumentos
print(resultado)  # Output: 1 (el resultado es el mismo)
```

##### En este caso, al usar argumentos por nombre, podemos cambiar el orden en que los pasamos sin afectar el resultado de la función.



#### Buenas prácticas:

- Usar con moderación: Los argumentos por nombre son útiles en funciones con muchos parámetros o cuando el orden no es intuitivo. En funciones simples, los argumentos por posición suelen ser suficientes.
- Consistencia: Si decides usar argumentos por nombre, úsalos para todos los argumentos de la función para mantener la coherencia.
- Documentación: Documenta tus funciones indicando claramente si esperan argumentos por posición, por nombre o ambos.

## Llamada a Funciones sin Argumentos y Parámetros por Defecto en Python
#### Llamada sin Argumentos
En Python, si una función está definida para recibir argumentos, es necesario proporcionarle esos argumentos al llamarla. Si no lo hacemos, obtendremos un error TypeError indicando que faltan argumentos.

Ejemplo:

```python
def resta(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b

resultado = resta()  # Error: TypeError: resta() missing 2 required positional arguments: 'a' and 'b'
```
#### Este error ocurre porque la función resta espera recibir dos argumentos (a y b), pero no le hemos proporcionado ninguno.

#### Parámetros por Defecto
Para evitar este error y hacer que nuestras funciones sean más flexibles, podemos asignar valores por defecto a los parámetros. Esto significa que si no se proporciona un argumento para un parámetro al llamar a la función, se utilizará el valor por defecto especificado en la definición de la función.

#### Ejemplo:

```python
def resta(a=10, b=5):  # a y b tienen valores por defecto
    """Resta dos números y devuelve el resultado."""
    return a - b

resultado = resta()  # No se pasan argumentos, se usan los valores por defecto
print(resultado)  # Output: 5
```
En este caso, como no pasamos ningún argumento al llamar a resta(), la función utiliza los valores por defecto a=10 y b=5, y el resultado es 5.

#### Combinación de Argumentos y Valores por Defecto:

- Podemos combinar argumentos y valores por defecto. Si pasamos un argumento para un parámetro, se usará ese valor en lugar del valor por defecto.

```python
resultado = resta(20)  # Se pasa un argumento para a, b usa el valor por defecto
print(resultado)  # Output: 15 

resultado = resta(b=8)  # Se pasa un argumento por nombre para b, a usa el valor por defecto
print(resultado)  # Output: 2
```
### Buenas prácticas:

- Valores por defecto opcionales: Utiliza valores por defecto solo para parámetros que puedan tener valores comunes o razonables si no se proporciona un argumento.
- Orden de los parámetros: Coloca los parámetros con valores por defecto al final de la lista de parámetros.
- Documentación: Documenta tus funciones indicando claramente qué parámetros tienen valores por defecto y cuáles no.

## Paso de Argumentos por Valor y por Referencia.

En Python, cuando pasamos argumentos a una función, existen dos formas principales en que estos argumentos se manejan:

#### Paso por valor:

- Se crea una copia del valor del argumento dentro de la función.
Cualquier modificación que se haga al argumento dentro de la función no afecta al valor original fuera de la función.
Los tipos de datos simples (números, cadenas, booleanos) se pasan por valor.

#### Paso por referencia:

- Se pasa una referencia (dirección de memoria) al objeto original.
Cualquier modificación que se haga al argumento dentro de la función afecta directamente al objeto original fuera de la función.
Los tipos de datos compuestos (listas, diccionarios, conjuntos, etc.) se pasan por referencia.
Ejemplos:

### Paso por valor (números):

```python
def duplicar(numero):
    """Duplica un número."""
    numero *= 2
    print("Dentro de la función:", numero)

valor = 5
duplicar(valor)  # Se pasa una copia de 'valor'
print("Fuera de la función:", valor)  # El valor original no cambia
```
Salida:

```Dentro de la función: 10
Fuera de la función: 5

```
### Paso por referencia (listas):
```python
def agregar_elemento(lista, elemento):
    """Agrega un elemento a una lista."""
    lista.append(elemento)
    print("Dentro de la función:", lista)

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista, 4)  # Se pasa una referencia a 'mi_lista'
print("Fuera de la función:", mi_lista)  # La lista original se modifica
```
```
Salida:

Dentro de la función: [1, 2, 3, 4]
Fuera de la función: [1, 2, 3, 4]
```
## ¿Por qué es importante?

Entender cómo funciona el paso de argumentos es crucial para evitar sorpresas y errores en tu código. Si modificas un argumento dentro de una función, debes saber si estás cambiando una copia local o el objeto original.

### Buenas prácticas:

- Tipos de datos simples: En general, es seguro modificar argumentos de tipos simples dentro de una función, ya que no afectará al valor original.
- Tipos de datos compuestos: Si necesitas modificar un objeto compuesto dentro de una función y que los cambios se reflejen fuera de ella, debes tener en cuenta que estás trabajando con una referencia al objeto original. Si no quieres modificar el original, crea una copia antes de pasarla a la función.


## ¿Qué son *args y **kwargs en Python?
- *args se utiliza en las funciones para aceptar un número variable de argumentos posicionales.
Cuando usas *args en una función, todos los argumentos adicionales que se pasen a la función se recopilan en una tupla.

Ejemplo:

```python

def suma(*args):
    total = 0
    for num in args:
        total += num
    return total

resultado = suma(1, 3, 4, 2)
print(resultado)  # Output: 10
```

### Explicación con manzanas:
Imagínate que *args es una bolsa que puede contener cualquier cantidad de manzanas. Cuando llamas a la función, todas las manzanas que pongas en la bolsa se suman.



- **kwargs se utiliza en las funciones para aceptar un número variable de argumentos con nombre (keyword arguments).
Cuando usas **kwargs en una función, todos los argumentos con nombre adicionales que se pasen a la función se recopilan en un diccionario.

Ejemplo:

```python

def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Ana", edad=30, ciudad="Madrid")
```

### Explicación con manzanas:
Imagínate que **kwargs es una caja que puede contener manzanas etiquetadas con su tipo. Cuando llamas a la función, todas las manzanas etiquetadas que pongas en la caja se muestran con su etiqueta.

## Recursividad en Python: Funciones que se Llaman a Sí Mismas
- La recursividad es un concepto poderoso en programación que permite a una función llamarse a sí misma durante su ejecución. Esta técnica es especialmente útil para resolver problemas que pueden ser divididos en subproblemas más pequeños de la misma naturaleza.

### ¿Cómo funciona la recursividad?
Una función recursiva se compone de dos partes esenciales:

- Caso base: Es la condición que detiene la recursión. Sin un caso base, la función se llamaría a sí misma infinitamente, creando un bucle sin fin.

- Llamada recursiva: Es la llamada que la función hace a sí misma, pero con un argumento modificado que se acerca al caso base.

## Tipos de funciones recursivas
- Recursivas sin retorno: Estas funciones realizan una acción en cada llamada recursiva, pero no devuelven un valor explícitamente. Suelen utilizarse para tareas como imprimir secuencias o recorrer estructuras de datos.

- Recursivas con retorno: Estas funciones devuelven un valor calculado a partir del resultado de las llamadas recursivas. Son útiles para problemas como el cálculo de factoriales o la búsqueda en estructuras de datos jerárquicas.

## Ventajas:

1. Elegancia y simplicidad: Soluciones recursivas pueden ser más claras y concisas que las iterativas para ciertos problemas.
2. Expresividad: La recursividad refleja la naturaleza recursiva de algunos problemas de forma natural.

## Desventajas:

1. Consumo de memoria: Cada llamada recursiva crea un nuevo marco de pila, lo que puede consumir mucha memoria si la recursión es profunda.
2. Rendimiento: En algunos casos, las soluciones iterativas pueden ser más eficientes que las recursivas.

### Ejemplo recursividad con retorno:
```python
def suma_lista(lista):
    """Calcula la suma de los elementos de una lista de forma recursiva."""
    if not lista:  # Caso base: si la lista está vacía, la suma es 0
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])  # Llamada recursiva con el resto de la lista

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
resultado = suma_lista(mi_lista)
print(resultado)  # Output: 15

```
### Recursividad sin retorno
```python
def cuenta_regresiva(numero):
    """Imprime una cuenta regresiva desde el número dado hasta 0."""
    if numero < 0:  # Caso base: detener la recursión si el número es negativo
        return  # No devuelve ningún valor

    print(numero)    # Imprime el número actual
    cuenta_regresiva(numero - 1)  # Llamada recursiva con el número disminuido en 1

# Ejemplo de uso:
cuenta_regresiva(5)
```