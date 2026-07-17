from backend.database.connection import conectar

def forma_pagamento():
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * 
            FROM forma_pagamento
        """,)

        resultado = cursor.fetchall()

        if resultado:
            return [dict(row) for row in resultado]

        return None

    finally:
        conn.close()
        
def categoria_receitas():
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                * 
            FROM
                categoria_transacao 
            WHERE
                id_tipo_transacao = 1 
                AND status = 1
        """,)

        resultado = cursor.fetchall()

        if resultado:
            return [dict(row) for row in resultado]

        return None

    finally:
        conn.close()
        
def categoria_despesas():
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                * 
            FROM
                categoria_transacao 
            WHERE
                id_tipo_transacao = 2 
                AND status = 1
        """,)

        resultado = cursor.fetchall()

        if resultado:
            return [dict(row) for row in resultado]

        return None

    finally:
        conn.close()
        
def insert_nova_transacao(valor,descricao,data,id_forma_pagamento,id_tipo_transacao,id_categoria,id_usuario):
    conn = conectar()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO transacoes (valor, descricao, data, id_forma_pagamento, id_tipo_transacao, id_categoria, id_usuario)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (valor,descricao,data,id_forma_pagamento,id_tipo_transacao,id_categoria,id_usuario))

        conn.commit()

        return cursor.lastrowid 

    finally:
        conn.close()