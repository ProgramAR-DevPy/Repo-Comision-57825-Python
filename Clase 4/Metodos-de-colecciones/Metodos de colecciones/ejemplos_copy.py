
#!COPIAR UN CONJUNTO DE CADENAS
colores = {"rojo", "verde", "azul"}
colores_copia = colores.copy()
colores_copia.remove("verde")  # Elimina un elemento de la copia
print(colores)  # Output: {'rojo', 'verde', 'azul'}
print(colores_copia)  # Output: {'rojo', 'azul'}

#!COPIAR UN CONJUNTO VACIO
conjunto_vacio = set()
copia_vacia = conjunto_vacio.copy()
print(copia_vacia)  # Output: set() (un conjunto vacío)


#!COPIAR UN CONJUNTO DENTRO DE UNA FUNCION
def modificar_conjunto(conjunto):
    copia = conjunto.copy()  # Crea una copia dentro de la función
    copia.add("nuevo elemento")
    return copia

numeros = {1, 2, 3}
numeros_modificados = modificar_conjunto(numeros)
print(numeros)  # Output: {1, 2, 3} (el conjunto original no cambia)
print(numeros_modificados)  # Output: {1, 2, 3, 'nuevo elemento'}

#!COPIAR UN CONJUNTO COMO PARTE DE UNA ESTRUCTURA MAS COMPLEJA
datos = {
    "nombres": {"Ana", "Juan"},
    "edades": {25, 30, 35}
}
datos_copia = datos.copy()
datos_copia["nombres"].add("María")  # Modifica la copia del conjunto "nombres"
print(datos)  # Output: {'nombres': {'Ana', 'Juan'}, 'edades': {25, 30, 35}}
print(datos_copia)  # Output: {'nombres': {'Ana', 'Juan', 'María'}, 'edades': {25, 30, 35}}


#!PROGRAMA DE USO REAL
#!GENERADOR DE NUMEROS DE LOTERIA
import random

def generar_numeros_loteria(cantidad, maximo):
    """Genera una cantidad de números aleatorios únicos entre 1 y maximo."""
    numeros = set()  # Conjunto para almacenar los números generados (sin repetición)

    while len(numeros) < cantidad:
        numeros.add(random.randint(1, maximo))

    return numeros.copy()  # Devuelve una copia del conjunto para evitar modificaciones accidentales

# Generar y mostrar 6 números de lotería del 1 al 49
numeros_loteria = generar_numeros_loteria(6, 49)
print("Números de lotería:", sorted(numeros_loteria))  # Ordenar los números antes de mostrarlos

