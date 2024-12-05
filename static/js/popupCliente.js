//CONFIGURAÇÕES POPUP EDIÇÃO
//CLIENTES
const popupCliente = document.getElementById('popup-edicao-cliente')
const abrePopupCliente = document.querySelectorAll('.btn-editar-cliente')
const fechaPopupCliente = document.getElementById('btn-fecha-cliente')
const inputNomeCliente = document.getElementById('cliente-nome-edicao')
const inputEmailCliente = document.getElementById('cliente-email-edicao')
const inputTelefoneCliente = document.getElementById('cliente-telefone-edicao')
const formCliente = document.getElementById('form-edicao-cliente')

abrePopupCliente.forEach((botao) => {
    botao.addEventListener('click', function() {
        popupCliente.style.display = 'block';

        const id = this.getAttribute('data-id')
        const nome = this.getAttribute('data-nome')
        const email = this.getAttribute('data-email')
        const telefone = this.getAttribute('data-telefone')

        inputNomeCliente.value = nome;
        inputEmailCliente.value = email;
        inputTelefoneCliente.value = telefone;
        formCliente.action = `/edita-cliente/${id}`;
    });
});

fechaPopupCliente.addEventListener('click', () => {
    popupCliente.style.display = 'none';
});

popupCliente.addEventListener('click', (e) => {
    if (e.target === popupCliente) {
        popupCliente.style.display = 'none';
    }
});