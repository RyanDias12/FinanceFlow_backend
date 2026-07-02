from flask  import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


from backend.routes.transacoes_router import *
from backend.routes.usuarios_router import *