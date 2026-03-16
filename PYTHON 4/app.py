import os
from flask import Flask
from dotenv import load_dotenv
from routes import api_bp
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)

# Configuración
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tropiche_db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CORRECCIÓN 1: Evitar que JWT falle si la variable no existe en el .env
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'clave-secreta-de-respaldo')

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Crear tablas
with app.app_context():
    db.create_all()

app.register_blueprint(api_bp, url_prefix='/api') 

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    # CORRECCIÓN 2: Asegurar que debug sea booleano correctamente
    debug_env = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    
    # Agregamos host='0.0.0.0' para que Postman encuentre el puerto más fácil
    app.run(host='0.0.0.0', port=port, debug=debug_env)

    jwt = JWTManager(app)