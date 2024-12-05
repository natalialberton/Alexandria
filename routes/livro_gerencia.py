from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import Usuario, Categoria, Autor, Livro, db

livro_gerencia_bp = Blueprint('livro_gerencia', __name__)

#CARREGAMENTO DA PÁGINA
@livro_gerencia_bp.route("/gerenciamento-livros", methods=["GET", "POST"])
def livro_gerencia():
    if 'usuario' not in session:
        flash('Você precisa fazer o login!')
        return redirect(url_for('auth.login'))
    usuario = session['usuario']
    usuario_obj = Usuario.query.filter_by(usuario=usuario).first()
    tipo_usuario = usuario_obj.tipo_usuario.value

    categorias = Categoria.query.all()
    autores = Autor.query.all()
    livros = Livro.query.all()
    return render_template('livro_gerencia.html', usuario=usuario, tipo_usuario=tipo_usuario, 
                           categorias=categorias, autores=autores, livros=livros)


#CADASTRAMENTO
@livro_gerencia_bp.route("/cadastramento-categorias", methods=['GET', 'POST'])
def cadastrar_categoria():
    if request.method == "POST":
        nome_categoria = request.form['nome-categoria']

        categoria_existente = Categoria.query.filter_by(nome=nome_categoria).first()

        if categoria_existente:
            flash("Categoria já cadastrada", "info")
            return redirect(url_for('livro_gerencia.livro_gerencia'))
        
        nova_categoria = Categoria(nome=nome_categoria)
        db.session.add(nova_categoria)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    return redirect(url_for('livro_gerencia.livro_gerencia'))


@livro_gerencia_bp.route("/cadastramento-autores", methods=['GET', 'POST'])
def cadastrar_autor():
    if request.method == "POST":
        nome_autor = request.form['nome-autor']
        ano_nascimento = request.form['ano-nascimento']
        ano_morte = request.form['ano-morte']

        autor_existente = Autor.query.filter_by(nome=nome_autor).first()

        if autor_existente:
            flash("Autor já cadastrado", "info")
            return redirect(url_for('livro_gerencia.livro_gerencia'))
        
        novo_autor = Autor(nome=nome_autor, ano_nascimento=ano_nascimento, ano_morte=ano_morte)
        db.session.add(novo_autor)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    return redirect(url_for('livro_gerencia.livro_gerencia'))


@livro_gerencia_bp.route("/cadastramento-livros", methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == "POST":
        titulo = request.form['titulo']
        isnb = request.form['isnb']
        nome_autor = request.form['autor']
        nome_categoria = request.form['categoria']
        ano_publicacao = request.form['ano-publicacao']
        estoque = request.form['estoque']
        
        autor = Autor.query.filter_by(nome=nome_autor).first()
        categoria = Categoria.query.filter_by(nome=nome_categoria).first()

        if len(isnb) > 13:
            flash("O ISNB precisa ter no mínimo 13 números!", "error")
            return redirect(url_for('livro_gerencia.livro_gerencia'))

        livro_existente = Livro.query.filter_by(isnb=isnb).first()
        if livro_existente:
            flash("Livro já cadastrado!", "info")
            return redirect(url_for('livro_gerencia.livro_gerencia'))
        
        novo_livro = Livro(titulo=titulo, isnb=isnb, id_autor=autor.id, id_categoria=categoria.id, ano_publicacao=ano_publicacao, estoque=estoque)
        db.session.add(novo_livro)
        db.session.commit()
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    return redirect(url_for('livro_gerencia.livro_gerencia'))



#EXCLUSÃO
@livro_gerencia_bp.route("/deleta-categoria/<int:id>", methods=['POST', 'GET'])
def deleta_categoria(id:int):
    categoria = Categoria.query.get(id)
    try:
        db.session.delete(categoria)
        db.session.commit()
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    except Exception as e:
        return f"ERROR:{e}"
    

@livro_gerencia_bp.route("/deleta-autor/<int:id>", methods=['POST', 'GET'])
def deleta_autor(id:int):
    autor = Autor.query.get(id)
    try:
        db.session.delete(autor)
        db.session.commit()
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    except Exception as e:
        return f"ERROR:{e}"
    

@livro_gerencia_bp.route("/deleta-livro/<int:id>", methods=['POST', 'GET'])
def deleta_livro(id:int):
    livro = Livro.query.get(id)
    try:
        db.session.delete(livro)
        db.session.commit()
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    except Exception as e:
        return f"ERROR:{e}"



#EDIÇÃO
@livro_gerencia_bp.route("/edita-categoria/<int:id>", methods=['POST', 'GET'])
def edita_categoria(id:int):
    categoria = Categoria.query.get(id)
    if request.method == "POST":
        categoria.nome = request.form['nome-categoria-edicao']
        try:
            db.session.commit()
            return redirect(url_for('livro_gerencia.livro_gerencia'))
        except Exception as e:
            return f"ERROR:{e}"
    else:       
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    

@livro_gerencia_bp.route("/edita-autor/<int:id>", methods=['POST', 'GET'])
def edita_autor(id:int):
    autor = Autor.query.get(id)
    if request.method == "POST":
        autor.nome = request.form['nome-autor-edicao']
        autor.ano_nascimento = request.form['ano-nascimento-edicao']
        autor.ano_morte = request.form['ano-morte-edicao']
        try:
            db.session.commit()
            return redirect(url_for('livro_gerencia.livro_gerencia'))
        except Exception as e:
            return f"ERROR:{e}"   
    else:
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    


@livro_gerencia_bp.route("/edita-livro/<int:id>", methods=['POST', 'GET'])
def edita_livro(id:int):
    livro = Livro.query.get(id)
    if request.method == "POST":
        livro.titulo = request.form['titulo-edicao']
        livro.isnb = request.form['isnb-edicao']
        livro.ano_publicacao = request.form['ano-publicacao-edicao']
        livro.estoque = request.form['estoque-edicao']
        nome_categoria = request.form['categoria-edicao']
        nome_autor = request.form['autor-edicao']
        
        autor = Autor.query.filter_by(nome=nome_autor).first()
        categoria = Categoria.query.filter_by(nome=nome_categoria).first()
        
        livro.id_autor = autor.id
        livro.id_categoria = categoria.id
        try:
            db.session.commit()
            return redirect(url_for('livro_gerencia.livro_gerencia'))
        except Exception as e:
            return f"ERROR:{e}"
    else:
        return redirect(url_for('livro_gerencia.livro_gerencia'))
    

@livro_gerencia_bp.route("/pesquisa-categorias", methods=['GET', 'POST'])
def pesquisar_categoria():
    if request.method == 'GET':
        categoria = request.form['pesquisa-categoria']
        categoria_existente = Categoria.query.filter_by(nome=categoria).first()

        if not categoria_existente:
            pass
