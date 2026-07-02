from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Importa e registra o Blueprint de usuários
from backend.routes.usuarios_router import usuarios_blueprint
app.register_blueprint(usuarios_blueprint)

# Se você ainda não mudou o transacoes_router para Blueprint, mantenha-o assim por enquanto:
from backend.routes.transacoes_router import *