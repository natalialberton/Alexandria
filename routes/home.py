from flask import Blueprint, render_template, redirect, url_for, session, flash
from models import Usuario

home_bp = Blueprint('home', __name__)

@home_bp.route("/home", methods=["GET", "POST"])
def home():
    usuario = session['usuario']
    if 'usuario' not in session:
        flash('Você precisa fazer o login!')
        return redirect(url_for('auth.login'))
    #PUXANDO DADOS PARA PEGAR O TIPO DE USUÁRIO E MUDAR PERMISSÕES NO GERENCIAMENTO
    usuario_obj = Usuario.query.filter_by(usuario=usuario).first()
    tipo_usuario = usuario_obj.tipo_usuario.value

    return render_template('home.html', usuario=usuario, tipo_usuario=tipo_usuario)