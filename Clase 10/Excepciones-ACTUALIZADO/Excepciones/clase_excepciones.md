# Errores y Excepciones: ¡Aprende de tus Tropiezos y Conviértete en un Maestro! 🏋️‍♀️
Programar es como aprender a andar en bicicleta 🚲: al principio te caes mucho, pero con cada error aprendes algo nuevo y te vuelves más hábil. ¡Los errores son parte del proceso!

En Python, hay dos tipos principales de errores que te puedes encontrar:

### 1. Errores de Sintaxis: ¡La Gramática de Python! 🔤
Son como errores gramaticales en un texto. Python es muy estricto con su "gramática" y te avisará si escribes algo que no entiende.

Ejemplos comunes:

Olvidar cerrar paréntesis, comillas o usar comillas diferentes:

```python
print("Hola)  # Error falta cerrar una comilla.(SyntaxError: unterminated string literal (detected at line 1))
print('Hola")  # Error: comillas diferentes (SyntaxError: unterminated string literal (detected at line 2))
```

## Indentación incorrecta :

```python
if True:
print("Hola")  # Bloque con sangría previsto (IndentationError: expected an indented block after 'if' statement on line 1)
```

- No poner dos puntos (:) al definir una función:

```python
def mi_funcion()
    print("Hola")  # Se esperaba ":" (SyntaxError: expected ':')
```
### SyntaxError: unexpected EOF while parsing ¡ Error de Final de Archivo! 🕵️‍♀️
Imagina que estás leyendo un libro y de repente, la historia termina abruptamente sin una conclusión. ¡Te quedarías con ganas de saber qué pasó!  Eso es similar a lo que ocurre con el error ```SyntaxError: unexpected EOF while parsing``` en Python.

- **¿Qué significa este error? 🤔
```EOF (End Of File)```:** Significa "Fin de Archivo". Python llegó al final del archivo (o de la línea de código) sin encontrar lo que esperaba.
- ```Unexpected (Inesperado):``` Python encontró un final de archivo donde no debería haberlo.
- ```While Parsing (Mientras Analizaba):``` El error ocurrió mientras Python estaba leyendo y analizando tu código.

En pocas palabras, este error significa que falta algo en tu código. Python esperaba encontrar algo más, pero se topó con el final del archivo antes de encontrarlo.

#### Causas Comunes:
- Olvidar cerrar paréntesis, corchetes o llaves:

```python
print("Hola"  # "(" no estaba cerrado (SyntaxError: '(' was never closed)
lista = [1, 2, 3  # "[" no estaba cerrado (SyntaxError: '[' was never closed)
diccionario = {"clave": "valor"  # "{" no estaba cerrado (SyntaxError: '{' was never closed)
```

- ### Olvidar cerrar comillas en una cadena de texto:

```python
mensaje = "Hola mundo!  # La cadena literal no está terminada (SyntaxError: unterminated string literal (detected at line 1))
```

- ### Errores de indentación (espacios al principio de las líneas):

```python
if True:
print("Hola")    # Bloque con sangría previsto (IndentationError: expected an indented block after 'if' statement on line 1)
```

🚦**TIP DE LÓGICA:**
- **Revisa cuidadosamente tu código**: Busca paréntesis, corchetes, llaves y comillas que no estén cerrados correctamente.
- **Verifica la indentación:** Asegúrate de que los bloques de código (como los que están dentro de if, for, while, etc.) estén correctamente indentados.
- **Usa un editor de código:** Un buen editor de código te ayudará a detectar estos errores resaltando la sintaxis y mostrando advertencias.

Ejemplo:
```Python
pint("Hola")  # "pint" no está definido (NameError: name 'pint' is not defined. Did you mean: 'print'?)
```


## Errores Semánticos: ¡La Lógica Importa! 🤔
Imagina que le pides a un robot que te traiga el tercer libro de un estante vacío 🤖📚. El robot no podrá hacerlo, porque no hay ningún tercer libro. ¡Eso es un error semántico!

En programación, los errores semánticos son errores en la lógica de tu programa. Ocurren cuando le pides a Python que haga algo que no tiene sentido, aunque la sintaxis del código sea correcta.

¡La Experiencia es Clave! 🗝️
La mejor manera de prevenir errores semánticos es escribir mucho código y aprender de tus propios errores. ¡La práctica hace al maestro! 💪

### Ejemplos Comunes de Errores Semánticos:
1. IndexError: ¡Fuera de los Límites! 🚫

```python
lista_vacia = []
elemento = lista_vacia[0]  # Error:  IndexError, la lista está vacía por lo que da fuera de rango (IndexError: list index out of range)
```

🚦**TIP DE LÓGICA:** Verifica si la lista tiene elementos antes de intentar acceder a ellos.

```python
if len(lista_vacia) > 0:
    elemento = lista_vacia[0] 
else:
    print("La lista está vacía.")
```
2. TypeError: ¡Tipos Incompatibles! ❌

