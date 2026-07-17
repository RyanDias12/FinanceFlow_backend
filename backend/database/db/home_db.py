from backend.database.connection import conectar

def buscar_transacoes(id_usuario):
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                t.id,
                t.valor,
                t.descricao,
                c.nome AS categoria_transacao,
                txt_icon,
                color_icon,
                t.data,
                fp.nome AS forma_pagamento,
                tp_t.nome AS tipo_transacao,
                tp_t.id AS id_tipo_transacao,
                t.id_usuario 
            FROM
                transacoes t
                JOIN categoria_transacao c ON t.id_categoria = c.id
                JOIN forma_pagamento fp ON t.id_forma_pagamento = fp.id
                JOIN tipo_transacao tp_t ON t.id_tipo_transacao = tp_t.id 
            WHERE
                t.id_usuario = ?
            ORDER BY
                t.id DESC 
                LIMIT 5
        """, (id_usuario,))

        resultado = cursor.fetchall()

        if resultado:
            return [dict(row) for row in resultado]

        return None

    finally:
        conn.close()
        
def card_home(id_usuario):

    id_usuario_sql = id_usuario
    
    def total_receitas(id_usuario):
        conn = conectar()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT
                    SUM(
                        CASE
                            WHEN id_tipo_transacao = 1 THEN valor
                            WHEN id_tipo_transacao = 2 THEN -valor
                            ELSE 0
                        END
                    ) AS saldo_total
                FROM transacoes
                WHERE id_usuario = ?
            """, (id_usuario,))

            resultado = cursor.fetchone()

            if resultado and resultado[0] is not None:
                return resultado[0]

            return 0

        finally:
            conn.close()
                

            
    def total_receitas_mensal(id_usuario):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT
                    id_usuario,
                    id_tipo_transacao,
                    SUM( valor ) AS valor_total 
                FROM
                    transacoes 
                WHERE
                    id_tipo_transacao = 1 
                    AND id_usuario = ?
                    AND substr( data, 4, 7 ) = strftime( '%m/%Y', 'now' )
            """, (id_usuario,))

            resultado = cursor.fetchall()

            if resultado:
                return resultado[0][2]


            return None

        finally:
            conn.close()
            
    def total_despesas_mensal(id_usuario):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT
                    id_usuario,
                    id_tipo_transacao,
                    SUM( valor ) AS valor_total 
                FROM
                    transacoes 
                WHERE
                    id_tipo_transacao = 2
                    AND id_usuario = ?
                    AND substr( data, 4, 7 ) = strftime( '%m/%Y', 'now' )
            """, (id_usuario,))

            resultado = cursor.fetchall()

            if resultado:
                return resultado[0][2]


            return None

        finally:
            conn.close()
            
    def gastos_mensal_por_categorias(id_usuario):
        conn = conectar()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT
                    c.nome AS categoria,
                    SUM(t.valor) AS total,
                    color_icon
                FROM transacoes t
                JOIN categoria_transacao c
                    ON t.id_categoria = c.id
                WHERE
                    t.id_tipo_transacao = 2
                    AND substr(t.data, 4, 7) = strftime('%m/%Y', 'now')
                    AND t.id_usuario = ?
                GROUP BY
                    c.id, c.nome
                ORDER BY
                    total DESC
            """, (id_usuario,))

            resultado = cursor.fetchall()

            return [dict(row) for row in resultado]

        finally:
            conn.close()
            
    def dados_usuario(id_usuario):
        conn = conectar()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT id, nome, email, cpf, telefone, tema
                FROM usuarios
                WHERE id = ?
            """, (id_usuario,))

            resultado = cursor.fetchall()

            return [dict(row) for row in resultado]

        finally:
            conn.close()
            
            
    resultado = [
        total_receitas(id_usuario_sql), 
        total_receitas_mensal(id_usuario_sql),
        total_despesas_mensal(id_usuario_sql),
        gastos_mensal_por_categorias(id_usuario_sql),
        dados_usuario(id_usuario_sql)
    ]
            
            
    return resultado
    
    

    
    

   
    
    

    

    
    