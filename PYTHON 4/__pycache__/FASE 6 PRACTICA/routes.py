import json
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Usuario, Producto

api_bp = Blueprint('api', __name__)

@api_bp.route('/usuario/registrar', methods=['POST'])
def registrar():
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'])
    nuevo_usuario = Usuario(
        username=data['username'],
        password_hash=hashed_pw,
        rol=data.get('rol', 'Operario')
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"msj": "Usuario creado", "user": nuevo_usuario.serializar()}), 201

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Usuario.query.filter_by(username=data.get('username')).first()
    
    if user and check_password_hash(user.password_hash, data.get('password')):
        # Guardamos identidad como string JSON para evitar errores de tipo
        identidad = json.dumps({"username": user.username, "rol": user.rol})
        token = create_access_token(identity=identidad)
        return jsonify({"token": token}), 200
    
    return jsonify({"error": "Credenciales inválidas"}), 401

@api_bp.route('/productos', methods=['POST'])
@jwt_required()
def crear_producto():
    id_actual = json.loads(get_jwt_identity())
    if id_actual.get("rol") != "Admin":
        return jsonify({"msg": "Error 403: Requiere rol Admin"}), 403

    data = request.get_json()

    # ESTA PARTE EVITA EL KEYERROR:
    if not data or 'nombre' not in data or 'precio' not in data:
        return jsonify({"error": "Faltan datos", "detalle": "Debes enviar 'nombre' y 'precio'"}), 400

    nuevo_p = Producto(nombre=data['nombre'], precio=data['precio'])
    db.session.add(nuevo_p)
    db.session.commit()
    return jsonify({"msj": "Producto creado", "data": nuevo_p.serializar()}), 201