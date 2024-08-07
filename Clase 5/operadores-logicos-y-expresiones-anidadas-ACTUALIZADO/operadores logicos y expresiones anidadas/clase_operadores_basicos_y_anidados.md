# Operadores

## ¿Qué son?

En Python, los operadores son símbolos especiales que realizan operaciones sobre uno o más valores, llamados operandos. Podemos pensar en ellos como los signos matemáticos que usas para calcular (+, -, *, /).

# Tipos de Operadores:

### Aritméticos

Se usan para realizar operaciones matemáticas básicas.

- **Suma (+)**
- **Resta (-)**
- **Multiplicación (*)**
- **División (/)**
- **División Entera (//)**
- **Módulo (%)** - Obtiene el resto de una división.
- **Potencia (**)**


```python
resultado = 5 + 3  # Suma
resultado = 10 - 4  # Resta
resultado = 6 * 7   # Multiplicación
resultado = 20 / 5  # División (resultado: 4.0)
resultado = 20 // 5 # División entera (resultado: 4)
resultado = 20 % 3  # Módulo (resultado: 2)
resultado = 2 ** 3  # Potencia (resultado: 8)
```
#### Programa de ejemplo: Cálculo de precio total con impuestos y descuento
```python
# Precio base de un artículo
precio_base = 100.0

# Porcentaje de impuestos
impuestos = 15.0  # 15%

# Porcentaje de descuento
descuento = 10.0  # 10%

# Calcular el precio con impuestos
precio_con_impuestos = precio_base + (precio_base * impuestos / 100)

# Calcular el descuento
monto_descuento = precio_con_impuestos * (descuento / 100)

# Calcular el precio final
precio_final = precio_con_impuestos - monto_descuento

# Mostrar resultados
print("Precio base: $", precio_base)
print("Impuestos (15%): $", precio_base * impuestos / 100)
print("Precio con impuestos: $", precio_con_impuestos)
print("Descuento (10%): $", monto_descuento)
print("Precio final: $", precio_final)
```

**Procedencia de Operadores Numéricos**

1. **Términos entre paréntesis:** `( )`
2. **Potenciación y raíces:** `^`, `√`
3. **Multiplicación y división:** `*`, `/`
4. **Suma y resta:** `+`, `-`

### Jerarquias de operadores logicos
1. not: Negación lógica.
2. and: Conjunción lógica (y).
3. or: Disyunción lógica (o).

## Tipos de Operadores:

### Lógicos Combinan expresiones booleanas
Son útiles para crear condiciones complejas, como verificar si un usuario cumple múltiples requisitos para un préstamo o si un sistema está funcionando correctamente al monitorear diferentes sensores.

Y un dato de color es que los operadores booleanos, tienen un valor por defecto. True = 1 y False = 0


```python
es_valido = (edad >= 18) and (tiene_permiso == True)  
es_posible = (opcion_a == True) or (opcion_b == True)
no_es_menor = not (edad < 18) 
```



### Tabla de la verdad

| P     | Q     | P AND Q | P OR Q | NOT P |
|-------|-------|---------|--------|-------|
| true  | true  | true    | true   | false |
| true  | false | false   | true   | false |
| false | true  | false   | true   | true  |
| false | false | false   | false  | true  |

Columna P y Q:

Acá tenemos dos columnas, P y Q, que representan valores booleanos (verdadero o falso).
Cada fila de la tabla muestra una combinación específica de estos valores para P y Q.
Operador AND (Y):

El operador AND (Y) devuelve verdadero (true) solo cuando ambos operandos son verdaderos (true).
Ejemplos:
- true AND true es true porque ambos P y Q son verdaderos.
- true AND false es false porque uno de los operandos (Q) es falso.
- false AND true es false porque uno de los operandos (P) es falso.
- false AND false es false porque ambos P y Q son falsos.
- Operador OR (O):

El operador OR (O) devuelve verdadero (true) si al menos uno de los operandos es verdadero (true).
Ejemplos:
- true OR true es true porque al menos uno de los operandos (P y Q) es verdadero.
- true OR false es true porque al menos uno de los operandos (P) es verdadero.
- false OR true es true porque al menos uno de los operandos (Q) es verdadero.
- false OR false es false porque ambos P y Q son falsos.

Operador NOT (Negación):

El operador NOT (Negación) invierte el valor booleano de un único operando.
Ejemplos:
- NOT true es false porque negar verdadero (true) resulta en falso (false).
- NOT false es true porque negar falso (false) resulta en verdadero (true).

### Operadores Relacionales

Se utilizan para comparar valores y obtener un resultado booleano (True o False).Son esenciales para tomar decisiones en un programa. Por ejemplo, verificar si un usuario tiene la edad suficiente para acceder a cierto contenido o si un producto está en stock.

- **Igual (==)**
- **Distinto (!=)**
- **Mayor que (>)**
- **Menor que (<)**
- **Mayor o igual que (>=)**
- **Menor o igual que (<=)**

```python
es_mayor = 10 > 5     # True
son_iguales = 5 == 5  # True
es_distinto = 5 != 3  # True
```
#### Programa de ejemplo: Verificación de edad y disponibilidad de producto

```python
# Edad del usuario
edad_usuario = not 20

# Edad mínima requerida
edad_minima = not 18

# Verificar si el usuario tiene la edad suficiente
puede_acceder = edad_usuario >= edad_minima

# Inventario de productos
productos_en_stock = 15

# Cantidad solicitada por el cliente
cantidad_solicitada = 10

# Verificar si hay suficiente stock
hay_suficiente_stock = productos_en_stock >= cantidad_solicitada

# Mostrar resultados
print("¿El usuario tiene la edad suficiente?", puede_acceder)
print("¿Hay suficiente stock del producto?", hay_suficiente_stock)
```
## Expresiones

Una expresión es una combinación de operadores y operandos que se evalúa para producir un valor. En Python, las expresiones pueden ser simples o complejas. Son la base de cualquier cálculo o lógica en un programa. Se utilizan para calcular resultados, tomar decisiones y controlar el flujo de un programa.

```python
expresion_simple = 5 + 3 * 2  # Resultado: 11
expresion_compleja = (10 > 5) and (not (3 == 4))  # Resultado: True
```


## Expresiones Anidadas
Son expresiones que contienen otras expresiones dentro de ellas. Python sigue un orden de precedencia para evaluar estas expresiones, similar a las reglas matemáticas.

```python
resultado = 2 + 3 * (4 - 1)  # Resultado: 11

```
### Programa de Uso real de Ejemplo

```python
# Datos de entrada
peso = 70.0  # Peso en kilogramos
altura = 1.75  # Altura en metros

# Cálculo del IMC
imc = peso / (altura ** 2)

# Clasificación del IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 24.9:
    clasificacion = "Peso normal"
elif 25 <= imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Mostrar resultados
print("Peso: ", peso, "kg")
print("Altura: ", altura, "m")
print("IMC: ", round(imc, 2))
print("Clasificación: ", clasificacion)
```





## Operadores de asignación

| Operador | Descripción                  | Ejemplo        |
|----------|------------------------------|----------------|
| =        | Asignación simple            | a = 10        |
| +=       | Suma y asignación            | a += 5  // equivale a (a = a + 5   )|
| -=       | Resta y asignación           | b -= 3  // equivale a (b = b - 3   )|
| *=       | Multiplicación y asignación  | c *= 2  // equivale a (c = c * 2   )|
| /=       | División y asignación        | d /= 4  // equivale a (d = d / 4   )|
| %=       | Módulo y asignación          | e %= 7  // equivale a (e = e % 7   )|
| **=      | Exponente y asignación       | f **= 3 // equivale a (f = f ** 3  )|
| //=      | División entera y asignación | g //= 5 // equivale a (g = g // 5  )|

### tabla

- **Operador:** Es el operador de asignación.
- **Descripción:** Breve descripción de lo que hace el operador.
- **Ejemplo:** Ejemplo de cómo se utiliza el operador en código.
- **Estos operadores permiten asignar valores a variables de manera eficiente y realizar operaciones aritméticas simultáneamente con la variable.**