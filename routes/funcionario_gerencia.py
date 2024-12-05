from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import Usuario, TipoUsuario, StatusAtividade, db

funcionario_gerencia_bp = Blueprint('funcionario_gerencia', __name__)

#CARREGAMENTO DA PÁGINA
@funcionario_gerencia_bp.route("/gerenciamento-funcionarios", methods=['GET', 'POST'])
def funcionario_gerencia():
    if 'usuario' not in session:
        flash('Você precisa fazer o login!')
        return redirect(url_for('auth.login'))
    usuario = session['usuario']
    usuario_obj = Usuario.query.filter_by(usuario=usuario).first()
    tipo_usuario = usuario_obj.tipo_usuario.value
    usuarios = Usuario.query.all()
    return render_template('funcionario_gerencia.html', usuario=usuario, tipo_usuario=tipo_usuario, usuarios=usuarios, TipoUsuario=TipoUsuario, StatusAtividade=StatusAtividade)


#CADASTRAMENTO
@funcionario_gerencia_bp.route("/cadastramento-funcionarios", methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        usuario = request.form['usuario']
        email = request.form['email']
        telefone = request.form['telefone']
        tipo_usuario = request.form['tipo-usuario']
        senha = request.form['senha']
        confirma_senha = request.form['confirma-senha']
        
        if senha != confirma_senha:
            flash("As senhas não correspondem!", "error")
            return redirect(url_for('funcionario_gerencia.cadastrar_funcionario'))
        
        usuario_existente = Usuario.query.filter_by(usuario=usuario).first()
        email_existente = Usuario.query.filter_by(email=email).first()

        if usuario_existente:
            flash("Usuário já cadastrado", "error")
            return redirect(url_for('funcionario_gerencia.cadastrar_funcionario'))
                
        if email_existente:
            flash("Email já cadastrado", "error")
            return redirect(url_for('funcionario_gerencia.cadastrar_funcionario'))
        
        novo_usuario = Usuario(nome=nome, usuario=usuario, email=email, telefone=telefone, tipo_usuario=tipo_usuario, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('funcionario_gerencia.funcionario_gerencia'))
    return redirect(url_for('funcionario_gerencia.funcionario_gerencia'))


#EDIÇÃO
@funcionario_gerencia_bp.route("/edita-funcionario/<int:id>", methods=['GET', 'POST'])
def editar_funcionario(id:int):
    funcionario = Usuario.query.get(id)
    if request.method == 'POST':
        funcionario.nome = request.form['nome-edicao']
        funcionario.usuario = request.form['usuario-edicao']
        funcionario.email = request.form['email-edicao']
        funcionario.telefone = request.form['telefone-edicao']
        funcionario.tipo_usuario = request.form['tipo-usuario-edicao']
        funcionario.status_atividade = request.form['status-atividade-edicao']
        
        senha = request.form['senha-edicao']
        confirma_senha = request.form['confirma-senha-edicao']
        
        if senha != confirma_senha:
            flash("As senhas não correspondem!", "error")
            return redirect(url_for('funcionario_gerencia.editar_funcionario'))
        
        funcionario.senha = senha
        try:
            db.session.commit()
            flash("Edição realizada com sucesso!", "success")
            return redirect(url_for('funcionario_gerencia.funcionario_gerencia'))
        except Exception as e:
            return f"ERROR:{e}"
        
    else:
        return redirect(url_for('funcionario_gerencia.funcionario_gerencia'))
    
        