```python
edad = input("Ingresa tu edad: ")
edad_doble = edad * 2  # No tira error pero no va a ser el resultado esperado ya que va a repetir 2 veces lo que se ponga en el input
```
🚦**TIP DE LÓGICA:** Convierte el input a un número (entero o flotante) antes de realizar operaciones matemáticas.

```python
edad = int(input("Ingresa tu edad: "))  # Convertimos a entero
```

#### ¡Python te Ayuda a Detectarlos! 🕵️‍♀️
Los errores semánticos no se detectan al escribir el código, sino cuando lo ejecutas. Python te mostrará un mensaje de error que te ayudará a identificar el problema.







# Excepciones: ¡Domina los Imprevistos en tu Código! 🦸‍♀️
Imagina que estás construyendo un castillo de naipes 🃏. Un pequeño error puede hacer que todo se derrumbe. ¡Las excepciones en Python son como una red de seguridad que evita que tu programa se caiga a pedazos cuando algo sale mal!

### ¿Qué son las Excepciones? 🤔
Son errores que ocurren durante la ejecución del programa, incluso si la sintaxis es correcta. Pueden ser causados por situaciones inesperadas, como intentar dividir por cero o usar una variable que no existe.

#### Ejemplos de Excepciones:

```python
10 * (1 / 0)  # ZeroDivisionError: división por cero
4 + spam * 3  # NameError: la variable 'spam' no está definida
```

### ¡Try-Except al Rescate! ⛑️

Para evitar que las excepciones detengan tu programa, puedes usar los bloques try-except:

```python
try:
    # Código que podría causar una excepción
except TipoDeExcepción:
    # Código que se ejecuta si ocurre la excepción
```

- ### Cómo funciona:

Python intenta ejecutar el código dentro del bloque try.
Si todo va bien, el bloque except se ignora.
Si ocurre una excepción del tipo especificado después de except, se ejecuta el código dentro del bloque except.
- Si ocurre una excepción de otro tipo, el programa se detiene y muestra un mensaje de error.

#### Ejemplo: Manejando una División por Cero

HINT: EJEMPLO CODIGO EN VIVO
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error! No puedes dividir por cero.")
```


## ¡Maneja Diferentes Excepciones! 🤹‍♀️

- #### Puedes tener varios bloques except para manejar diferentes tipos de excepciones:
VIVO
```python
try:
    resultado = 10 / int(input("Ingresa un número: "))
except ZeroDivisionError:
    print("¡Error! No puedes dividir por cero.")
except ValueError:
    print("¡Error! Debes ingresar un número válido.")
```



# Excepciones en Python: ¡Controla el Caos y Mantén tu Código a Salvo! 🛡️
### Else: ¡La Celebración del Éxito! 🎉
El bloque else en una estructura try-except es opcional y se ejecuta solo si NO ocurre ninguna excepción dentro del bloque try. Es como una fiesta de celebración por haber superado los obstáculos sin problemas. 🥳

### Ejemplo:

```python
while True:
    try:
        a = float(input("Introduce un número: "))
        b = float(input("Introduce otro número: "))
        print(a + b)
    except ValueError:
        print("¡Error! Debes introducir números válidos.")
    else:
        print("¡La suma se realizó correctamente!")
        break  # Salimos del bucle si todo salió bien
```

### Finally: ¡El Limpiador Responsable! 🧹
El bloque finally (opcional) se ejecuta siempre, haya ocurrido o no una excepción. Es como el equipo de limpieza que se asegura de que todo quede ordenado después de la fiesta, incluso si hubo algún incidente. 😉

Ejemplo:

```python
try:
    archivo = open("mi_archivo.txt", "r")
    # ... código para trabajar con el archivo ...
except FileNotFoundError:
    print("¡Error! El archivo no existe.")
finally:
    archivo.close()  # Cerramos el archivo siempre, incluso si hubo un error
```
Otro ejemplo:

```python
try:
    resultado = 10 / 2  # División por cero (genera una excepción ZeroDivisionError)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Esta línea siempre se imprime, incluso con el error.")
```

### Excepciones Múltiples: ¡Identifica al Culpable! 🕵️‍♂️
Puedes tener varios bloques except para manejar diferentes tipos de excepciones. Cada bloque se ejecutará solo si ocurre la excepción específica que está capturando.

Ejemplo:

```python
try:
    n = float(input("Introduce un número divisor: "))
    5 / n
except TypeError:
    print("¡Error! No puedes dividir un número por una cadena de texto.")
except ValueError:
    print("¡Error! Debes introducir un número válido.")
except ZeroDivisionError:
    print("¡Error! No puedes dividir por cero.")
except Exception as e:  # Captura cualquier otra excepción
    print(f"¡Error inesperado! {type(e).__name__}: {e}")
```

### Explicación:

- Primero, intentamos convertir la entrada del usuario a un número flotante y dividir 5 entre ese número.
Si el usuario ingresa algo que no es un número, se lanza un ValueError y se ejecuta el segundo bloque except.
Si el usuario ingresa "0", se lanza un ZeroDivisionError y se ejecuta el tercer bloque except.
Si ocurre cualquier otro tipo de error, se ejecuta el último bloque except, que captura la excepción general Exception y muestra un mensaje de error más detallado.