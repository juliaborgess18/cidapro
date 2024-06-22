SQL_CRIAR_TABELA = """
    CREATE TABLE pais(
        id    INTEGER PRIMARY KEY AUTOINCREMENT
        ,nome TEXT NOT NULL
    )
"""

SQL_INSERIR = """
    INSERT INTO pais (nome)
    VALUES(?)
"""

SQL_RESETAR = """
    DROP TABLE pais
"""

