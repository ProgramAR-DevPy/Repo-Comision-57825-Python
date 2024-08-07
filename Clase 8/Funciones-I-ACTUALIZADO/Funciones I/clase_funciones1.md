<h1 style="color:blue; text-align:center; font-size:50px">FUNCIONES</h1>


## Funciones: ¡Tus Ayudantes Personales en la Programación! 🤖

Imagina que estás construyendo una casa 🏠. En lugar de hacer cada tarea individualmente (cortar madera, clavar clavos, pintar paredes), contratas a expertos en cada área. ¡Eso es lo que hacen las funciones en programación!

En Python, las funciones son bloques de código reutilizables que realizan una tarea específica. Son como tus ayudantes personales que puedes llamar cuando los necesitas, ¡ahorrándote tiempo y esfuerzo! 🦸‍♀️🦸‍♂️

### ¿Por qué usar funciones? 🤔

* **Organización:** Dividen tu código en partes más pequeñas y manejables, facilitando su lectura y mantenimiento.
* **Reutilización:** Evitan la repetición de código, haciéndolo más eficiente y evitando errores.
* **Abstracción:** Te permiten enfocarte en la tarea principal sin preocuparte por los detalles de implementación.

### ¿Pero como es eso de reutilizar una función?


- Puedes ver el código de ejemplo aquí: [reutilizar.py](./reutilizar.py)


## Anatomía de una función:

1. `def:` Palabra clave que indica que estamos definiendo una función.
`nombre_de_la_funcion:` Nombre único que identifica a la función.
`parametros (opcional):` Valores que la función puede recibir para trabajar con ellos.
2. `Documentación (opcional):` Descripción de lo que hace la función y cómo usarla.
3. `Código de la función:` Las instrucciones que la función ejecutará.
4. `return :` Palabra clave que indica el valor que la función devolverá al finalizar.

```python
def nombre_de_la_funcion(parametros):
    """Documentación de la función (opcional)"""  #Opcional quiere decir que la función va a funcionar aunque no tengamos documentado la misma. Pero cada función que uno haga, tiene que ser documentada. Por lo que por convención, es una MUY BUENA práctica documentar una función y lo hacemos por medio de los docstring (Triples comillas)

    # Código de la función
    return resultado  #Devuelve el resultado de todo lo que pase dentro de la función.
```

<p style="color:red; font-size:50px;">🥊🔴Atención a esto 🔴🥊</p>

<h1 style="color:blue; font-size: 40px">Parámetros vs. Argumentos: ¡El Dúo Dinámico de las Funciones! 🤝</h1>

### 

Imagina que estás enviando una carta 📬. Para enviarla, necesitas la dirección del destinatario y el contenido de la carta. En este caso, la dirección y el contenido son como los **parámetros** de una función en Python. Cuando realmente escribes la dirección y el contenido en la carta, esos son los **argumentos**.

En términos de programación:

- **Parámetros:** Son las variables que se definen en la declaración de la función. Actúan como marcadores de posición para los valores que la función espera recibir.
- **Argumentos:** Son los valores reales que se pasan a la función cuando se llama. Estos valores se asignan a los parámetros correspondientes dentro de la función.

**Ejemplo:**

```python
def enviar_carta(direccion, contenido):  # "direccion" y "contenido" son parámetros
    print(f"Enviando carta a: {direccion}")
    print(f"Contenido de la carta: {contenido}")

enviar_carta("123 Calle Falsa", "Hola, ¿cómo estás?")  # "123 Calle Falsa" y "Hola, ¿cómo estás?" son argumentos
```



## Return vs. Print: ¡El Duelo de las Salidas de Función! 🥊

Imagina que estás en una fábrica 🏭. `return` es como el camión de reparto que lleva el producto terminado a otro lugar para ser usado. `print`, por otro lado, es como la bocina del camión que anuncia que el producto está listo, pero no lo entrega a nadie.

En Python, tanto `return` como `print` se utilizan para producir salidas de una función, pero tienen propósitos muy diferentes:

### Return: ¡El Mensajero Discreto! 🤫

