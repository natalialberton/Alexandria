from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import Usuario, Cliente, db
import re

cliente_gerencia_bp = Blueprint('cliente_gerencia', __name__)

#CARREGAMENTO DA PÁGINA
@cliente_gerencia_bp.route("/gerenciamento-clientes",  methods=["GET", "POST"])
def cliente_gerencia():
    if 'usuario' not in session:
        flash('Você precisa fazer o login!')
        return redirect(url_for('auth.login'))
    usuario = session['usuario']
    usuario_obj = Usuario.query.filter_by(usuario=usuario).first()
    tipo_usuario = usuario_obj.tipo_usuario.value
    clientes = Cliente.query.all()
    return render_template('cliente_gerencia.html', usuario=usuario, tipo_usuario=tipo_usuario, clientes=clientes)


#CADASTRAMENTO
@cliente_gerencia_bp.route("/cadastramento-clientes", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        
        email_padrao = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_padrao, email):
            flash("Por favor, insira um email válido!", "error")
            return redirect(url_for('cliente_gerencia.cadastrar_cliente'))
        
        cliente_existente = Cliente.query.filter_by(email=email).first()
        
        if cliente_existente:
            flash("Email já cadastrado!", "error")
            return redirect(url_for('cliente_gerencia.cliente_gerencia'))
        
        novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
        db.session.add(novo_cliente)
        db.session.commit()
        
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('cliente_gerencia.cliente_gerencia'))
    return redirect(url_for('cliente_gerencia.cliente_gerencia'))


#EDIÇÃO
@cliente_gerencia_bp.route("/edita-cliente/<int:id>", methods=['POST', 'GET'])
def editar_cliente(id:int):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.nome = request.form['cliente-nome-edicao']
        cliente.email = request.form['cliente-email-edicao']
        cliente.telefone = request.form['cliente-telefone-edicao']
        try:
            db.session.commit()
            return redirect(url_for('cliente_gerencia.cliente_gerencia'))
        except Exception as e:
            return f"ERROR:{e}"
    else:
        return redirect(url_for('cliente_gerencia.cliente_gerencia'))