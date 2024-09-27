#Actividades de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 26-septiembre-2024

# Solicita al usuario un número natural
c0 = int(input("Ingresa un número natural: "))

# Verifica que el número sea positivo
if c0 <= 0:
    print("El número debe ser un entero positivo.")
else:
    pasos = 0  # Inicializa el contador de pasos

    # Bucle que ejecuta la secuencia de Collatz
    while c0 != 1:
        print(c0)  # Muestra el valor actual de c0
        if c0 % 2 == 0:  # Si es par
            c0 = c0 // 2
        else:  # Si es impar
            c0 = 3 * c0 + 1
        pasos += 1  # Incrementa el contador de pasos

    # Muestra el último valor (que será 1)
    print(c0)
    # Muestra el número total de pasos
    print("Cantidad de pasos:", pasos)
