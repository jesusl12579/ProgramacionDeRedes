
#Actividades de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 26-septiembre-2024
# Leer el ingreso anual del usuario

year = int(input("Introduce un año: "))

# Verificar si el año es anterior a 1582 (inicio del calendario Gregoriano)
if year < 1582:
    print("No dentro del período del calendario Gregoriano")
else:
    # Determinar si el año es bisiesto o común
    if year % 4 != 0:
        print("Año Común")
    elif year % 100 != 0:
        print("Año Bisiesto")
    elif year % 400 != 0:
        print("Año Común")
    else:
        print("Año Bisiesto")
