from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum

db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(225), nullable=False)

    def __repr__(self):
        return f'<Categoria {self.nome}>'
    
    def __str__(self):
        return self.nome
    

class Autor(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    ano_nascimento = db.Column(db.String(4), nullable=False)
    ano_morte = db.Column(db.String(4))

    def __repr__(self):
        return f'<Autor {self.nome}>'
    
    def __str__(self):
        return self.nome
    

class Livro(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    isnb = db.Column(db.String(13), unique=True, nullable=False)
    id_autor = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    ano_publicacao = db.Column(db.String(4), nullable=False)
    estoque = db.Column(db.String(3), nullable=False)
    
    autor = db.relationship('Autor', backref='livros')
    categoria = db.relationship('Categoria', backref='livros')

    def __repr__(self):
        return f'<Livro {self.titulo}>'
    
    def __str__(self):
        return self.titulo


class TipoUsuario(Enum):
    ADMIN = 'ADMIN'
    FUNCIONARIO = 'FUNCIONÁRIO'
    
class StatusAtividade(Enum):
    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'   

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    usuario = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255))
    telefone = db.Column(db.String(13))
    data_registro = db.Column(db.DateTime, default=datetime.utcnow)
    tipo_usuario = db.Column(db.Enum(TipoUsuario), nullable=False, default=TipoUsuario.ADMIN)
    status_atividade = db.Column(db.Enum(StatusAtividade), nullable=False, default=StatusAtividade.ATIVO)
    
    def __repr__(self):
        return f'<Usuário {self.usuario}>'
    

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255))
    data_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Cliente {self.nome}>'
    
    def __str__(self):
        return self.nome


class StatusEmprestimo(Enum):
    ATIVO = 'ATIVO'
    PENDENTE = 'PENDENTE'
    FINALIZADO = 'FINALIZADO'

class Emprestimo(db.Model):
    __tablename__ = 'emprestimos'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    id_livro = db.Column(db.Integer, db.ForeignKey('livros.id'))
    data_emprestimo = db.Column(db.DateTime, default=datetime.utcnow)
    data_devolucao = db.Column(db.DateTime, nullable=False)
    status_emprestimo = db.Column(db.Enum(StatusEmprestimo), nullable=False, default=StatusEmprestimo.ATIVO)

    cliente = db.relationship('Cliente', backref='emprestimos')
    livro = db.relationship('Livro', backref='emprestimos')  # Corrigido

    def __repr__(self):
        return f'<Empréstimo {self.id}>'
    

class HistoricoEmprestimo(db.Model):
    __tablename__ = 'historicos'

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    id_emprestimo = db.Column(db.Integer, db.ForeignKey('emprestimos.id'))
    data_conclusao = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref='historicos')
    emprestimo = db.relationship('Emprestimo', backref='historicos')

    def __repr__(self):
        return f'<Histórico {self.id}>'