import sqlite3
import json
from infrastructure.sql.crud_pais import *
from infrastructure.util.database import obter_conexao

paises = []

class PaisRepo:

    @classmethod
    def criar_tabela(cls,):
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_CRIAR_TABELA)
        except sqlite3.Error as ex:
            print(ex)
    
    @classmethod
    def resetar_tabelar(cls,):
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_RESETAR)
        except sqlite3.Error as ex:
            print(ex)
            
    @classmethod
    def inserir_dados(cls,):
        with open("infrastructure/data/paises.json", 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
        for dado in dados:
            pais = [dado["nome_pais"]]
            paises.append(pais)
        
        for pais in paises:
            try:
                with obter_conexao() as conexao:
                    cursor = conexao.cursor()
                    cursor.execute(SQL_INSERIR, (pais))
            except sqlite3.Error as ex:
                print(ex)
