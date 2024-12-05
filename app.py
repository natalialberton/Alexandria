from flask import Flask
from config import Config
from models import db
from routes.auth import auth_bp
from routes.cadastro import cadastro_bp
from routes.home import home_bp
from routes.livro_gerencia import livro_gerencia_bp
from routes.cliente_gerencia import cliente_gerencia_bp
from routes.funcionario_gerencia import funcionario_gerencia_bp
from routes.emprestimo_gerencia import emprestimo_gerencia_bp

#Setup App
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'Alexandria-2024-NATALI'

#Inicializa DB
db.init_app(app)

#Registra ROTAS webpages
app.register_blueprint(auth_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(home_bp)
app.register_blueprint(livro_gerencia_bp)
app.register_blueprint(cliente_gerencia_bp)
app.register_blueprint(funcionario_gerencia_bp)
app.register_blueprint(emprestimo_gerencia_bp)

#Conexão DB
with app.app_context():
    db.create_all()

#Runner e Debugger
if __name__ == "__main__":
    app.run(debug=True, port=8080)