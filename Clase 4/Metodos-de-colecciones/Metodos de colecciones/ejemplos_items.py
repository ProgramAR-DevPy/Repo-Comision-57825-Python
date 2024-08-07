
#!ITERAR SOBRE ITEMS
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
for clave, valor in colores.items():
    print(f"La clave '{clave}' tiene el valor '{valor}'")
# Output:
# La clave 'amarillo' tiene el valor 'yellow'
# La clave 'azul' tiene el valor 'blue'
# La clave 'verde' tiene el valor 'green'




#!BUSCAR UN VALOR ESPECIFICO POR SU CLAVE
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
for clave, valor in colores.items():
    if valor == "blue":
        print(f"La clave '{clave}' tiene el valor 'blue'")
        break

#!MODIFICAR VALORES EN UN DICCIONARIO
edades = {"Ana": 30, "Juan": 25, "María": 35}
for nombre, edad in edades.items():
    if edad < 30:
        edades[nombre] += 1  # Incrementa la edad en 1 si es menor a 30
print(edades)  # Output: {'Ana': 30, 'Juan': 26, 'María': 35}