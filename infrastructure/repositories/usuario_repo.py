import sqlite3
from typing import List, Optional
from domain.entities.usuario import Usuario
from infrastructure.sql.crud import *
from infrastructure.util.database import obter_conexao

class ClienteRepo:
    
    @classmethod
    def criar_tabela(cls,):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)
    
    @classmethod
    def selecionar_todos(cls, ) -> List[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                usuarios = cursor.execute(SQL_SELECIONAR_TODOS).fetchall()
            return usuarios
        except sqlite3.Error as ex:
            print(ex)
            return None
    
    @classmethod
    def selecionar_por_id(cls, id:str) -> Usuario:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                usuario = cursor.execute(
                    SQL_SELECIONAR_POR_ID,
                    (
                        id
                    )
                ).fetchone()
            return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None
            
    @classmethod 
    def inserir(cls, usuario: Usuario) ->  Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR,
                    (
                        usuario.nome            
                        ,usuario.cpf             
                        ,usuario.data_nascimento 
                        ,usuario.email           
                        ,usuario.senha           
                    ),
                )
            if cursor.rowcount > 0:
                usuario.id = cursor.lastrowid
                return usuario 
        except sqlite3.Error as ex:
            print(ex)
            return None 
            
    @classmethod 
    def deletar(cls, id: str):
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_EXCLUIR,
                    (
                        id
                    ),
                )
        except sqlite3.Error as ex:
            print(ex)
            
    @classmethod
    def alterar(cls, usuario: Usuario) -> Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR,
                    (
                         usuario.nome
                        ,usuario.data_nascimento
                        ,usuario.email
                        ,usuario.id
                    ),   
                )
            return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None 
        
                
            