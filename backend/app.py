from flask  import Flask

app = Flask(__name__)

from routes.transacoes_router import *
from routes.usuarios_router import *