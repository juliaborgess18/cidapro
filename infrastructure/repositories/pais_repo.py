import sqlite3
import json
from typing import List, Optional
from domain.entities.pais import Pais
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
    def se_existe(cls, id: str) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_SE_EXISTE, (id,)).fetchone()
                resultado = tupla[0]
                if resultado == 0 or resultado == None:
                    return False
                return True
        except sqlite3.Error as ex:
            print(ex)

    @classmethod
    def selecionar_quantidade(cls) -> int:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_SELECIONAR_QUANTIDADE).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def inserir_dados(cls,):
        if cls.selecionar_quantidade() == 0:
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

    @classmethod
    def obter_paises(cls) -> List[Pais]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_SELECIONAR_PAISES)
                resultados = cursor.fetchall()
                paises = [(codigo, nome) for codigo, nome in resultados]
                return paises
        except sqlite3.Error as ex:
            print(ex)
            return []
                    
    @classmethod
    def selecionar_por_id(cls, id: str) -> Optional[Pais]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_SELECIONAR_POR_ID,
                    (
                        id,
                    )
                ).fetchone()
                if tupla is not None:
                    pais = Pais(*tupla)
                    return pais
                else:
                    return None
        except sqlite3.Error as ex:
            print(ex)
            return None
        