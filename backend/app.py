from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



from backend.routes.usuarios_router import usuarios_blueprint
app.register_blueprint(usuarios_blueprint)

from backend.routes.home_router import home_blueprint
app.register_blueprint(home_blueprint)

from backend.routes.nova_transacao_router import nova_transacao_blueprint
app.register_blueprint(nova_transacao_blueprint)





















