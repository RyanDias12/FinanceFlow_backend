from flask  import Flask

app = Flask(__name__)

from backend.routes.transacoes_router import *
from backend.routes.usuarios_router import *