function ClickBtnAceitar(id) {

    url = '/usuario/aceitar_solicitacao?id_solicitacao=5'
    var response = fetch(url, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        location.reload()
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function ClickBtnNegar(id) {

    url = '/usuario/negar_solicitacao?id_solicitacao=5'
    var response = fetch(url, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        location.reload()
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function ClickBtnCancelar(id) {

    url = '/usuario/cancelar_solicitacao?id_solicitacao=5'
    var response = fetch(url, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        location.reload()
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}