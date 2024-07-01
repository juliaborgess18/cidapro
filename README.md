# CidaPro

**Grupo**: Igor Almeida e Júlia Borges

Este é um projeto de aplicação web projetado para simplificar e facilitar o processo de retirada de cidadania estrangeira. Ele foi desenvolvido para a disciplina de Desenvolvimento Web do sétimo período do curso Cacharelado em Sistemas de Informação do Instituto Federal do Espírito Santo Campus Cachoeiro.
Neste sistema teremos dois tipo de usuários, o **Solicitante**, aquele que busca uma cidadania estrangeira e o **Examinador**, que é quem valida as solicitações dentro do sistema.

Este projeto pode ser acessado [clicando aqui](https://cidapro.cachoeiro.es/).


## ☕ Funcionalidades Implementadas
### Solicitante
* Criar Solicitações de Cidadania
* Visualizar Andamento
* Visualizar Histórico

### Examinador
* Visualizar o Solicitante
* Analisar as Solicitações


## 🐱‍🏍Práticas Utilizadas:
* Clean Architecture 
* Repositorys Pattern
* Data Transfer Objects (DTO)
* Mappers
* Autenticação
* Autorização


## 💻 Pré-requisitos
* Python 3
* fastapi
* uvicorn
* jinja2
* requests
* httpx
* httpie
* python-multipart
* bcrypt

## 🎬 Executando o Projeto
* Para instalar todas as dependências deste projeto, na raiz do projeto, abra o terminal e insira o seguinte o comando.
```console
    pip install -r requirements.txt
```

* Para executar, ainda no terminal, insira o comando
```console
    uvicorn main:app --reload
```

* O banco de dados em SQLite será gerado autômaticamente na primeira execução.

## 👉 Recriando o Banco
* Caso esteja em vista a necessidade de recriar o banco de dados, basta remover o arquivo **dados.db** presente no diretório raiz e executar o projeto novamente que o banco será recriado.
* Os dados de testes serão inseridos normalmente, caso deseje altera-los, eles estão presentes [clicando aqui](./infrastructure/data/).
* Para mudar o comportamento de geração autômatico de dados, você pode alterar o seguinte [método](./infrastructure/util/data_seeder.py).

## 📃 Documentação com Swagger
* Para acessar a documentação da API pelo Swagger, colocar o prefixo '/docs' ao final da url ou [clique aqui](http://localhost:8000/docs) com o projeto em execução.


## 👨‍💻 Autores
### Igor Almeida da Silva
[![Linkedin](https://img.shields.io/badge/-Linkedin-blue?style=for-the-badge&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/igoralmeidadasilva/)](https://www.linkedin.com/in/igoralmeidadasilva/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/igoralmeidadasilva)



### Júlia Borges Santos
[![Linkedin](https://img.shields.io/badge/-Linkedin-blue?style=for-the-badge&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/igoralmeidadasilva/)](https://www.linkedin.com/in/julia-borgess/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juliaborgess18)
