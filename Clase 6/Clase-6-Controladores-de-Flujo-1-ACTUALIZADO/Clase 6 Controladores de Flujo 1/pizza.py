# Menú de pizzas y precios
pizzas_menu = [
    ('Marplatense', 800.0),
    ('Pepperoni', 900.0),
    ('Tropical', 1000.0),
    ('Vegetariana', 900.5)
]

# Ingredientes adicionales y precios
ingredientes_adicionales = {
    'Queso extra': 200,
    'Champiñones': 300,
    'Pimiento': 500,
    'Cebolla': 100,
    'Aceitunas': 50,
}

# Mostrar menú
print("Menú de Pizzas:")
print(f"1. {pizzas_menu[0][0]} - ${pizzas_menu[0][1]}")
print(f"2. {pizzas_menu[1][0]} - ${pizzas_menu[1][1]}")
print(f"3. {pizzas_menu[2][0]} - ${pizzas_menu[2][1]}")
print(f"4. {pizzas_menu[3][0]} - ${pizzas_menu[3][1]}")

print("\nIngredientes adicionales:")
print(f"{list(ingredientes_adicionales.keys())[0]} - ${ingredientes_adicionales['Queso extra']}")
print(f"{list(ingredientes_adicionales.keys())[1]} - ${ingredientes_adicionales['Champiñones']}")
print(f"{list(ingredientes_adicionales.keys())[2]} - ${ingredientes_adicionales['Pimiento']}")
print(f"{list(ingredientes_adicionales.keys())[3]} - ${ingredientes_adicionales['Cebolla']}")
print(f"{list(ingredientes_adicionales.keys())[4]} - ${ingredientes_adicionales['Aceitunas']}")

# Selección de pizza
pizza_seleccionada = int(input("\nSelecciona el número de la pizza que deseas: "))

# Validación de selección de pizza
if pizza_seleccionada == 1:
    precio_pizza = pizzas_menu[0][1]
    pizza_nombre = pizzas_menu[0][0]
elif pizza_seleccionada == 2:
    precio_pizza = pizzas_menu[1][1]
    pizza_nombre = pizzas_menu[1][0]
elif pizza_seleccionada == 3:
    precio_pizza = pizzas_menu[2][1]
    pizza_nombre = pizzas_menu[2][0]
elif pizza_seleccionada == 4:
    precio_pizza = pizzas_menu[3][1]
    pizza_nombre = pizzas_menu[3][0]
else:
    print("Selección inválida. Por favor, selecciona una pizza válida.")
    precio_pizza = 0
    pizza_nombre = ""

# Selección de ingredientes adicionales
ingredientes_seleccionados = set()
ingrediente = input("Ingresa un ingrediente adicional (o 'no' para terminar): ").title()
if ingrediente in ingredientes_adicionales:
    ingredientes_seleccionados.add(ingrediente)
ingrediente = input("Ingresa un ingrediente adicional (o 'no' para terminar): ").title()
if ingrediente in ingredientes_adicionales:
    ingredientes_seleccionados.add(ingrediente)
ingrediente = input("Ingresa un ingrediente adicional (o 'no' para terminar): ").title()
if ingrediente in ingredientes_adicionales:
    ingredientes_seleccionados.add(ingrediente)
ingrediente = input("Ingresa un ingrediente adicional (o 'no' para terminar): ").title()
if ingrediente in ingredientes_adicionales:
    ingredientes_seleccionados.add(ingrediente)
ingrediente = input("Ingresa un ingrediente adicional (o 'no' para terminar): ").title()
if ingrediente in ingredientes_adicionales:
    ingredientes_seleccionados.add(ingrediente)

# Calcular el precio total
precio_total = precio_pizza
if 'Queso extra' in ingredientes_seleccionados:
    precio_total += ingredientes_adicionales['Queso extra']
if 'Champiñones' in ingredientes_seleccionados:
    precio_total += ingredientes_adicionales['Champiñones']
if 'Pimiento' in ingredientes_seleccionados:
    precio_total += ingredientes_adicionales['Pimiento']
if 'Cebolla' in ingredientes_seleccionados:
    precio_total += ingredientes_adicionales['Cebolla']
if 'Olivas' in ingredientes_seleccionados:
    precio_total += ingredientes_adicionales['Aceitunas']

# Mostrar el resumen de la compra
print("\nResumen de la compra:")
print(f"Pizza seleccionada: {pizza_nombre}")
if ingredientes_seleccionados:
    print(f"Ingredientes adicionales: {', '.join(ingredientes_seleccionados)}")
else:
    print("No se seleccionaron ingredientes adicionales.")
print(f"Precio total: ${precio_total:.2f}")  #redondeo el resultado precio_total a 2 decimales
