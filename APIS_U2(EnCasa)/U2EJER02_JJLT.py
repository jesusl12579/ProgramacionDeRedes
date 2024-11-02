#Autor: Jose de Jesus Lucio Tovar 
#Fecha: 1 de noviembre del 2024
#Descripcion: El script consulta una api de chistes el chiste lo mustra aleatorio como no lo da la api

import requests
import json

def chuck_norris():
#Realiza una solicitud a la api de Chuck Norris y muestra un chiste aleatorio 
    try:
        # Se manda llamar la api de Chuck Norris para obtener el chiste 
        response = requests.get('https://api.chucknorris.io/jokes/random')
        
        # Verifica si la respuesta es exitosa
        if response.status_code == 200:
            data = response.json()
            
            # Extrae el chiste de la respuesta 
            joke = data.get('value', 'Chiste no disponible')
            print("Chiste de Chuck Norris:", joke)
        else:
            print(f"Error: No se pudo obtener el chiste. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error de conexion al intentar obtener el chiste:", e)
    except json.JSONDecodeError:
        print("Error al consultar la api.")
        
#con este ciclo preguta si quiere consultar otro chiste
while True:
    chuck_norris()
    
    # Pregunta si el usuario desea otro chiste
    otro= input("¿Quieres otro chiste? (s/n): ").strip().lower()
    if otro != 's':
        print("Adiosssss")
        break