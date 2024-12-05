//CONFIGURAÇÕES POPUP EDIÇÃO
//FUNCIONÁRIOS
const popupFuncionario = document.getElementById('popup-edicao-funcionario')
const abrePopupFuncionario = document.querySelectorAll('.btn-editar-usuario')
const fechaPopupFuncionario = document.getElementById('btn-fecha-funcionario')
const inputNomeFuncionario = document.getElementById('nome-edicao')
const inputUsuarioFuncionario = document.getElementById('usuario-edicao')
const inputEmailFuncionario = document.getElementById('email-edicao')
const inputTelefoneFuncionario = document.getElementById('telefone-edicao')
const inputTipoUsuarioFuncionario = document.getElementById('tipo-usuario-edicao')
const inputStatusAtividadeFuncionario = document.getElementById('status-atividade-edicao')
const inputSenhaFuncionario = document.getElementById('senha-edicao')
const formFuncionario = document.getElementById('form-edicao-funcionario')

abrePopupFuncionario.forEach((botao) => {
    botao.addEventListener('click', function() {
        popupFuncionario.style.display = "block";

        const id = this.getAttribute('data-id')
        const nome = this.getAttribute('data-nome')
        const usuario = this.getAttribute('data-usuario')
        const email = this.getAttribute('data-email')
        const telefone = this.getAttribute('data-telefone')
        const tipo_usuario = this.getAttribute('data-tipo-usuario')
        const status_atividade = this.getAttribute('data-status-atividade')
        const senha = this.getAttribute('data-senha')

        inputNomeFuncionario.value = nome;
        inputUsuarioFuncionario.value = usuario;
        inputEmailFuncionario.value = email;
        inputTelefoneFuncionario.value = telefone;
        inputTipoUsuarioFuncionario.value = tipo_usuario;
        inputStatusAtividadeFuncionario.value = status_atividade;
        inputSenhaFuncionario.value = senha;
        formFuncionario.action = `/edita-funcionario/${id}`;
    });
});

fechaPopupFuncionario.addEventListener('click', () => {
    popupFuncionario.style.display = 'none';
});

popupFuncionario.addEventListener('click', (e) => {
    if (e.target === popupFuncionario) {
        popupFuncionario.style.display = 'none';
    }
});