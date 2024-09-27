#Actividades de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 26-septiembre-2024
# Leer el ingreso anual del usuario

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

# Iniciar el bucle while para adivinar el número secreto
while True:
    guess = int(input("Introduce tu número: "))
    
    # Comprobar si el número es el secreto
    if guess == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")