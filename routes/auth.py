from flask import Blueprint, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from models import Usuario, StatusAtividade

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def passlogin():
    return render_template('index.html')

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form['senha']

        # Verifica se o usuário existe
        usuario = Usuario.query.filter_by(usuario=usuario).first()
        if usuario and senha == usuario.senha:
            if usuario.status_atividade == StatusAtividade.ATIVO:
                session['usuario'] = usuario.usuario
                flash("Login realizado com sucesso!", "success")
                return redirect(url_for('home.home'))
            else:
                flash("Sua conta está inativada!", "error")
                return redirect(url_for('auth.login'))
        else:
            flash("Usuário ou senha inválidos", "error")
    return render_template('index.html')

@auth_bp.route("/logout")
def logout():
    session.pop('usuario', None)
    flash("Volte sempre!")
    return redirect(url_for('auth.login'))