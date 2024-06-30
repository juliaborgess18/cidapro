async function criarSolicitacao(event) {
    event.preventDefault(); 

    const idUsuario = document.getElementById('idUsuario').value.trim();
    const idPais = document.getElementById('idPais').value.trim();
    const idMotivo = document.getElementById('idMotivo').value.trim();

    const requestData = {
        status: "PENDENTE", 
        id_usuario: idUsuario,  
        id_pais: idPais,
        id_motivo: idMotivo
    };
    console.log(requestData);

    try {
        const response = await fetch('/solicitacao', {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) {
            throw new Error('Erro ao enviar a solicitação');
        }

        const data = await response.json();
        console.log('Solicitação enviada com sucesso:', data);
        alert('Solicitação enviada com sucesso!');
    } catch (error) {
        console.error('Erro ao enviar a solicitação:', error);
        alert('Erro ao enviar a solicitação');
    }
}

document.getElementById('pais').addEventListener('change', function() {
    var selectedValue = this.value;
    document.getElementById('idPais').value = selectedValue;
});

document.getElementById('motivo').addEventListener('change', function() {
    var selectedValue = this.value;
    document.getElementById('idMotivo').value = selectedValue;
});
