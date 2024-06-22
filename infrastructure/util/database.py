import sqlite3

def obter_conexao():
    conn = sqlite3.connect("dados.db")
    conn.execute("PRAGMA foreign_keys = ON")

    return conn