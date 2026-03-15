import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask (__name__)
CORS(app)

@app.route('/api/config', methods=['GET'])
def obtener_config():
    ambiente_actual = os.getenv("FLASK_ENV","produccion")
    puerto_asignado = os.getenv("PORT",5000)

    return jsonify({
        "status": "servidor seguro en linea",
        "entorno": ambiente_actual,
        "puerto": puerto_asignado

    })
if __name__ == '__main__':
    debug_mode = os.getenv ("FASK_DEBUG","false").lower() == "true" 
    port = int(os.getenv("PORT",5000))
    app.run(host='0.0.0.0',port=port, debug=debug_mode)
    
