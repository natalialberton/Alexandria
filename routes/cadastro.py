from flask import Blueprint, render_template, request, session, redirect, flash, url_for, get_flashed_messages
from models import Usuario, db
import re

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    if 'usuario' in session:
        return redirect(url_for('home.home'))
    
    if request.method == "POST":
        usuario = request.form['usuario-cadastro']
        nome = request.form['nome-cadastro']
        email = request.form['email-cadastro']
        telefone = request.form['telefone-cadastro']
        senha = request.form['senha-cadastro']
        confirma_senha = request.form['confirma-senha-cadastro']

        # Verifica se o email é válido
        email_padrao = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_padrao, email):
            flash("Por favor, insira um email válido!", "error")
            return redirect(url_for('cadastro.cadastrar'))
                
        if senha != confirma_senha:
            flash("As senhas não correspondem!", "error")
            return redirect(url_for('cadastro.cadastrar'))
                
        usuario_existente = Usuario.query.filter_by(usuario=usuario).first()
        email_existente = Usuario.query.filter_by(email=email).first()

        if usuario_existente:
            flash("Usuário já cadastrado", "error")
            return redirect(url_for('cadastro.cadastrar'))
                
        if email_existente:
            flash("Email já cadastrado", "error")
            return redirect(url_for('cadastro.cadastrar'))
                
        novo_usuario = Usuario(nome=nome, usuario=usuario, telefone=telefone, senha=senha, email=email)
        db.session.add(novo_usuario)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", "success")
        session['usuario'] = usuario
        return redirect(url_for('cadastro.cadastrar'))
    return render_template('index.html')