* **Devuelve un valor:** La palabra clave `return` termina la ejecución de la función y envía un valor de vuelta al lugar donde se llamó la función.
* **Asignación a variables:** El valor retornado puede ser asignado a una variable para ser usado más adelante en el programa.
* **Cálculos:** `return` es esencial para funciones que realizan cálculos o procesan datos y necesitan proporcionar un resultado.

**Ejemplo:**

```python
def sumar(a, b):
    resultado = a + b
    return resultado

suma = sumar(5, 3)
print(suma)  # Output: 8
```
### Print: ¡El Anunciador Público! 📢
- **Muestra en pantalla:**  La función `print()` muestra un mensaje o valor en la consola (o en la salida estándar).
- **Efectos secundarios:** No afecta el flujo del programa ni devuelve ningún valor.
- **Depuración y visualización:** `print()` es útil para mostrar mensajes informativos, resultados intermedios o el estado de las variables durante la ejecución del programa.

Ejemplo:

```python
def saludar(nombre):
    mensaje = f"¡Hola, {nombre}!"
    print(mensaje)

saludar("Alice")  # Output: ¡Hola, Alice!
```


### ¿Cuándo usar cada uno? 🤔
- `return:` Cuando necesitas que la función produzca un valor que pueda ser utilizado por otras partes del programa.
- `print:` Cuando quieres mostrar información en la pantalla para el usuario o para depurar tu código.

<br>

## **_Alejandrino TIP_ 💡**
Puedes usar `print()` dentro de una función para mostrar resultados intermedios, pero recuerda usar `return` para devolver el resultado final al programa principal.

### Hint: Veamos ejemplo en código en las primeras lineas del main.py
## 
<br>

# Variables Locales: ¡El Club Exclusivo de las Funciones! 🚪

Imagina que estás en una fiesta privada 🎉. Solo las personas invitadas pueden entrar y disfrutar de lo que hay dentro. Una vez que salen, ya no tienen acceso. ¡Las variables locales en Python funcionan de manera similar!

En programación, una **variable local** es aquella que se define *dentro* de una función. Es como un invitado VIP que solo existe en el contexto de esa función. 

### ¿Por qué usar variables locales? 🤔

* **Encapsulación:** Mantienen el código organizado y evitan conflictos con variables que puedan tener el mismo nombre en otras partes del programa.
* **Protección de datos:** Impiden que el código externo modifique accidentalmente los valores de las variables internas de la función.
* **Liberación de memoria:** Una vez que la función termina de ejecutarse, las variables locales se eliminan automáticamente, liberando memoria.

### Ejemplo en código:

```python
def mi_funcion():
    x = 10  # Variable local "x"
    print(x)  # Output: 10

mi_funcion()
print(x)  # ¡Error! La variable "x" no existe fuera de la función
```

## Funciones y el Mundo Exterior: ¡Comunicación y Retorno de Valores! 🗣️📤
Imagina que una función es como una caja mágica 📦. Puedes poner cosas dentro (argumentos) y la caja hace algo con ellas. Pero, ¿cómo sabes qué pasó dentro de la caja? ¡Con la sentencia return!

En Python, return es la forma en que una función se comunica con el mundo exterior. Es como una puerta que se abre para entregar un mensaje o un regalo al programa principal. 🎁

### Retorno de Valores: ¡El Regalo de la Función! 🎁
return termina la ejecución de la función y envía un valor de vuelta al lugar donde se llamó.
Este valor puede ser de cualquier tipo: números, cadenas de texto, listas, diccionarios, ¡incluso otras funciones!
Puedes usar el valor retornado para realizar cálculos, imprimirlo en pantalla o almacenarlo en una variable para usarlo más tarde.
¡Cuidado! ¡La Función Termina al Retornar! 🛑
Una vez que una función ejecuta un return, se detiene inmediatamente. Cualquier código que esté después del return no se ejecutará.

```python
def mi_funcion():
    print("¡Hola!")
    return 5
    print("¡Adiós!")  # Este print nunca se ejecutará

resultado = mi_funcion()
print(resultado)  # Output: 5
```

### ¡No Abuses del print! 🙅‍♀️
- Es tentador usar print dentro de una función para ver qué está pasando, pero cada vez que llamas a print, estás ejecutando la función nuevamente. Es mejor usar return para obtener el resultado y luego imprimirlo fuera de la función.

