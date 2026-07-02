from database.connection import conectar

def buscar_usuario(usuario, senha):
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, email, cpf, telefone, tema
            FROM usuarios
            WHERE usuario = ?
            AND senha = ?
        """, (usuario, senha))

        resultado = cursor.fetchone()

        if resultado:
            return dict(resultado)

        return None

    finally:
        conn.close()


def buscar_email(email):
    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT email, usuario, senha
            FROM usuarios
            WHERE email = ?
        """, (email,))

        resultado = cursor.fetchone()

        if resultado:
            return dict(resultado)

        return None

    finally:
        conn.close()
        
def salvar_usuario(usuario):

    conn = conectar()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios
            (
                nome,
                email,
                cpf,
                telefone,
                usuario,
                senha,
                tema
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            usuario["nome"],
            usuario["email"],
            usuario["cpf"],
            usuario["telefone"],
            usuario["usuario"],
            usuario["senha"],
            1
        ))

        conn.commit()

        return True

    except Exception as erro:
        print(erro)
        return False

    finally:
        conn.close()

    