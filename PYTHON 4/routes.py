
from flask import Blueprint, request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Usuario

api_bp = Blueprint('api', __name__)


@api_bp.route('/usuario/registrar', methods=['POST'])
def registrar_usuario() -> tuple[Response, int]:
    try:
        payload = request.get_json()
        clave_segura = generate_password_hash(payload['password'])

        nuevo_user = Usuario(
            username=payload['username'],
            password_hash=clave_segura,
            rol=payload.get('rol', 'Operario')
        )

        db.session.add(nuevo_user)
        db.session.commit()

        return jsonify({"mensaje": "exito", "data": nuevo_user.serializar()}), 201
    except Exception as e:
        db.session.rollback()  
        return jsonify({"error": "Fallo de integridad", "detalle": str(e)}), 400


@api_bp.route('/usuarios', methods=["GET"])
def listar_usuario() -> tuple[Response, int]:
    try:
        
        pagina = request.args.get('page', 1, type=int)

        paginacion = Usuario.query.paginate(page=pagina, per_page=10, error_out=False)
        resultado = [u.serializar() for u in paginacion.items]

        return jsonify({
            "pagina_actual": paginacion.page,
            "total_pagina": paginacion.pages,
            "usuarios": resultado
        }), 200
    except Exception as e:
        return jsonify({"error": "Error al listar", "detalle": str(e)}), 500

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
import json

@api_bp.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    usuario = Usuario.query.filter_by(username=payload.get('username')).first()

    if usuario and check_password_hash(usuario.password_hash, payload.get('password')):
        
        data = {"username": usuario.username, "rol": usuario.rol}
        
        
        identidad_firme = str(json.dumps(data)) 
        
        token_acceso = create_access_token(identity=identidad_firme)

        return jsonify({"token": token_acceso}), 200

    return jsonify({"error": "Credenciales inválidas"}), 401


from flask_jwt_extended import jwt_required, get_jwt_identity

@api_bp.route('/inventario/critico', methods=['POST'])
@jwt_required()
def modificar_inventario() -> tuple[Response, int]:
    
    identidad_recibida = get_jwt_identity()
    usuario_actual = json.loads(identidad_recibida)

    
    if usuario_actual.get("rol") != "Admin":
        return jsonify({"error": "Forbidden: requiere privilegios de administrador"}), 403
    
    return jsonify({
        "mensaje": "Acceso concedido al servidor crítico.",
        "operador": usuario_actual["username"]
    }), 200