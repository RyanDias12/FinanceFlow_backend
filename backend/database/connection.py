import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "financeflow.db")

import sqlite3

def conectar():
    print("Banco:", DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL,
            descricao TEXT,
            categoria TEXT,
            data TEXT,
            forma_pagamento TEXT,
            tipo TEXT
        )
    """)

    conn.commit()
    conn.close()