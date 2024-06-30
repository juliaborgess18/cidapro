SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS motivo(
        id    INTEGER PRIMARY KEY AUTOINCREMENT
        ,nome TEXT NOT NULL
    )
"""

SQL_INSERIR = """
    INSERT INTO motivo(nome) 
    VALUES (?)
"""

SQL_VERIFICAR_EXISTENCIA = """
    SELECT COUNT(*) FROM motivo
"""

SQL_OBTER_TODOS = """
    SELECT *
    FROM motivo
"""