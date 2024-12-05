//CONFIGURAÇÕES POPUP PERFIL
const popupPerfil = document.getElementById('popup-overlay-perfil')
const abrePopupPerfil = document.getElementById('btn-abre-perfil')
const fechaPopupPerfil = document.getElementById('btn-fecha-perfil')

abrePopupPerfil.addEventListener('click', () => {
    popupPerfil.style.display = 'block';
});

fechaPopupPerfil.addEventListener('click', () => {
    popupPerfil.style.display = 'none';
});

popupPerfil.addEventListener('click', (e) => {
    if (e.target === popupPerfil) {
        popupPerfil.style.display = 'none';
    }
});


//CONFIGURAÇÕES POPUP EDIÇÃO
//CATEGORIAS
const popupCategoria = document.getElementById('popup-edicao-categoria');
const abrePopupCategoria = document.querySelectorAll('.btn-editar-categoria');
const fechaPopupCategoria = document.getElementById('btn-fecha-categoria'); 
const inputNomeCategoria = document.getElementById('nome-categoria-edicao');
const formCategoria = document.getElementById('form-edicao-categoria');

abrePopupCategoria.forEach((botao) => {
    botao.addEventListener('click', function () {
        popupCategoria.style.display = 'block';

        //Obtém dados do botão
        const id = this.getAttribute('data-id');
        const nome = this.getAttribute('data-nome');

        //Atualiza o valor do input e a ação do formulário
        inputNomeCategoria.value = nome;
        formCategoria.action = `/edita-categoria/${id}`;
    });
});

fechaPopupCategoria.addEventListener('click', () => {
    popupCategoria.style.display = 'none';
});

popupCategoria.addEventListener('click', (e) => {
    if (e.target === popupCategoria) {
        popupCategoria.style.display = 'none';
    }
});


//AUTORES
const popupAutor = document.getElementById('popup-edicao-autor');
const abrePopupAutor = document.querySelectorAll('.btn-editar-autor');
const fechaPopupAutor = document.getElementById('btn-fecha-autor');
const inputNomeAutor = document.getElementById('nome-autor-edicao');
const inputAnoNascimentoAutor = document.getElementById('ano-nascimento-edicao');
const inputAnoMorteAutor = document.getElementById('ano-morte-edicao');
const formAutor = document.getElementById('form-edicao-autor');

abrePopupAutor.forEach((botao) => {
    botao.addEventListener('click', function() {
        popupAutor.style.display = 'block';

        const id = this.getAttribute('data-id');
        const nome = this.getAttribute('data-nome');
        const anoNascimento = this.getAttribute('data-ano-nascimento');
        const anoMorte = this.getAttribute('data-ano-morte');

        inputNomeAutor.value = nome;
        inputAnoNascimentoAutor.value = anoNascimento;
        inputAnoMorteAutor.value = anoMorte;
        formAutor.action = `/edita-autor/${id}`;
    });
});

fechaPopupAutor.addEventListener('click', () => {
    popupAutor.style.display = 'none';
});

popupAutor.addEventListener('click', (e) => {
    if (e.target === popupAutor) {
        popupAutor.style.display = 'none';
    }
});


//LIVROS
const popupLivro = document.getElementById('popup-edicao-livro')
const abrePopupLivro = document.querySelectorAll('.btn-editar-livro')
const fechaPopupLivro = document.getElementById('btn-fecha-livro')
const inputTituloLivro = document.getElementById('titulo-edicao')
const inputIsnbLivro = document.getElementById('isnb-edicao')
const inputAutorLivro = document.getElementById('autor-edicao')
const inputCategoriaLivro = document.getElementById('categoria-edicao')
const inputAnoPublicacaoLivro = document.getElementById('ano-publicacao-edicao')
const inputEstoqueLivro = document.getElementById('estoque-edicao')
const formLivro = document.getElementById('form-edicao-livro')

abrePopupLivro.forEach((botao) => {
    botao.addEventListener('click', function() {
        popupLivro.style.display = 'block';

        const id = this.getAttribute('data-id');
        const titulo = this.getAttribute('data-titulo');
        const autor = this.getAttribute('data-autor');
        const categoria = this.getAttribute('data-categoria');
        const anoPublicacao = this.getAttribute('data-ano-publicacao');
        const isnb = this.getAttribute('data-isnb');
        const estoque = this.getAttribute('data-estoque');

        inputTituloLivro.value = titulo;
        inputAutorLivro.value = autor;
        inputCategoriaLivro.value = categoria;
        inputAnoPublicacaoLivro.value = anoPublicacao;
        inputIsnbLivro.value = isnb;
        inputEstoqueLivro.value = estoque;
        formLivro.action = `/edita-livro/${id}`;
    });
});

fechaPopupLivro.addEventListener('click', () => {
    popupLivro.style.display = 'none';
});

popupLivro.addEventListener('click', (e) => {
    if (e.target === popupLivro) {
        popupLivro.style.display = 'none';
    }
});