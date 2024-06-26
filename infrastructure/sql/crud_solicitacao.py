SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS solicitacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        , dh_solicitacao    TEXT NOT NULL
        , status            TEXT NOT NULL
        , id_usuario        INTEGER NOT NULL
        , id_pais           INTEGER NOT NULL
        , id_motivo         TEXT NOT NULL
        , FOREIGN KEY (id_usuario)    REFERENCES usuario(id)
        , FOREIGN KEY (id_pais)       REFERENCES pais(id)
        , FOREIGN KEY (id_motivo)     REFERENCES motivo(id)
    )
"""

SQL_SELECIONAR_TODOS = """
    SELECT 
        * 
    FROM 
        solicitacao
"""

# SQL_SELECIONAR_TODOS_POR_USUARIO_LOGADO = """
#     SELECT 
#         * 
#     FROM 
#         solicitacao
#     WHERE 
#         id_usuario = ?
# """

SQL_SELECIONAR_TODOS_POR_USUARIO_LOGADO = """
    SELECT 
        solicitacao.*, 
        strftime('%Y-%m-%d %H:%M:%S', dh_solicitacao) ,
        p.nome AS nome_pais, 
        m.nome AS nome_motivo
    FROM 
        solicitacao
    INNER JOIN 
        pais p ON p.id = solicitacao.id_pais
    INNER JOIN 
        motivo m ON m.id = solicitacao.id_motivo
    WHERE 
        solicitacao.id_usuario = ?;
"""

SQL_SELECIONAR_POR_ID = """
    SELECT 
        * 
    FROM 
      solicitacao
    WHERE 
        id = ?
"""
SQL_SELECIONAR_POR_ID_USUARIO = """
    SELECT 
        * 
    FROM 
      solicitacao
    WHERE 
        id_usuario = ?
"""

SQL_SELECIONAR_POR_ID_E_USUARIO_LOGADO = """
    SELECT 
        * 
    FROM 
      solicitacao
    WHERE 1 = 1
        AND id             = ?
        AND id_usuario     = ?
"""

SQL_INSERIR = """
    INSERT INTO solicitacao(dh_solicitacao, status, id_usuario, id_pais, id_motivo) 
    VALUES (?, ?, ?, ?, ?)
"""

SQL_ALTERAR_STATUS = """
    UPDATE 
        solicitacao
    SET 
        status=?
    WHERE 
        id=?
"""

SQL_EXCLUIR = """
    DELETE FROM solicitacao
    WHERE id=?
"""

SQL_SE_EXISTE = """
    SELECT COUNT(*) FROM solicitacao WHERE id=?
"""

SQL_SELECIONAR_QUANTIDADE = """
    SELECT COUNT(*) FROM solicitacao
"""

SQL_SELECIONAR_POR_ID_VISUALIZACAO = """
    SELECT 
        s.id,
        s.dh_solicitacao,
        s.status,
        p.nome AS pais,
        m.nome AS motivo 
    FROM 
      solicitacao s
    INNER JOIN 
        pais p ON p.id = s.id_pais
    INNER JOIN 
        motivo m ON m.id = s.id_motivo
    WHERE 
        s.id = ?
"""
