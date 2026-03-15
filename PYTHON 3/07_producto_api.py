import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

class Producto:

    def __init__(self, nombre: str, precio: float, stock: int, id: int):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio,
            "stock": self.__stock
        }

class Inventario:

    def __init__(self):
        self.__productos = []

    def agregar_producto(self, nombre, precio, stock):
        nuevo = Producto(nombre, precio, stock, len(self.__productos) + 1)
        self.__productos.append(nuevo)
        return nuevo

    def listar_productos(self):
        return [p.to_dict() for p in self.__productos]


inventario = Inventario()



@app.route("/api/productos", methods=["GET"])
def obtener_productos() -> tuple[Response, int]:

    productos = inventario.listar_productos()

    return jsonify({
        "total": len(productos),
        "productos": productos
    }), 200


@app.route("/api/productos", methods=["POST"])
def crear_producto() -> tuple[Response, int]:

    try:
        data = request.get_json()

        nuevo = inventario.agregar_producto(
            data["nombre"],
            data["precio"],
            data["stock"]
        )

        return jsonify({
            "mensaje": "Producto creado",
            "producto": nuevo.to_dict()
        }), 201

    except KeyError:
        return jsonify({
            "error": "JSON inválido"
        }), 400


if __name__ == "__main__":

    app.run(
        port=int(os.getenv("PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG") == "1"
    )