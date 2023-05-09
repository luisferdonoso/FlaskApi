from flask import Flask, request, jsonify
from  sqlite import create_table
import sqlite 

app = Flask(__name__)

@app.route("/sqlite", methods=["GET"])
def get_compradores():
    comprador = sqlite.get_compradores()
    return jsonify(comprador)


@app.route("/sqlite", methods=["POST"])
def insert_comprador():
    detalles_comprador = request.get_json()
    id = detalles_comprador["id"]
    nombre = detalles_comprador["nombre"]
    edad = detalles_comprador["edad"]
    local=  detalles_comprador ["local"]
    producto =  detalles_comprador ["producto"]
    precio = detalles_comprador ["precio"]
    cantidad =  detalles_comprador ["cantidad"]
    fecha = detalles_comprador ["fecha"]
    insertar_comprador = sqlite.insert_comprador(id, nombre, edad, local, producto, precio, cantidad, fecha)
    return jsonify(insertar_comprador)



@app.route("/sqlite", methods=["PUT"])
def update_comprador():
    detalles_comprador = request.get_json()
    id = detalles_comprador["id"]
    nombre = detalles_comprador["nombre"]
    edad = detalles_comprador["edad"]
    local=  detalles_comprador ["local"]
    producto =  detalles_comprador ["producto"]
    precio = detalles_comprador ["precio"]
    cantidad =  detalles_comprador ["cantidad"]
    fecha = detalles_comprador ["fecha"]
    actualizar_comprador = sqlite.update_comprador(id, nombre, edad, local, producto, precio, cantidad, fecha)
    return jsonify(actualizar_comprador)


@app.route("/sqlite/<id>", methods=["DELETE"])
def delete_compradores(id):
    borrar_comprador = sqlite.delete_comprador(id)
    return jsonify(borrar_comprador)


@app.route("/sqlite/<id>", methods=["GET"])
def get_comprador_id(id):
    get_comprador = sqlite.get_comprador_by_id(id)
    return jsonify(get_comprador)


if __name__ == "__Api__":
    create_table()
    app.run(host = '0.0.0.0', port=8000, debug=False)
