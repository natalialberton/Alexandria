from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import Cliente, TipoUsuario, Usuario, Emprestimo, StatusEmprestimo, Livro, db

emprestimo_gerencia_bp = Blueprint('emprestimo_gerencia', __name__)

#CARREGAMENTO DA PÁGINA
@emprestimo_gerencia_bp.route("/gerenciamento-emprestimos", methods=['GET', 'POST'])
def emprestimo_gerencia():
    if 'usuario' not in session:
        flash('Você precisa fazer o login!')
        return redirect(url_for('auth.login'))
    usuario = session['usuario']
    usuario_obj = Usuario.query.filter_by(usuario=usuario).first()
    tipo_usuario = usuario_obj.tipo_usuario.value
    
    emprestimos = Emprestimo.query.all()
    clientes = Cliente.query.all()
    livros = Livro.query.all()
    return render_template('emprestimo_gerencia.html', usuario=usuario, tipo_usuario=tipo_usuario, 
                           emprestimos=emprestimos, clientes=clientes, livros=livros,
                           TipoUsuario=TipoUsuario, StatusEmprestimo=StatusEmprestimo)


#CADASTRAMENTO
@emprestimo_gerencia_bp.route("/lancamento-emprestimo", methods=["GET", "POST"])
def lancar_emprestimo():
    if request.method == "POST":
        livro_titulo = request.form['livro']
        cliente_nome = request.form['cliente']
        data_emprestimo = request.form['data-emprestimo']
        data_devolucao = request.form['data-devolucao']
        status_emprestimo = request.form['status-emprestimo']
        
        livro = Livro.query.filter_by(titulo=livro_titulo).first()
        cliente = Cliente.query.filter_by(nome=cliente_nome).first()
        
        novo_emprestimo = Emprestimo(id_livro=livro.id, id_cliente=cliente.id, data_emprestimo=data_emprestimo, data_devolucao=data_devolucao, status_emprestimo=status_emprestimo)
        db.session.add(novo_emprestimo)
        db.session.commit()
        
        flash("Lançamento realizado com sucesso!", "success")
        return redirect(url_for('emprestimo_gerencia.estoque_livro'))
    return redirect(url_for('emprestimo_gerencia.emprestimo_gerencia'))


#EDIÇÃO
@emprestimo_gerencia_bp.route("/edita-emprestimo/<int:id>", methods=['GET', 'POST'])
def editar_emprestimo(id:int):
    emprestimo = Usuario.query.get(id)
    if request.method == 'POST':
        emprestimo.tipo_usuario = request.form['status-emprestimo-edicao']
        try:
            db.session.commit()
            flash("Edição realizada com sucesso!", "success")
            return redirect(url_for('emprestimo_gerencia.emprestimo_gerencia'))
        except Exception as e:
            return f"ERROR:{e}"
        
    else:
        return redirect(url_for('emprestimo_gerencia.emprestimo_gerencia'))
