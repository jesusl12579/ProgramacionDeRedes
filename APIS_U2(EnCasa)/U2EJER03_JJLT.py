# Autor: Jose de Jesus Lucio Tovar
# Fecha: 1 de noviembre del 2024
# Descripción: El script consulta la api de Star Wars  y consulta planetas
# Permite al usuario ingresar el ID del planeta y muestra su nombre, clima, diametro y poblacion

import requests
import json

try:
    while True:
        try:
            # Ingreso del ID del planeta 
            planeta_id = input("Ingrese el ID del planeta o 0 para salir: ")

            # Verifica la entrada
            if not planeta_id.isdigit():
                print("Ingrese un numero valido.")
                continue
            
            planeta_id = int(planeta_id)

            # Salie del ciclo si selecciono el numero 0
            if planeta_id == 0:
                print("Saliendooooo...")
                break

            # Consulta a la api de Star Wars con el ID del planeta
            url = f'https://www.swapi.tech/api/planets/{planeta_id}'
            respuesta = requests.get(url)
            
            # Verificar errores de conexion 
            respuesta.raise_for_status()  

            datos = respuesta.json()

# Verifica que los datos de resultado existan
            if 'result' in datos and 'properties' in datos['result']:
                propiedades = datos['result']['properties']
                nombre = propiedades.get('name', 'No disponible')
                clima = propiedades.get('climate', 'No disponible')
                diametro = propiedades.get('diameter', 'No disponible')
                poblacion = propiedades.get('population', 'No disponible')
#Muestra los resultados consultados
                print(f'Nombre del planeta: {nombre}')
                print(f'CLima: {clima}')
                print(f'Diametro del planeta: {diametro}')
                print(f'Poblacion del planeta: {poblacion}')
            else:
                print(f"No se encontro informacion del planeta con ID {planeta_id}")

        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la api para el planeta {planeta_id}: {e}")
        except json.JSONDecodeError:
            print(f"Error alconsultar el planeta con ID {planeta_id}")

except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
