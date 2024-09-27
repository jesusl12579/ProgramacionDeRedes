#Actividades de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 26-septiembre-2024

# Leer la cantidad de bloques disponibles
blocks = int(input("Ingresa el número de bloques: "))

# Inicializar la altura de la pirámide y el número de bloques en la capa actual
height = 0
blocks_in_current_layer = 1

# Bucle while para construir la pirámide
while blocks >= blocks_in_current_layer:
    blocks -= blocks_in_current_layer  # Restar los bloques de la capa actual
    height += 1  # Aumentar la altura
    blocks_in_current_layer += 1  # La siguiente capa necesita un bloque más

# Imprimir la altura de la pirámide
print("La altura de la pirámide:", height)