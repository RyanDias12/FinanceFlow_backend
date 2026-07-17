from flask import Blueprint, request, jsonify
from backend.database.db.nova_transacao.nova_transacao_db import forma_pagamento, categoria_receitas, categoria_despesas,insert_nova_transacao




nova_transacao_blueprint = Blueprint("nova_transacao", __name__)

@nova_transacao_blueprint.route("/dados_cadastro_nova_transacao", methods=["GET"])
def dados_cadastro_nova_transacao():
    dados_forma_pagamento = forma_pagamento()
    dados_categoria_receitas = categoria_receitas()
    dados_categoria_despesas = categoria_despesas()
    
    dados = {
        "formas_pagamento" : dados_forma_pagamento,
        "categoria_receitas" : dados_categoria_receitas,
        "categoria_despesas" : dados_categoria_despesas,
        
    }
    
    if dados_forma_pagamento:
        return jsonify({
            "success": True,
            "dados": dados
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Não consta dados no banco de dados"
        }), 500

@nova_transacao_blueprint.route("/insert_nova_transacao", methods=["POST"])
def insert_nova_transacao_route():
    dados = request.get_json()

    print("Dados recebidos:", dados)  # Adicione esta linha para depuração
    
    valor = dados.get("valor")
    descricao = dados.get("descricao")
    data = dados.get("data")
    id_forma_pagamento = dados.get("id_forma_pagamento")
    id_tipo_transacao = dados.get("id_tipo_transacao")
    id_categoria = dados.get("id_categoria")
    id_usuario = dados.get("id_usuario")

    if not all([valor, descricao, data, id_forma_pagamento, id_tipo_transacao, id_categoria, id_usuario]):
        return jsonify({"erro": "Dados incompletos"}), 400

    novo_id = insert_nova_transacao(
        valor=valor,
        descricao=descricao,
        data=data,
        id_forma_pagamento=id_forma_pagamento,
        id_tipo_transacao=id_tipo_transacao,
        id_categoria=id_categoria,
        id_usuario=id_usuario
    )
    

    return jsonify({"mensagem": "Transação criada com sucesso", "id": novo_id}), 201
