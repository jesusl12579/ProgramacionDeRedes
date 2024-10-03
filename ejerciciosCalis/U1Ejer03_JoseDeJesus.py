# Nombre completo: Jose de Jesus Lucio Tovar
# Fecha de creación: 3 de octubre 
# Tema: Fundamentos de Python

#Crea una lista llamada numeros_control e inicialízala con cinco números de control de tus compañeros
numeros_control = [1223100400, 1223100401, 1223100403, 1223100404, 1223100405]

# Escribe la instrucción que imprima todo el contenido de la lista
print("Números de control:", numeros_control)


grupo = {}  # Colección vacía con el nombre del grupo

for numero in numeros_control:
# Solicita los nombres de los estudiantes de acuerdo al número de control
    nombre = input(f"Ingresa el nombre del No. Control {numero}: ")
    
# Mediante la función input solicite el nombre
#Una vez capturado el nombre, agrega el dato a la colección asociándolo con el número de control
    grupo[numero] = nombre

#Imprime el contenido de la colección
print("\nContenido del grupo:")
for numero, nombre in grupo.items():
    print(f"Número de control: {numero}, Nombre: {nombre}")

#Escribe un ciclo infinito que busque en la colección un número de control existente
while True:
#Solicita el número de control con la función input
    numero_buscado = int(input("\nIngresa el número de control para buscar: "))
    
#Condicional SI-ENTONCES-SINO para verificar si existe el número de control en la colección
    if numero_buscado in grupo:
# En caso afirmativo, despliega el nombre correspondiente y rompe el ciclo con break
        print(f"Nombre asociado al No. Control {numero_buscado}: {grupo[numero_buscado]}")
        break  # Rompe el ciclo infinito
    else:

        print("El número de control no fue encontrado. Inténtalo otra vez.")
