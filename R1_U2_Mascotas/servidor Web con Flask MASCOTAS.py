from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario para almacenar las mascotas
listaMascotas = {}

# Elementos del diccionario 
listaMascotas['Firulais'] = {
    "nombre": "Firulais",
    "edad": "12 meses",
    "raza": "Chihuahua",
    "alergias": "   Ninguna",
    "genero": "Macho",
    "observaciones": "Ninguna"
}
listaMascotas['Solovino'] = {
    "nombre": "Solovino",
    "edad": "2 años",
    "raza": "No se conoce",
    "alergias": "Ninguna",
    "genero": "Macho",
    "observaciones": "Travieso"
}

# Metodo GET para listar todas las mascotas
@app.route('/mascotas', methods=['GET'])
def obtener_mascotas():
    return jsonify(listaMascotas), 200

# Metodo GET para buscar una mascota por nombre
@app.route('/mascotas/<string:nombre>', methods=['GET'])
def buscar_mascota_por_nombre(nombre):
# Buscar la mascota por nombre
    for mascota in listaMascotas.values():
        if mascota['nombre'] == nombre:
            return jsonify(mascota), 200

# Si no se encuentra la mascota ddevolver mensaje
    return jsonify({"mensaje": "Mascota no encontrada"}), 404

# Metodo POST para agregar una mascota 
@app.route('/mascotas', methods=['POST'])
def agregar_mascota():
    datos = request.get_json()

    if not datos or 'nombre' not in datos or 'edad' not in datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    if datos['nombre'] in listaMascotas:
        return jsonify({"mensaje": "La mascota ya existe"}), 400

    listaMascotas[datos['nombre']] = datos
    return jsonify(datos), 201

# Metodo PUT para modificar una mascota existente en el diccionario
@app.route('/mascotas/<string:nombre>', methods=['PUT'])
def modificar_mascota(nombre):
    # Verificar si la mascota existe
    if nombre not in listaMascotas:
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    # Obtener los datos del json
    datos = request.get_json()
    
    # Validar que el json no este vacio 
    if not datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    #  verifica que no exista duplicado el elemento 
    nuevo_nombre = datos.get('nombre', nombre)
    if nuevo_nombre != nombre and nuevo_nombre in listaMascotas:
        return jsonify({"mensaje": "Ya existe una mascota con ese nombre"}), 400

    # Validar tipos de datos
    for key, value in datos.items():
        if not isinstance(value, (str, int)):
            return jsonify({"mensaje": f"El campo '{key}' debe ser de tipo string o entero."}), 400

    # Actualiza los datos de la mascota existente con los nuevos datos
    for key, value in datos.items():
        listaMascotas[nombre][key] = value

    # Si el nombre se cambio se actualiza la mascota en el diccionario
    if nuevo_nombre != nombre:
        listaMascotas[nuevo_nombre] = listaMascotas.pop(nombre)

    return jsonify(listaMascotas[nuevo_nombre]), 201


# Metodo DELETE para eliminar una mascota
@app.route('/mascotas/<string:nombre>', methods=['DELETE'])
def eliminar_mascota(nombre):
    if nombre not in listaMascotas:
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    del listaMascotas[nombre]
    return jsonify({"mensaje": f"Mascota {nombre} eliminada correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)