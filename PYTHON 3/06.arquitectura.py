import os
from flask import Flask,jsonify,Request,Response
from flask_cors  import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

class InventarioTrapiche:
    def __init__(self):
        self._producto: list[dict] = []
        
    def agregar_lote(self,tipo: str,kilos:float) -> dict :
        lote = {"id": len(self._producto) + 1, "tipo":tipo,"kilos": kilos}
        self._productos.append(lote)
        return lote
    
    def obtener_todos(self) -> list[dict]:
        return self._producto
    
    



gestor_inventario = InventarioTrapiche()  

@app.route('/api/inventario', methods=['GET'])
def ver_inventario() -> tuple[Response,int]:
    datos = gestor_inventario.obtener_todos()
    return jsonify({"total": len(datos),"lotes":datos}),200

@app.route('/api/inventario', methods =['POST'])
def  registrar_lote() ->tuple[Response,int]:
        try:
            payload = Request.get_json()
            nuevo_lote = gestor_inventario.agregar_lote(payload["tipo"],payload["kilo"])
            return jsonify({"mensaje":"lote registrado","data": nuevo_lote}),201
        except KeyError:
            return jsonify ({"error":"Estructura Json invalida."}), 400
if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT",5000)), debug=os.getenv ("FLASK_DEBUG")) 