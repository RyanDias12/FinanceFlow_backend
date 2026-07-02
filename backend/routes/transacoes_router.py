from app import app
from flask import request, jsonify

from models.transacao_model import Transacao_model
from database.db.transacao_db import salvar_transacao

@app.route("/novaTransacao", methods=["POST"])
def nova_transacao():

    dados = request.json

    transacao = Transacao_model(
        valor=dados["valor"],
        descricao=dados["descricao"],
        categoria=dados["categoria"],
        forma_pagamento=dados["forma_pagamento"],
        data=dados["data"],
        tipo=dados["tipo"]
    )

    salvar_transacao(transacao)

    return jsonify({"status": "ok"})