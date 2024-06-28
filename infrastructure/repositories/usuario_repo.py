import json
import sqlite3
from typing import List, Optional

import bcrypt
from domain.entities.usuario import Usuario
from infrastructure.sql.crud_usuario import *
from infrastructure.util.database import obter_conexao

class UsuarioRepo:
    
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
                tuplas = cursor.execute(SQL_SELECIONAR_TODOS).fetchall()
                usuarios = [Usuario(*tupla) for tupla in tuplas]
            return usuarios
        except sqlite3.Error as ex:
            print(ex)
            return None
    
    @classmethod
    def selecionar_por_id(cls, id:str) -> Usuario:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_SELECIONAR_POR_ID,
                    (
                        id,
                    )
                ).fetchone()
                usuario = Usuario(*tupla)
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
                        id,
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
    def selecionar_por_email(cls, email:str) -> Usuario:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_SELECIONAR_POR_EMAIL,
                    (
                        email,
                    )
                ).fetchone()
                usuario = Usuario(*tupla)
            return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None
    
    @classmethod
    def alterar_token(cls, id: int, token: str) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR_TOKEN, (token, id))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod
    def selecionar_por_token(cls, token:str) -> Usuario:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_SELECIONAR_POR_TOKEN,
                    (
                        token,
                    )
                ).fetchone()
                if tupla:
                    usuario = Usuario(*tupla)
                    return usuario
                else:
                    return None
        except sqlite3.Error as ex:
            print(ex)
            return None
        
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
    def inserir_dados(cls):
        if cls.selecionar_quantidade() == 0:
            usuarios = []

            with open("infrastructure/data/usuarios.json", 'r', encoding='utf-8') as f:
                dados = json.load(f)
                
            for dado in dados:
                usuario = Usuario()
                
                usuario.nome = dado["nome"]
                usuario.cpf = dado["cpf"]
                usuario.data_nascimento = dado["data_nascimento"]
                usuario.email = dado["email"]
                usuario.senha = bcrypt.hashpw(dado["senha"].encode(), bcrypt.gensalt()).decode()
                usuarios.append(usuario)
            
            for usuario in usuarios:
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
                except sqlite3.Error as ex:
                    print(ex)

        