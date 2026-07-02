from database.connection import conectar

def salvar_transacao(transacao):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transacoes
        (
            valor,
            descricao,
            categoria,
            forma_pagamento,
            data,
            tipo
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        transacao.valor,
        transacao.descricao,
        transacao.categoria,
        transacao.forma_pagamento,
        transacao.data,
        transacao.tipo
    ))

    conn.commit()
    conn.close()