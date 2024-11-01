import requests
import time  # Importar el módulo time

latitud = 20.64
longitud = 101.02
clave = "1809eecfd96c7d3d21734b41528edf21"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

'''
200        OK
401        Usuario no Autorizado
'''

while True:
    latitud = input("Ingresa la latitud: ")
    if latitud.lower() == 'salir' or latitud.lower() == 's':
        break
    longitud = input("Ingresa la longitud: ")
    if longitud.lower() == 'salir' or longitud.lower() == 's':
        break
    
    main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
    json_data = requests.get(main_api).json()
    codigo = json_data['cod']

    if codigo == 200:
        print(f"El código {codigo} indica que la respuesta es correcta")
        print('--------------------------------------------------------')
        print(f"Latitud:                    {json_data['coord']['lat']}")
        print('--------------------------------------------------------')
        print(f"longitud:                  {json_data['coord']['lat']}")
        print('--------------------------------------------------------')
        print(f"velocidad:                {json_data['wind']['speed']}")
        print('--------------------------------------------------------')
        print(f"temperatura:             {json_data['main']['temp']}")
        print('--------------------------------------------------------')
        print(f"humedad:                  {json_data['main']['humidity']}")
        print('--------------------------------------------------------')
        print(f"Clima:                    {json_data['weather'][0]['main']}")

    else:
        print(f"El código {codigo} indica que algo anda mal")
    time.sleep(3)

print('Adiós, hasta luego')
