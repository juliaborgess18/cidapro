SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS solicitacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        , dh_solicitacao    TEXT NOT NULL
        , status            TEXT NOT NULL
        , id_usuario        INTEGER NOT NULL
        , id_pais           INTEGER NOT NULL
        , FOREIGN KEY (id_usuario)    REFERENCES usuario(id)
        , FOREIGN KEY (id_pais)       REFERENCES pais(id)
    )
"""

SQL_SELECIONAR_TODOS = """
    SELECT 
        * 
    FROM 
        solicitacao
"""

SQL_SELECIONAR_POR_ID = """
    SELECT 
        * 
    FROM 
      solicitacao
    WHERE 
        id = ?
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
    INSERT INTO solicitacao(dh_solicitacao, status, id_usuario, id_pais) 
    VALUES (?, ?, ?, ?)
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