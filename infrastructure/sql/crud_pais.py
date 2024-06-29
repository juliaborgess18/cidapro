SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS pais(
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

SQL_SE_EXISTE = """
    SELECT COUNT(*) FROM pais WHERE id=?
"""

SQL_SELECIONAR_QUANTIDADE = """
    SELECT COUNT(*) FROM pais
"""

SQL_SELECIONAR_PAISES = """
    SELECT * FROM pais
"""

