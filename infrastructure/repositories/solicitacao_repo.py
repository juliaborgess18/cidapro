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
    def selecionar_todos(cls,) -> List[Solicitacao]:
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
    def selecionar_todos_por_usuario_logado(cls, id_usuario:str) -> List[tuple]:
        tuplas = []
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_SELECIONAR_TODOS_POR_USUARIO_LOGADO, (id_usuario,)).fetchall()
            return tuplas
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def selecionar_por_id(cls, id: str) -> Optional[Solicitacao]:
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
                    solicitacao = Solicitacao(*tupla)
                    return solicitacao
                else:
                    return None
        except sqlite3.Error as ex:
            print(ex)
            return None
    
    @classmethod
    def selecionar_por_id_e_usuario_logado(cls, id_solicitacao: str, id_usuario: str) -> Optional[Solicitacao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_SELECIONAR_POR_ID_E_USUARIO_LOGADO,
                    (
                         id_solicitacao
                        ,id_usuario
                    )
                ).fetchone()
                if tupla is not None:
                    solicitacao = Solicitacao(*tupla)
                    return solicitacao
                else:
                    return None
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
                        ,solicitacao.id_motivo     
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
    def inserir_dados(cls) -> None:
        if cls.selecionar_quantidade() == 0:
            solicitacoes = []
            with open("infrastructure/data/solicitacoes.json", "r", encoding='utf-8') as f:
                dados = json.load(f)

            for dado in dados:
                solicitacao = Solicitacao()
                solicitacao.dh_solicitacao = dado['dh_solicitacao']
                solicitacao.status = dado['status']
                solicitacao.id_usuario = dado['id_usuario']
                solicitacao.id_pais = dado['id_pais']
                solicitacao.id_motivo = dado['id_motivo']
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
                                ,solicitacao.id_motivo
                            ) 
                        ) 
                except sqlite3.Error as ex:
                    print(ex)

    @classmethod
    def selecionar_por_id_usuario(cls, id_usuario: str) -> Optional[List[Solicitacao]]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_SELECIONAR_POR_ID, (id_usuario,)).fetchall()
                if tuplas is not None:
                    solicitacoes = [Solicitacao(*tupla) for tupla in tuplas]
                    return solicitacoes
                return None
        except sqlite3.Error as ex:
            print(ex)
            return None