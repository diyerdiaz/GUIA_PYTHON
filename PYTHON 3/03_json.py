from flask import Flask, jsonify, Response

app = Flask(__name__)

sensores_trapiche: list[dict] = [
    {"id":"S1", "Tipo":"temperatura","valor":95.5, "estado":"Activo"},
    {"id":"S2", "Tipo":"Presion","valor":40.2, "estado": "Alerta"}
]

@app.route('/api/sensores', methods=['GET'])
def obtener_sensores() -> Response:
    return jsonify({
        "total_registro": len(sensores_trapiche),
        "data": sensores_trapiche
    })

@app.route('/api/sensores/<string:id_sensor>', methods=['GET'])
def buscar_sensor(id_sensor: str) -> tuple[Response,int]:
    for sensor in sensores_trapiche:
        if sensor["id"] == id_sensor:
            return jsonify(sensor), 200
    return jsonify({"error":"sensor no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
