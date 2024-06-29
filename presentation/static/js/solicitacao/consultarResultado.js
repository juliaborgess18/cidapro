async function consultar(event) {
    event.preventDefault(); 
    const id = document.getElementById('idSolicitacao').value.trim();

    // Verifica se o campo está preenchido
    if (!id) {
        alert("Por favor, informe o código de solicitação.");
        return;
    }

    try {
        const response = await fetch(`/solicitacao/${id}`);
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