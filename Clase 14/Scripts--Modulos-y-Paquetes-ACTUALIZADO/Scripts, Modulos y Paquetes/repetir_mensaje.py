import sys

if len(sys.argv) == 3:  # Verificamos que se hayan pasado 2 argumentos (además del nombre del script)
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])  # Convertimos el segundo argumento a entero

    for _ in range(repeticiones):
        print(texto)
else:
    print("Error: Debes proporcionar dos argumentos: texto y número de repeticiones.")

