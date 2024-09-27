
#Actividades de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 26-septiembre-2024
# Leer el ingreso anual del usuario
income = float(input("Introduce el ingreso anual: "))

# Inicializamos el impuesto en cero
tax = 0

# Cálculo del impuesto dependiendo del ingreso
if income <= 85528:
    tax = (0.18 * income) - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

# Si el impuesto calculado es menor que 0, ajustarlo a 0
if tax < 0:
    tax = 0

# Redondear el impuesto a pesos totales
tax = round(tax, 0)

# Mostrar el resultado
print("El impuesto es:", tax, "pesos")
