from flask import Blueprint, request, jsonify
from backend.database.db.usuarios.usuarios_db import buscar_usuario, buscar_email, salvar_usuario

usuarios_blueprint = Blueprint('usuarios', __name__)

@usuarios_blueprint.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    usuario = dados.get("usuario")
    senha = dados.get("senha")
    resultado = buscar_usuario(usuario, senha)

    if resultado:
        return jsonify({
            "success": True,
            "usuario": resultado
        }), 200

    return jsonify({
        "success": False,
        "message": "Usuário ou senha inválidos"
    }), 401

@usuarios_blueprint.route("/recuperar-login", methods=["POST"])
def recuperar_login():
    dados = request.get_json()
    email = dados.get("email")
    resultado = buscar_email(email)

    if resultado:
        return jsonify({
            "success": True,
            "email": resultado["email"],
            "usuario": resultado["usuario"],
            "senha": resultado["senha"]
        }), 200

    return jsonify({
        "success": False,
        "message": "Email não encontrado"
    }), 404
    
@usuarios_blueprint.route("/novaConta", methods=["POST"])
def cadastro():
    dados = request.get_json()
    resultado = salvar_usuario(dados)

    if resultado:
        return jsonify({
            "success": True,
            "message": "Usuário cadastrado com sucesso"
        }), 201 
    else:
        return jsonify({
            "success": False,
            "message": "Erro ao cadastrar usuário"
        }), 500