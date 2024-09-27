#Actividades de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 26-septiembre-2024



#Crear una variable vacía para almacenar la palabra sin vocales
word_without_vowels = ""

# Pedir al usuario que ingrese una palabra
user_word = input("Introduce una palabra: ")
user_word = user_word.upper()  # Convertir la palabra a mayúsculas

# Bucle for para recorrer cada letra de la palabra
for letter in user_word:
    if letter in ('A', 'E', 'I', 'O', 'U'):  # Verificar si la letra es una vocal
        continue  # Saltar la iteración si la letra es una vocal
    word_without_vowels += letter  # Concatenar las letras no vocales a la variable

# Imprimir la palabra sin vocales
print(word_without_vowels)