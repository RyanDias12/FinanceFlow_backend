from flask import Blueprint, request, jsonify
from backend.database.db.home_db import buscar_transacoes, card_home



home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/dados_home/<int:id_usuario>", methods=["GET"])
def dados_home(id_usuario):
    resultado_transacoes = buscar_transacoes(id_usuario)
    resultado_card = card_home(id_usuario)          
    
    
    dados = {
        "ultimas_transacoes" : resultado_transacoes,
        "total_receitas" : resultado_card[0],
        "total_receitas_mensal" : resultado_card[1],
        "total_despesas_mensal" : resultado_card[2],
        "gastos_mensal_por_categorias": resultado_card[3],
        "dados_usuario":resultado_card[4]
    }
    
    if resultado_transacoes:
        return jsonify({
            "success": True,
            "dados": dados
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Não consta dados no banco de dados"
        }), 500

