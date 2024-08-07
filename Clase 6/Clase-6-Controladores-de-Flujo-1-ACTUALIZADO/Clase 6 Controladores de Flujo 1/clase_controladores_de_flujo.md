<font color="yellow"><h1 > Clase 6: Controladores de Flujo I - Condicionales en Python</h1></font>


### Introducción al Flujo

En programación, el **flujo** se refiere al orden en que se ejecutan las instrucciones de un programa. Python, como lenguaje de programación, ejecuta estas instrucciones de manera secuencial, una tras otra.

Para manipular datos y crear programas más dinámicos, necesitamos herramientas que permitan al programa tomar decisiones y repetir tareas. Aquí es donde entran los **controladores de flujo**.

### Sentencias de Control

Las sentencias de control se dividen en dos categorías:

* **Condicionales:** Permiten que el programa elija entre diferentes caminos de ejecución basados en condiciones.
* **Iterativas:** Permiten que el programa repita un bloque de código varias veces.

En esta clase, nos enfocaremos en las sentencias condicionales.

### Condicionales: If, Elif, Else

Las sentencias condicionales en Python se construyen con las palabras clave `if`, `elif` y `else`.

#### If:

La sentencia `if` evalúa una condición. Si la condición es verdadera (`True`), se ejecuta el bloque de código indentado debajo del `if`.

```python
edad = 25
if edad >= 18:
    print("Eres mayor de edad")
```

#### Else:

La sentencia `else` se utiliza junto con `if`. Si la condición del `if` es falsa (`False`), se ejecuta el bloque de código indentado debajo del `else`.

```python
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
```

#### Else:

La sentencia `else` se utiliza junto con `if`. Si la condición del `if` es falsa (`False`), se ejecuta el bloque de código indentado debajo del `else`.

```python
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
```

#### Elif:
La sentencia elif (abreviatura de "else if") permite evaluar múltiples condiciones en secuencia. Si la condición del `if` es falsa, se evalúa la condición del primer `elif`. Si esta también es falsa, se evalúa la siguiente, y así sucesivamente.

```python
calificacion = 85
if calificacion >= 90:
  print("Sobresaliente")
elif calificacion >= 80:
  print("Notable")
elif calificacion >= 70:
  print("Bien")
else:
  print("Insuficiente")
```
### Operadores Relacionales y Lógicos

Para construir condiciones, utilizamos operadores relacionales y lógicos:

* **Operadores Relacionales:** 
    * `==` (igual)
    * `!=` (diferente)
    * `>` (mayor que)
    * `<` (menor que)
    * `>=` (mayor o igual que)
    * `<=` (menor o igual que)

* **Operadores Lógicos:**
    * `and` (y)
    * `or` (o)
    * `not` (no)

#### Ejemplo:

```python
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
  print("Puedes conducir")
else:
  print("No puedes conducir")
```

### Indentación

En Python, la **indentación** (espacios en blanco al inicio de una línea) es crucial. Define qué líneas de código pertenecen a un bloque condicional.

El siguiente código nos arrojará un error ¿Por que?

```python
a = 25
b = 50
if b > a:
print("b es más grande que a")
```



#### If en una sola línea

Python permite escribir sentencias `if`-`else` simples en una sola línea:

```python
x = 10
resultado = "Par" if x % 2 == 0 else "Impar"
print(resultado)  # Output: Par
```

# Reglas de estructuras de condicionales
#### En Python, las estructuras de control de flujo `if`, `elif`, y `else` tienen reglas específicas sobre su uso, pero no todas las combinaciones son obligatorias. Aquí están las reglas y cómo se pueden usar:

# `if:`
#### Requerido: Siempre se necesita un `if` para iniciar una estructura de control condicional.
#### Opcional: No necesita necesariamente un `else` o `elif`.
#### Ejemplo:

```python
if condición:
    # Bloque de código
```

# `elif:`
#### Opcional: Puede haber cero o más `elif` en una estructura condicional.
#### Requerido: Debe preceder un `if`. No puede existir sin un `if` inicial.
##### Ejemplo:

```python
if condición1:
    # Bloque de código 1
elif condición2:
    # Bloque de código 2
elif condición3:
    # Bloque de código 3
```
# `else:`
#### Opcional: Puede haber cero o un `else` en una estructura condicional.
#### Requerido: Debe preceder un `if` o un `elif`. No puede existir sin un `if` inicial.
#### Finaliza: Debe ser la última cláusula de la estructura condicional.
#### Ejemplo:

```python
if condición1:
    # Bloque de código 1
elif condición2:
    # Bloque de código 2
else:
    # Bloque de código 3
```


# Combinaciones permitidas
Solo `if`: Una estructura de control mínima puede consistir solo en un `if`.

```python
if condición:
    # Bloque de código
```

`if` con `else`: Un `if` puede tener un `else` opcional.

```python
if condición:
    # Bloque de código verdadero
else:
    # Bloque de código falso
```
`if` con uno o más `elif`: Un `if` puede tener uno o más `elif`.

```python

if condición1:
    # Bloque de código 1
elif condición2:
    # Bloque de código 2
elif condición3:
    # Bloque de código 3
```
`if` con `elif` y `else`: Un `if` puede tener uno o más `elif` y un `else` final.

```python
if condición1:
    # Bloque de código 1
elif condición2:
    # Bloque de código 2
else:
    # Bloque de código 3
```



#### Ejemplos prácticos
#### Ejemplo sin `else`:
```python
edad = 20
if edad >= 18:
    print("Es un adulto")
```

#### Ejemplo con `if` y `else`:
```python
edad = 15
if edad >= 18:
    print("Es un adulto")
else:
    print("Es menor de edad")
```
#### Ejemplo con `if` y `elif`:
```python
nota = 85
if nota >= 90:
    print("Sobresaliente")
elif nota >= 80:
    print("Notable")
elif nota >= 70:
    print("Aprobado")
```

#### Ejemplo con `if`, `elif`, y `else`:
```python
nota = 65
if nota >= 90:
    print("Sobresaliente")
elif nota >= 80:
    print("Notable")
elif nota >= 70:
    print("Aprobado")
else:
    print("Suspenso")
```