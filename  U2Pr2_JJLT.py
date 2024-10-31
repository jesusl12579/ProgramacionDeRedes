#
#Nombre: Jose de Jesus Lucio Tovar
#Fecha: 31 de otctubre 
#TERMINADO 

import requests 

def linea():
    for _ in range(20):
        print("=", end="")
    print()

def buscar_libro(titulo):
    url = "https://openlibrary.org/search.json"
    params = {'title': titulo}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Error al procesar la solicitud")
        return

    datos = response.json()
    if datos['num_found'] > 0:
        print(f"Se encontraron {datos['num_found']} documentos.")
        for libro in datos['docs']: 
            titulo_libro = libro.get('title', 'No disponible')
            autores = ', '.join(libro.get('author_name', ['No disponible']))
            ano_publicacion = libro.get('first_publish_year', 'No disponible')
            
            linea()
            print(f"Título: {titulo_libro}")
            print(f"Autor(es): {autores}")
            print(f"Año de publicación: {ano_publicacion}")
            linea()
    else:
        print("No se encontraron documentos que coincidan con el título del libro.")

def main():
    titulo = ""
    while not titulo.strip():
        titulo = input("Ingrese el titulo del libro que deseas buscar: ")

    buscar_libro(titulo)

if __name__ == "__main__":
    main()
