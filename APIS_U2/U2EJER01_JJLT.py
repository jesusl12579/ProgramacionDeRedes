#Autor: Jose de Jesus Lucio Tovar 
#Fecha: 1 de noviembre del 2024
import requests
import json

try:
    while True:
        try:
            # Aqui el usuario ingresa el ID
            personaje_id = input("Ingrese el ID del personaje o 0 para salir: ")

            # Verifica la entrada
            if not personaje_id.isdigit():
                print("Ingrese un número válido.")
                continue
            
            personaje_id = int(personaje_id)

            # Salir si se presiono 0
            if personaje_id == 0:
                print("Saliendooooooooo...")
                break

            # Consulta a la API con el ID 
            url = f'https://rickandmortyapi.com/api/character/{personaje_id}'
            respuesta = requests.get(url)
            # Verificar errores en la conexión
            respuesta.raise_for_status()  

            datos = respuesta.json()

            # retorna los valores que le pedi
            if all(key in datos for key in ['name', 'status', 'species', 'gender']):
                name = datos['name']
                status = datos['status']
                species = datos['species']
                gender = datos['gender']
                print(f'El personaje tiene como nombre: {name}, estatus: {status} , especie: {species}, y género: {gender}')
            else:
                print(f"No se encontró informacion del personaje con ID {personaje_id}")

        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API para el personaje {personaje_id}: {e}")
        except json.JSONDecodeError:
            print(f"Error al decodificar la respuesta  para el personaje con ID {personaje_id}")

except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
