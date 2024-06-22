SQL_CRIAR_TABELA =  """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        , nome            TEXT NOT NULL
        , cpf             TEXT NOT NULL UNIQUE
        , data_nascimento DATE NOT NULL
        , email           TEXT NOT NULL UNIQUE
        , senha           TEXT NOT NULL        
    )
"""

SQL_SELECIONAR_TODOS = """
    SELECT 
        * 
    FROM 
        usuario
"""

SQL_SELECIONAR_POR_ID = """
    SELECT
        *
    FROM
        usuario
    WHERE id=?
"""

SQL_ALTERAR = """
    UPDATE 
        usuario
    SET 
        nome=?
        ,data_nascimento=?
        ,email=?
    WHERE 
        id = ?
"""

SQL_INSERIR = """
    INSERT INTO usuario (nome, cpf, data_nascimento, email, senha)
    VALUES (?,?,?,?,?)
"""

SQL_EXCLUIR = """
    DELETE FROM usuario 
    WHERE id=?
"""

