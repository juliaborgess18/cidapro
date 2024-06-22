import json
import sqlite3
from typing import List, Optional

from domain.entities.solicitacao import Solicitacao
from infrastructure.sql.crud_solicitacao import *
from infrastructure.util.database import obter_conexao


class SolicitacaoRepo:

    @classmethod
    def criar_tabela(cls) -> None:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_CRIAR_TABELA)
        except sqlite3.Error as ex:
            print(ex)
    
    @classmethod
    def inserir_dados(cls) -> None:
        solicitacoes = []

        with open("infrastructure/data/solicitacoes.json", "r", encoding='utf-8') as f:
            dados = json.load(f)

        for dado in dados:
            solicitacao = Solicitacao()
            solicitacao.dh_solicitacao = dado['dh_solicitacao']
            solicitacao.status = dado['status']
            solicitacao.id_usuario = dado['id_usuario']
            solicitacao.id_pais = dado['id_pais']
            solicitacoes.append(solicitacao)
        
        for solicitacao in solicitacoes:
            try:
                with obter_conexao() as conexao:
                    cursor = conexao.cursor()
                    cursor.execute(
                        SQL_INSERIR,
                        (
                            solicitacao.dh_solicitacao
                            ,solicitacao.status
                            ,solicitacao.id_usuario
                            ,solicitacao.id_pais
                        ) 
                    ) 
            except sqlite3.Error as ex:
                print(ex)

    @classmethod
    def selecionar_todos(cls) -> List[Solicitacao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_SELECIONAR_TODOS).fetchall()
                solicitacoes = [Solicitacao(*tupla) for tupla in tuplas]
            return solicitacoes
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def selecionar_por_id(cls, id: str) -> Solicitacao:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_SELECIONAR_POR_ID,
                    (
                        id,
                    )
                ).fetchone()
                solicitacao = Solicitacao(*tupla)
            return solicitacao
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def inserir(cls, solicitacao: Solicitacao) -> Optional[Solicitacao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR,
                    (
                        solicitacao.dh_solicitacao
                        ,solicitacao.status
                        ,solicitacao.id_usuario
                        ,solicitacao.id_pais         
                    ),
                )
            if cursor.rowcount > 0:
                solicitacao.id = cursor.lastrowid
                return solicitacao 
        except sqlite3.Error as ex:
            print(ex)
            return None 

    @classmethod
    def alterar_status(cls, id: str, status: str):
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_STATUS,
                    (
                        status
                        ,id
                    ),   
                )
        except sqlite3.Error as ex:
            print(ex)

    @classmethod
    def remover(cls, id: str):
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_EXCLUIR,
                    (
                        id,
                    ),
                )
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