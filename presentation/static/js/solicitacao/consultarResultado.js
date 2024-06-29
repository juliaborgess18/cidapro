async function consultar(event) {
    event.preventDefault(); 
    const idSolicitacao = document.getElementById('idSolicitacao').value.trim();
    const idUsuario = document.getElementById('idUsuario').value.trim();
    console.log(idSolicitacao);
    // Verifica se o campo está preenchido
    if (!idSolicitacao) {
        alert("Por favor, informe o código de solicitação.");
        return;
    }

    try {
        const response = await fetch(`/solicitacao/${idSolicitacao}/${idUsuario}`);
        if (response.ok) {
            const data = await response.json();
            const status = data["Solicitação"] ? data["Solicitação"].status : "Solicitação não encontrada";
            document.getElementById('resultadoConsulta').innerHTML = `<label>${status}</label>`;
        } else {
            throw new Error('Erro ao consultar solicitação');
        }
    } catch (error) {
        console.error("Erro na requisição:", error);
        alert("Erro ao consultar a solicitação. Por favor, tente novamente mais tarde.");
    }
}