//CONFIGURAÇÕES POPUP EDIÇÃO
//EMPRÉSTIMOS
const popupEmprestimo = document.getElementById('popup-edicao-emprestimo')
const abrePopupEmprestimo = document.querySelectorAll('.btn-editar-emprestimo')
const fechaPopupEmprestimo = document.getElementById('btn-fecha-emprestimo')
const inputLivroEmprestimo = document.getElementById('livro-edicao')
const inputClienteEmprestimo = document.getElementById('cliente-edicao')
const inputDataEmprestimo = document.getElementById('data-emprestimo-edicao')
const inputDataDevolucao = document.getElementById('data-devolucao-edicao')
const inputStatusEmprestimo = document.getElementById('status-emprestimo-edicao')
const formEmprestimo = document.getElementById('form-edicao-emprestimo')

abrePopupEmprestimo.forEach((botao) => {
    botao.addEventListener('click', function() {
        popupEmprestimo.style.display = 'block';

        const id = this.getAttribute('data-id')
        const livro = this.getAttribute('data-livro')
        const cliente = this.getAttribute('data-cliente')
        const data_emprestimo = this.getAttribute('data-data-emprestimo')
        const data_devolucao = this.getAttribute('data-data-devolucao')
        const status_emprestimo = this.getAttribute('data-status-emprestimo')

        inputLivroEmprestimo.value = livro;
        inputClienteEmprestimo.value = cliente;
        inputDataEmprestimo.value = data_emprestimo;
        inputDataDevolucao.value = data_devolucao;
        inputStatusEmprestimo.value = status_emprestimo;
        formEmprestimo.action = `/edita-emprestimo/${id}`;
    });
});

fechaPopupEmprestimo.addEventListener('click', () => {
    popupEmprestimo.style.display = 'none';
});

popupEmprestimo.addEventListener('click', (e) => {
    if (e.target === popupEmprestimo) {
        popupEmprestimo.style.display = 'none';
    }
});
